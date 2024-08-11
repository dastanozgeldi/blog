from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.database import db
from app.models import Post

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'solar'

admin = Admin(app, name='Dastan Ozgeldi', template_mode='bootstrap4')
admin.add_view(ModelView(Post, db.session))

app.run()
