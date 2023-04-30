from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Lf (FlaskForm):
    name= StringField("Имя", validators=[DataRequired()])
    email= EmailField("Укажите электронную почту", validators=[DataRequired()])
    password= PasswordField("Введите пароль", validators=[DataRequired()])
    password_again= PasswordField("Повторить пароль", validators=[DataRequired()])
    remember_me= BooleanField("Запомнить меня")
    submit= SubmitField("Зарегистрироваться")
