from flask import Flask
    return app

    app.register_blueprint(main)

    from app.routes import main

    app.config.from_object("app.config.Config")
    app = Flask(__name__)
def create_app():



