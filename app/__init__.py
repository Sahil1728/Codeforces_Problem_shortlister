from flask import Flask
from .routes import main

def app_init():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app