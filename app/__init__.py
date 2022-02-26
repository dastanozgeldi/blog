from flask import Flask

from app import commands, main

from .config import config
from .extensions import csrf_protect, db, migrate


def create_app():
    """Create application factory."""
    app = Flask(__name__)
    app.config.from_object(config[app.config["ENV"]])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register app extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    csrf_protect.init_app(app)
    return None


def register_blueprints(app):
    """Plug blueprints."""
    app.register_blueprint(main.bp)
    return None


def register_commands(app):
    """Register custom commands."""
    app.cli.add_command(commands.lint)
    return None
