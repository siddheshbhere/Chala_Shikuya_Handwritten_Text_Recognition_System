from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from teprojectfinal.data import user

class RegiForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = IntegerField('contact',validators=[DataRequired(),
            NumberRange(min=7000000000,max=9999999999)])
    password = PasswordField('Password', 
                        validators=[DataRequired(),Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        u = user.query.filter_by(username=username.data).first()
        if u:
            raise ValidationError('That username is taken')

    def validate_email(self, email):
        e = user.query.filter_by(email=email.data).first()
        if e:
            raise ValidationError('That email is taken')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        e = user.query.filter_by(email=email.data).first()
        if e is None:
            raise ValidationError('No account found with that email')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                        validators=[DataRequired(),Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset PasswordField')