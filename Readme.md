### Docker
`docker build -t test-holy .`

`docker run -p 80:80 -t test-holy`

### Run Tests
`cd app/ && python -m unittest test_clv_prediction.py`
