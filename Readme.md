### Docker
`docker build -t test-holy .`

`docker run -p 80:80 -t test-holy`

### Test API
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost/customers/<CUSTOMER_ID>`


### Run Tests
`cd app/ && python -m unittest test_clv_prediction.py`
