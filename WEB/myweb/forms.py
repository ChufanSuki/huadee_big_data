from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Regexp, ValidationError, EqualTo, Email, InputRequired, Optional

coin_types = ["CRV", "AMP", "MDX", "ZEN", "XMR", "CEL", "USDC", "XRP", "BTC", "FTM", "HOT", "SHIB", "RUNE", "AVAX",
              "EGLD", "VET", "KCS", "XTZ", "BTG", "DGB", "BNT", "KLAY", "XDC", "STX", "AR", "PAX", "COMP", "USDT",
              "XEM", "DOGE", "NANO", "MANA""TFUEL", "AAVE", "ATOM", "BSV", "CAKE", "SNX", "SC", "ALGO", "TEL", "FIL",
              "NEXO", "UST", "FTT", "LUNA",
              "ZRX", "DAI", "TRX", "OKB", "BTCB", "ADA", "ZIL", "YFI", "LINK", "CHZ", "BAT", "THETA", "BCH", "CHSB",
              "DCR", "LEO", "QNT", "BUSD", "UNI", "ZEC", "HNT", "ENJ", "AXS", "XLM", "BNB", "HT", "EQUAD", "DOT", "LTC",
              "WAVES", "QTUM", "MIOTA", "NEAR", "MATIC", "FLOW", "CELO", "ICX", "ICP", "EOS", "TUSD", "KSM", "DASH",
              "GRT", "ONE", "BTT", "SUSHI", "HBAR", "WBTC", "NEO", "ONT", "ETH", "SOL", "MKR", "ETC", ]


# 判断长度validator
class Length(object):
    def __init__(self, min=-1, max=-1, element='', message=None):
        self.min = min
        self.max = max
        self.element = element
        if not message:
            message = u'%s字数限制在 %i 到 %i 之间' % (element, min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)


length = Length


# 登录界面表单
class LoginForm(FlaskForm):
    # 密码不支持default提示，故用户名也未设提示
    username = StringField('username', validators=[DataRequired(),
                                                   Length(2, 10, '用户名')],
                           default="")
    password = PasswordField('password', validators=[DataRequired(),
                                                     Length(6, 14, '密码')],
                             default="")


# admin界面coin选择表单
class AdminCoinSelectForm(FlaskForm):
    selectCoin = SelectField('selectCoin', validators=[Optional()],
                             # choices=[("BTC", "BTC"), ("ETH", "ETH"), ("USDT", "USDT")],
                             choices=list([coin, coin] for coin in coin_types),
                             coerce=str
                             )

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
