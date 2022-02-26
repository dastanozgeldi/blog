from datetime import datetime

import mistune

from .database import Column, PkModel, db


class Post(PkModel):
    __tablename__ = "posts"
    pub_date = Column(db.DateTime, nullable=False, default=datetime.utcnow())
    title = Column(db.String(100), nullable=False)
    brief = Column(db.String(100), nullable=False)
    content = Column(db.String, nullable=False)
    modified = Column(db.Boolean, default=False, nullable=False)
    mod_date = Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Post('{self.title}', '{self.pub_date}')"

    @property
    def get_html_content(self):
        return mistune.html(self.content)
