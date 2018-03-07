from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

from app.util.auth2 import get_account
from app.util.validators import RegisteredEmail


class ResetPassword(FlaskForm):
    """ResetPassword

    This form allows a user to submit their email to have their password
    reset.

    We extend the self.validate function per this example snippet:
    http://flask.pocoo.org/snippets/64/

    """

    email = StringField('Email', validators=[
        Email(),
    ])

    submit = SubmitField('Login')


    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.account = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        account = get_account(self.email.data)

        if account is None:
            self.email.errors.append('This email is not registered.')
            return False

        self.account = account
        return True
