"""Here all Flask-exts are defined, then initialized in `__init__.py`"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf_protect = CSRFProtect()
