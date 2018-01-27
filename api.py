from flask import Flask, g
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)


DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


class HelloWorld(Resource):
    def get(self):
        init_db()
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)