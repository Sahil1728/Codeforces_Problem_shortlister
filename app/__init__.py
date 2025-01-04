from flask import Flask

def app_init():
    app = Flask(__name__)
    app.config.from_object('config')

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)
        return app