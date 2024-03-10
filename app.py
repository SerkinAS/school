import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from routes.routes import route

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()
migrate = Migrate()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('configs.config')
    db = SQLAlchemy(flask_app)
    migrate.init_app(flask_app, db)
    flask_app.register_blueprint(route)
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
