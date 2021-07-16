from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, ValidationError, EqualTo, Email


# from .app import User


class Length(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = u'Field must be between %i and %i characters long.' % (min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)


length = Length


# 定义的表单都需要继承自FlaskForm
class LoginForm(FlaskForm):
    # 密码不支持default提示，故用户名也未设提示
    username = StringField('username', validators=[DataRequired(),
                                                   Length(2, 10)],
                           default="")
    password = PasswordField('password', validators=[DataRequired(),
                                                     Length(6, 14)],
                             default="")

# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Length(1, 60), Email()])
#     username = StringField('Username', validators=[DataRequired(), Length(1, 60),
#                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#                                                           'username must have only letters, numbers dots or underscores')])
#     password = PasswordField('Password',
#                              validators=[DataRequired(), EqualTo('password2', message='password must match')])
#     password2 = PasswordField('Confirm password', validators=[DataRequired()])
#
#     def validate_email(self, field):
#         if User.objects.filter(email=field.data).count() > 0:
#             raise ValidationError('Email already registered')
#
#     def validate_username(self, field):
#         if User.objects.filter(username=field.data).count() > 0:
#             raise ValidationError('Username has exist')
