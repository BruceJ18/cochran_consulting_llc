from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    SubmitField, PasswordField
    )
from wtforms.validators import (
    InputRequired, 
    Email
    )




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")