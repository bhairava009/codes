from flask import Flask

app = Flask(__name__)

# A decorator for registering a route with the given/default URL
@app.route('/')
def hello():
    return "Hello, I am learning Flask for the first time!"