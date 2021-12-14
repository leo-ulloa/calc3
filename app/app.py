"""A simple flask web app"""
from flask import Flask
from controllers.index_controller import IndexController
from controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """A simple flask web app"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """A simple flask web app"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """A simple flask web app"""
    return CalculatorController.post()
