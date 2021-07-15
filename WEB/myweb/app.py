from os import name
from flask import Flask,render_template,redirect,request,url_for,flash
from flask.helpers import flash
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
import config
from urllib.parse import urlparse, urljoin
import pymysql
import mysql
# from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '1xasada'
app.debug = True
app.config.from_object(config)
login_manager = LoginManager(app)

# 指定登录的URL
login_manager.login_view = 'login1'

class User(UserMixin):
    pass

# 构造一个用户类对象,并使用用户名作为ID
# 回调函数
@login_manager.user_loader
def load_user(username):
        curr_user = User()
        curr_user.id = username
        return curr_user
        
# 登录功能
@app.route('/login1',methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    sql = "select name from user where name=\'"+username+"\' and pwd=\'"+pwd+"\';"
    user1 = mysql.query(sql)
    if len(user1) != 0:
        username = user1[-1][-1]
        curr_user = User()
        curr_user.id = username
        login_user(curr_user)
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

# 大数据面板
@app.route('/index',methods = ['GET','POST'])
@login_required
def index():
    if request.method == 'POST':
        return redirect(url_for('/index'))
    return render_template("index.html")

# 登出
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# 注册
@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    username = request.form.get('username')
    pwd1 = request.form.get('pwd1')
    pwd2 = request.form.get('pwd2')
    email = request.form.get('email')
    sql = "select name from user where name=\'"+username+"\';"
    user1 = mysql.query(sql)
    if username == "":
        flash("用户名不能为空！")
        return render_template('register.html')
    elif len(user1) != 0:
        flash("用户名已存在！")
        return render_template('register.html')
    elif pwd1 != pwd2:
        flash('两次密码不一致！')
        print("mima")
        return render_template('register.html')
    else:
        sql = "insert into user value(\'" + username +"\',\'" + pwd1 + "\',\'" + email + "\');"
        # print(sql)
        flag = mysql.insert(sql)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()