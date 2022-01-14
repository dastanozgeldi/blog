import os
import click
from flask.cli import with_appcontext
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.2.0'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    db_path = os.path.join(app.instance_path, "dev.sqlite")
    db_url = f"sqlite:///{db_path}"
    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)


    app.config.from_mapping(
        SECREY_KEY="dev",
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    app.cli.add_command(init_db)

    app.add_url_rule("/", endpoint="index")

    return app


@click.command("init-db")
@with_appcontext
def init_db():
    db.drop_all()
    db.create_all()
    click.secho("Initialized the database.", fg="green")
