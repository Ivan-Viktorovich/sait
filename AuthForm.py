from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AuthF(FlaskForm):
    email= EmailField("Укажите электронную почту", validators=[DataRequired()])
    password= PasswordField("Введите пароль", validators=[DataRequired()])
    submit= SubmitField("Вход")