from os import name
from flask import Flask,render_template,redirect,request,url_for,flash,jsonify,session
from flask.helpers import flash
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
import config
from urllib.parse import urlparse, urljoin
import mysql
import pymysql
import random
from flask_mail import Mail,Message
import hashlib

app = Flask(__name__)
app.secret_key = '1xasada'
app.debug = True
app.config.from_object(config)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = "587"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "1501138908@qq.com"
app.config['MAIL_PASSWORD'] = "jvyfhfsxzhgzbace"
app.config['MAIL_DEFAULT_SENDER'] = "1501138908@qq.com"
login_manager = LoginManager(app)
mail = Mail(app)

# 指定登录的URL
login_manager.login_view = 'login1'

mainstream_currency = ['BTC','ETH','USDT','XRP','BCH','LTC','BNB','LINK','DOT','ADA']


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
    # 加密
    hs = hashlib.sha1()
    data = str(pwd)
    hs.update(data.encode())
    # 加盐
    hs.update("13sda23".encode())
    hsvar = hs.hexdigest()
    sql = "select name from user where name=\'"+username+"\' and pwd=\'"+hsvar+"\';"
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
    else:
        code = request.form.get('valid')
        if str(session['code']).upper() == str(code).upper():
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
                # 加密
                hs = hashlib.sha1()
                data = str(pwd1)
                hs.update(data.encode())
                # 加盐
                hs.update("13sda23".encode())
                hsvar = hs.hexdigest()
                sql = "insert into user value(\'" + username +"\',\'" + hsvar + "\',\'" + email + "\');"
                flag = mysql.insert(sql)
                return redirect(url_for('login'))
        else:
            return render_template('register.html')

# 验证用户名是否存在
@app.route('/validateUniqueName',methods = ['GET','POST'])
def validateUniqueName():
    res = {'data':''}
    if request.method == 'GET':
        return render_template('register.html')
    username = request.form.get('username')
    sql = "select name from user where name=\'"+username+"\';"
    user1 = mysql.query(sql)
    flag = "True"
    if len(user1) != 0:
        flag = "False"
    res['data'] = flag
    return jsonify(res)

# 邮箱验证码
# 随机数函数
def random_str():
    _str = '1234567890abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(_str) for i in range(4))

# 发送邮件
@app.route('/send_email',methods = ['GET','POST'])
def send_email():
    res = {'data':''}
    if request.method == 'POST':
        return render_template('register.html')
    elif request.method == 'GET':
        msg = ""
        email = request.args.get('email')
        email_code = random_str()
        msg = Message('数字货币大数据分析平台注册',recipients=[email],body="您的验证码是:%s" %email_code)
        mail.send(msg) # 发送
        res['data'] = str(email_code)
        session['code'] = email_code
        return jsonify(res)
    else:
        res['data'] = "error"
        return jsonify(res)

# 重置密码发送邮件
@app.route('/send_email_forget',methods = ['GET','POST'])
def send_email_forget():
    res = {'data':'','email':''}
    if request.method == 'POST':
        return render_template('forget.html')
    elif request.method == 'GET':
        username = request.args.get('username')
        email_code = random_str()
        sql = "select email from user where name=\'"+username+"\';"
        user1 = mysql.query(sql)
        email = user1[-1][-1]
        msg = ""
        msg = Message('数字货币大数据分析平台重置密码',recipients=[email],body="您的验证码是:%s" %email_code)
        mail.send(msg) # 发送
        res['data'] = 'success'
        # temp_email = email.split('@')
        # temp_email[0]
        res['email'] = str(email)
        session['code'] = email_code
        return jsonify(res)
    else:
        res['data'] = "error"
        return jsonify(res)
    
# 验证码检验
@app.route('/checkCode',methods = ['GET','POST'])
def checkCode():
    res = {'data':''}
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form.get('email')
    res['data'] = session['code']
    return jsonify(res)

