from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class FlairForm(FlaskForm):
    URL = StringField('URL',validators=[DataRequired()])
    submit = SubmitField('Submit')

