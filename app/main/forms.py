from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(3, 100, "Title too short")])
    brief = StringField(
        validators=[DataRequired(), Length(3, 100, "Brief description too short")]
    )
    content = TextAreaField()
    submit = SubmitField()