# 忘记密码
@app.route('/forget',methods = ['GET','POST'])
def forget():
    if request.method == 'GET':
        return render_template('forget.html')
    else:
        code = request.form.get('valid')
        if str(session['code']).upper() == str(code).upper():
            username = request.form.get('username')
            pwd1 = request.form.get('pwd1')
            pwd2 = request.form.get('pwd2')
            email = request.form.get('email')
            sql = "select name from user where name=\'"+username+"\';"
            user1 = mysql.query(sql)
            if username == "":
                flash("用户名不能为空！")
                return render_template('forget.html')
            elif len(user1) == 0:
                flash("用户名不存在！")
                return render_template('forget.html')
            elif pwd1 != pwd2:
                flash('两次密码不一致！')
                print("mima")
                return render_template('forget.html')
            else:
                # 加密
                hs = hashlib.sha1()
                data = str(pwd1)
                hs.update(data.encode())
                # 加盐
                hs.update("13sda23".encode())
                hsvar = hs.hexdigest()
                print(username)
                sql = "update user set pwd=\'" + hsvar+ "\' where name = \'" + username +"\';"
                flag = mysql.update(sql)
                return redirect(url_for('login'))
        else:
            return render_template('forget.html')


# 关于画k线图的函数
@app.route('/k_line_echart', methods=['POST','GET'])
def k_line_echart():
    if request.method =="GET":
        return render_template('data.html')
    if request.method =="POST":
        symbol = str(request.form.get("symbol_opt"))
        print(symbol)
        # 连接数据库
        conn = pymysql.connect(host='localhost',user='root',password='123456',database='encryption_currency')
        cur = conn.cursor()
        # sql语句
        sql = "SELECT Symbol,date,open,close,high,low from coin where symbol = '%s'" % symbol
        print(sql)
        try:
            cur.execute(sql)
            all_data = cur.fetchall()
            data_lists =[]
            for data in all_data:
                symbol = data[0]
                date = data[1].strftime("%Y/%m/%d")
                open = data[2]
                close = data[3]
                high = data[4]
                low = data[5]
                data_list =[date,open,close,low,high]
                data_lists.append(data_list)
            # 将列表转化为json
            keys =[]
            for i in range(len(data_lists)):
                keys.append(str(i))
            json_data = dict(zip(keys,data_lists))
       
            return json_data
        except:
            print("k-line-echart的sql执行错误")
            return render_template('data.html')
# 动态从数据库中 选取币种 没有写死 暂时没有用到该函数
@app.route('/echart1', methods=['POST','GET'])        
def select_symbol():
    if request.method =="GET":
        return render_template('data.html')
    if request.method =="POST":  
        
        conn = pymysql.connect(host='localhost',user='root',password='123456',database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT Symbol from coin" 
        cur.execute(sql)
        u = cur.fetchall()
        symbol_set = set()
        # 为了转化为json
        keys = []
        i = 0
        for data in u:
            symbol_set.add(data[-1])
            i = i + 1
            keys.append(str(i))
        # print(s)
        # set 转化为 list
        symbol_list = list(symbol_set)
        # print(keys)
        json_data = dict(zip(keys,symbol_list))
        # print(json_data)
        print("haha")
        return json_data

@app.route('/rank', methods=['POST','GET'])
def rank():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == 'POST':
        conn = pymysql.connect(host='localhost',user='root',password='123456',database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT name from avg_volume_marketcap" 
        main_coin_five =[]
        key_main = []
        key_main_i = 0
        not_main_coin_five =[]
        # cur.execute(sql)
        try:
            cur.execute(sql)
            # while(u!=None):
            #     u = cur.fetchone()
            #     if(u in mainstream_currency):
            #         main_coin_five.append(u)
            #         key_main_i = key_main_i + 1
            #         key_main.append(str(key_main_i))
            #     else:
            #         not_main_coin_five.append(u)
            #         key_main_i

            u = cur.fetchall()
            i = 0
            for data in u:
                main_coin_five.append(data)
                i=i+1
                key_main.append(str(i))

            print("main",main_coin_five)
            json_data = dict(zip(key_main,main_coin_five))
            # print("not_mian",not_main_coin_five)
            return json_data
            # return render_template('data.html')
        except:
            print("排行榜出错!!")
            return render_template('data.html')

if __name__ == '__main__':
    app.run(debug="True")