from flask import Flask, g, jsonify, make_response, abort
from flask_restful import Resource, Api
# from flask.ext import FlaskUUID
import sqlite3 as sql

app = Flask(__name__)
# FlaskUUID(app)
api = Api(app)

DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    db.row_factory = sql.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/customers/<string:customer_id>', methods=['GET'])
def get_data(customer_id):
    prediction = query_db('select value from predictions where customer_id = ?', [customer_id], one=True)

    print(type(prediction))

    if prediction is None:
        abort(404)

    return jsonify({'success': True,
                    'value': prediction['value']})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


class HelloWorld(Resource):
    def get(self):
        # init_db()
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
