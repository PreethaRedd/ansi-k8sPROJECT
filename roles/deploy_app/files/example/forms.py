from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


FIELD_CLASSES = 'input'


class ExampleForm(FlaskForm):
    first_name = StringField(
        'First Name',
        render_kw={
            'class': FIELD_CLASSES,
            'placeholder': 'User\'s first name'
        }
    )
    last_name = StringField(
        'Last Name',
        render_kw={
            'class': FIELD_CLASSES,
            'placeholder': 'User\'s surname'
        }
    )
    hobby = StringField(
        'Hobby',
        render_kw={
            'class': FIELD_CLASSES,
            'placeholder': 'User\'s favourite hobby'
        }
    )
    submit = SubmitField(
        'Submit',
        render_kw={
            'class': 'button is-primary'
        }
    )