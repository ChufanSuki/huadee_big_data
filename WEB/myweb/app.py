import datetime
import functools
from os import name
import re
from flask import Flask,render_template,redirect,request,url_for,flash,jsonify,session
from flask.helpers import flash
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
import config
from urllib.parse import urlparse, urljoin
import mysql_connector
# from . import mysql_connector
import pymysql
import random
from flask_mail import Mail, Message
import hashlib
# from .forms import LoginForm
from forms import LoginForm

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
login_manager.login_view = '/login1'

mainstream_currency = ['BTC', 'ETH', 'USDT', 'XRP', 'BCH', 'LTC', 'BNB', 'LINK', 'DOT', 'ADA']


def float_to_str(price):
    if (price > 100000000):
        price = price / 100000000
        return str(price) + '亿'
    elif (price > 10000):
        price = price / 10000
        return str(price) + '万'
    else:
        return str(price)


def float_formatter(f):
    if (f > 10000):
        return format(f, '.0f')
    elif (f > 1000):
        return format(f, '.1f')
    elif (f > 100):
        return format(f, '.2f')
    elif (f > 10):
        return format(f, ".3f")
    else:
        return format(f, '.4f')


class User(UserMixin):
    pass


# 获取当前系统时间 年-月-日 时:分:秒
def getDateTime():
    now = datetime.datetime.now()
    now_funmat = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_funmat


# 绑定默认错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 绑定默认错误页面
@app.errorhandler(500)
def page_server_error(e):
    return render_template('login.html'), 500


# 构造一个用户类对象,并使用用户名作为ID
# 回调函数
@login_manager.user_loader
def load_user(username):
    curr_user = User()
    curr_user.id = username
    return curr_user


# 装饰器，判断是否为管理员
def is_admin(f):
    @functools.wraps(f)
    def decorated_function(*args, **kws):
        # 需要在登录状态调用, 检查是否为有admin权限的用户登录，
        # 如果不是，返回错误码；
        adminname = session['_user_id']
        sql = "select name from admin where name=\'" + adminname + "\';"
        user1 = mysql_connector.query(sql)
        if len(user1) == 0:
            return render_template('404.html')
        return f(*args, **kws)

    return decorated_function


# 加密函数
def encryption(pwd):
    # 加密
    hs = hashlib.sha1()
    data = str(pwd)
    hs.update(data.encode())
    # 加盐
    hs.update("13sda23".encode())
    hsvar = hs.hexdigest()
    return hsvar


# 登录功能
@app.route('/login1',methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    # 加密
    hsvar = encryption(pwd)
    sql = "select name from user where name=\'"+username+"\' and pwd=\'"+hsvar+"\';"
    user1 = mysql_connector.query(sql)
    if len(user1) != 0:
        username = user1[-1][-1]
        curr_user = User()
        curr_user.id = username
        login_user(curr_user)
        return redirect(url_for('index'))
    else:
        flash("账号或密码错误！")
        return render_template('login.html')


# 大数据面板
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        return redirect(url_for('/index'))
    return render_template("data.html")
    # return render_template("index.html")


# 登出
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# 功能：检查字符串str是否符合正则表达式re_exp
# re_exp:正则表达式
# str:待检查的字符串
def check_string(str):
    re_exp = '^[A-Za-z0-9]+$'
    res = re.match(re_exp, str)
    if res:
        return True
    else:
        return False

# 判断用户名
# 0:通过检查 1：用户名为空 2：位数不正确 3：格式不正确
def check_username(username):
    username = username.replace(" ","")
    username_len = len(username)
    zz = check_string(username)
    flag = 0
    if username_len == 0:
        flag = 1
    elif (username_len < 6) or (username_len > 14):
        flag = 2
    elif(zz == False):
        flag = 3
    return flag

# 判断密码
# 0:通过检查 1：密码不一致 2：密码存在空格 3:密码长度不在[6-14]
def check_pwd(pwd1,pwd2):
    pwd1_len = len(pwd1)
    pwd2_len = len(pwd2)
    pwd1 = pwd1.replace(" ","")
    pwd2 = pwd2.replace(" ","")
    pwd1_len_q = len(pwd1)
    pwd2_len_q = len(pwd2)
    flag = 0
    if pwd1 != pwd2:
        flag = 1
    elif (pwd1_len != pwd1_len_q) or (pwd2_len != pwd2_len_q) or (pwd1_len_q == 0) or (pwd2_len_q == 0):
        flag = 2
    elif (pwd1_len_q <6) or (pwd1_len_q >14):
        flag = 3
    return flag


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        code = request.form.get('valid')
        if str(session['code']).upper() == str(code).upper():
            username = request.form.get('username')
            username = username.replace(" ","")
            pwd1 = request.form.get('pwd1')
            pwd2 = request.form.get('pwd2')
            email = request.form.get('email')
            sql = "select name from user where name=\'" + username + "\';"
            user1 = mysql_connector.query(sql)
            checkname = check_username(username)
            checkpwd = check_pwd(pwd1,pwd2)
            if  checkname == 1:
                flash("用户名不能为空！")
                return render_template('register.html')
            elif checkname == 2:
                flash("用户名位数错误！")
                return render_template('register.html')
            elif checkname == 3:
                flash("用户名格式错误！")
                return render_template('register.html')
            elif len(user1) != 0:
                flash("用户名已存在！")
                return render_template('register.html')
            elif checkpwd == 1:
                flash('两次密码不一致！')
                return render_template('register.html')
            elif checkpwd == 2:
                flash('密码为空或存在空格！')
                return render_template('register.html')
            elif checkpwd == 3:
                flash('密码长度不符合！')
                return render_template('register.html')
            else:
                # 加密
                regdate = getDateTime()
                hsvar = encryption(pwd1)
                sql = "insert into user value(\'" + username + "\',\'" + hsvar + "\',\'" + email + "\',\' " + regdate + "\');"
                flag = mysql_connector.insert(sql)
                return redirect(url_for('login'))
        else:
            return render_template('register.html')



# 验证用户名是否可以使用(用户名未注册且格式正确)
@app.route('/validateUniqueName',methods = ['GET','POST'])
def validateUniqueName():
    res = {'data': ''}
    if request.method == 'GET':
        return render_template('register.html')
    username = request.form.get('username')
    username = username.replace(" ","")
    sql = "select name from user where name=\'"+username+"\';"
    user1 = mysql_connector.query(sql)
    # 用户名判断
    check = check_username(username)
    flag = "True"
    # 是否存在判断
    if len(user1) != 0:
        flag = "False"
    elif check != 0:
        flag = "Error"
    res['data'] = flag
    return jsonify(res)


# 邮箱验证码
# 随机数函数
def random_str():
    _str = '1234567890abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(_str) for i in range(4))


# 发送邮件
@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    res = {'data': ''}
    if request.method == 'POST':
        return render_template('register.html')
    elif request.method == 'GET':
        msg = ""
        email = request.args.get('email')
        email_code = random_str()
        msg = Message('数字货币大数据分析平台注册', recipients=[email], body="您的验证码是:%s" % email_code)
        mail.send(msg)  # 发送
        res['data'] = str(email_code)
        session['code'] = email_code
        return jsonify(res)
    else:
        res['data'] = "error"
        return jsonify(res)


# 重置密码发送邮件
@app.route('/send_email_forget', methods=['GET', 'POST'])
def send_email_forget():
    res = {'data': '', 'email': ''}
    if request.method == 'POST':
        return render_template('forget.html')
    elif request.method == 'GET':
        username = request.args.get('username')
        email_code = random_str()
        sql = "select email from user where name=\'" + username + "\';"
        user1 = mysql_connector.query(sql)
        email = user1[-1][-1]
        msg = ""
        msg = Message('数字货币大数据分析平台重置密码', recipients=[email], body="您的验证码是:%s" % email_code)
        mail.send(msg)  # 发送
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
@app.route('/checkCode', methods=['GET', 'POST'])
def checkCode():
    res = {'data': ''}
    if request.method == 'GET':
        return render_template('register.html')
    email = request.form.get('email')
    res['data'] = session['code']
    return jsonify(res)


# 忘记密码
@app.route('/forget', methods=['GET', 'POST'])
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
            sql = "select name from user where name=\'" + username + "\';"
            user1 = mysql_connector.query(sql)
            checkpwd = check_pwd(pwd1,pwd2)
            if username == "":
                flash("用户名不能为空！")
                return render_template('forget.html')
            elif len(user1) == 0:
                flash("用户名不存在！")
                return render_template('forget.html')
            elif checkpwd == 1:
                flash('两次密码不一致！')
                return render_template('forget.html')
            elif checkpwd == 2:
                flash('密码为空或存在空格！')
                return render_template('register.html')
            elif checkpwd == 3:
                flash('密码长度不符合！')
                return render_template('register.html')
            else:
                # 加密
                hsvar = encryption(pwd1)
                sql = "update user set pwd=\'" + hsvar + "\' where name = \'" + username + "\';"
                flag = mysql_connector.update(sql)
                return redirect(url_for('login'))
        else:
            return render_template('forget.html')


# 后台管理-数字货币数据
@app.route('/admin', methods=['GET', 'POST'])
@login_required
@is_admin
def admin():
    print([session['_user_id']])
    if request.method == "GET":
        sql = "select * from coin limit 0,200;"
        content = mysql_connector.query(sql)
        sql = "SHOW FIELDS FROM coin"
        lables = mysql_connector.query(sql)
        lables = [l[0] for l in lables]
        return render_template('admin.html', content=lables, content2=content)
    elif request.method == "POST":
        res = {'data': ''}
        symbol = request.form.get('select')
        sql = "select * from coin where symbol = \'" + symbol + "\';"
        content = mysql_connector.query(sql)
        sql = "SHOW FIELDS FROM coin"
        lables = mysql_connector.query(sql)
        lables = [l[0] for l in lables]
        res['data'] = 'True'
        # print(content)
        return render_template('admin.html', content=lables, content2=content)
    else:
        return render_template('admin.html')


# 后台管理-用户
@app.route('/adminUser', methods=['GET', 'POST'])
@login_required
@is_admin
def adminUser():
    if request.method == "GET":
        sql = "select * from user;"
        content = mysql_connector.query(sql)
        sql = "SHOW FIELDS FROM user"
        lables = mysql_connector.query(sql)
        lables = [l[0] for l in lables]
        return render_template('admin_user.html', content=lables, content2=content)


# 后台管理-管理员
@app.route('/adminAdmin', methods=['GET', 'POST'])
@login_required
@is_admin
def adminAdmin():
    if request.method == "GET":
        sql = "select * from admin;"
        content = mysql_connector.query(sql)
        sql = "SHOW FIELDS FROM admin"
        lables = mysql_connector.query(sql)
        lables = [l[0] for l in lables]
        return render_template('admin_admin.html', content=lables, content2=content)


# 404返回
@app.route('/error_page', methods=['GET', 'POST'])
@login_required
def error_page():
    if request.method == "GET":
        print("#########################")
        print(session['_user_id'])
        print("#########################")
        return redirect(url_for('index'))


# 关于画k线图的函数,上方是两个圆圈
@app.route('/k_line_echart', methods=['POST','GET'])
def k_line_echart():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == "POST":
        symbol = str(request.form.get("symbol_opt"))
        # 默认值设置为BTC，便于一开始的页面展示
        if (symbol == 'None'):
            symbol = 'BTC'
        print(symbol)
        # 连接数据库
        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
        cur = conn.cursor()
        # sql语句
        sql = "SELECT Symbol,date,open,close,high,low from coin where symbol = '%s'" % symbol
        # 上方两个圆形的数据sql
        sql2 = "SELECT * from coin_rise_fall where symbol='%s'" % symbol
        cur.execute(sql2)
        print(sql2)
        try:
            # 处理得到第一个k线图的数据
            cur.execute(sql)
            all_data = cur.fetchall()
            data_lists = []
            for data in all_data:
                symbol = data[0]
                date = data[1].strftime("%Y/%m/%d")
                open = data[2]
                close = data[3]
                high = data[4]
                low = data[5]
                data_list = [date, open, close, low, high]
                data_lists.append(data_list)
            keys = []
            for i in range(len(data_lists)):
                keys.append(str(i))
            json_data1 = dict(zip(keys, data_lists))
            # print(json_data1)
            #处理得到两个圆圈的图的数据
            cur.execute(sql2)
            all_data2 = cur.fetchall()
            data_list2 = []
            for data2 in all_data2:
                close_taday = float_formatter(data2[2])
                rise_down = data2[4]
                # sym = data[1]
                # print(sym)
                data_list2.append([close_taday, rise_down])
            keys2 = ['0']
            json_data2 = dict(zip(keys2,data_list2))
            # print(json_data2)

            json_data = {'1':json_data1,'2':json_data2}
            # print(json_data1)

            # 将列表转化为json

            return json_data
        except:
            print("k-line-echart的sql执行错误")
            return render_template('data.html')
# 预测
@app.route('/predict',methods=['POST','GET'])
def predict_echart():
    if request.method =="GET":
        return render_template('data.html')
    if request.method =="POST":  
        conn = pymysql.connect(host='localhost',user='root',password='123456',database='encryption_currency')
        cur = conn.cursor()
        symbol = str(request.form.get("symbol"))
        print("haaaaaaaaaa",symbol)
        # 默认值设置为BTC，便于一开始的页面展示
        if(symbol == 'None'):
            symbol = 'BTC'
        sql = "SELECT date,open,close,high,low from coin_predict where symbol='%s'" % symbol 
        cur.execute(sql)
        u = cur.fetchall()
        data_list = []
        key_list = []
        i = 0
        for data in u:
            date = data[0].strftime("%Y/%m/%d")
            open = data[1]
            close = data[2]
            high = data[3]
            low = data[4]
            data_list.append([date,open,close,high,low])
            i = i + 1 
            key_list.append(str(i))
        json_data = dict(zip(key_list,data_list))
        print(json_data)

        return json_data

# 动态从数据库中 选取币种 没有写死 暂时没有用到该函数
@app.route('/echart1', methods=['POST', 'GET'])
def select_symbol():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == "POST":

        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
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
        json_data = dict(zip(keys, symbol_list))
        # print(json_data)
        print("haha")
        return json_data


# 左侧动态栏
@app.route('/rank_left', methods=['POST', 'GET'])
def rank_left():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == 'POST':
        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT symbol,open,market_cap from coin_price"
        sql_res = []
        keys = []
        try:
            cur.execute(sql)
            u = cur.fetchall()
            i = 0
            for data in u:
                symbol = data[0]
                open = str(data[1])
                market_cap_today = float_to_str(data[2])
                data_list = [symbol, open, market_cap_today]
                sql_res.append(data_list)
                i = i + 1
                keys.append(str(i))

            # print("data:",sql_res)
            json_data = dict(zip(keys, sql_res))
            cur.close()
            conn.close()
            return json_data
        except:
            print("左侧排行榜sql执行出错!!")
            return render_template('data.html')


# 左下角玫瑰图
@app.route('/rose_echart', methods=['POST', 'GET'])
def rose_echart():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == "POST":

        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT symbol,percentage from marketcap_percentage limit 0,5"
        try:
            cur.execute(sql)
            u = cur.fetchall()
            print(u)
            xdatalist = []
            ydatalist = []

            i = 1
            for data in u:
                xdatalist.append(data[0])
                ydatalist.append(data[1])
                i = i - data[1]

            xdatalist.append('other')
            ydatalist.append(i)

            json_data = {'0': xdatalist, '1': ydatalist}
            print(json_data)

            return json_data
        except:
            print("ERROR")
            return render_template('data.html')


@app.route('/rank_right', methods=['POST', 'GET'])
def rank_right():
    if request.method == "GET":
        return render_template('data.html')
    if request.method == 'POST':
        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT symbol,market_cap_today,volume_today from avg_volume_marketcap"

        main_coin_five = []
        key_main = []
        key_main_i = 0
        key_not_main = []
        key_not_main_i = 0
        not_main_coin_five = []
        cur.execute(sql)
        try:
            cur.execute(sql)
            u = cur.fetchall()
            for data in u:
                data_list = []
                symbol = data[0]
                market_cap_today = float_to_str(data[1])
                volume_today = float_to_str(data[2])
                data_list = [symbol, market_cap_today, volume_today]
                if (key_main_i < 5 and symbol in mainstream_currency):
                    main_coin_five.append(data_list)
                    key_main.append(str(key_main_i))
                    key_main_i = key_main_i + 1
                elif (key_not_main_i < 5 and symbol not in mainstream_currency):
                    not_main_coin_five.append(data_list)
                    key_not_main.append(str(key_not_main_i))
                    key_not_main_i = key_not_main_i + 1
                elif (key_main_i == 5 and key_not_main_i == 5):
                    break

            # print("main",main_coin_five)
            # print("not_mian",not_main_coin_five)
            json_data1 = dict(zip(key_main, main_coin_five))
            json_data2 = dict(zip(key_not_main, not_main_coin_five))

            return {'1': json_data1, '2': json_data2}
            # return render_template('data.html')
        except:
            print("右侧排行榜sql出错!!")
            return render_template('data.html')


# 涨跌幅
@app.route('/chart1_json', methods=['POST', 'GET'])
def getChart1():
    if request.method == 'GET':
        return render_template('data.html')
    if request.method == 'POST':
        # item_name = []
        # item_data = []
        try:
            con = mysql_connector.conn()
            cur = con.cursor()
            sql = """
            select * from coin_rise_fall
            """
            cur.execute(sql)
            data = cur.fetchall()
            datalists = []
            item_name = []
            item_data = []
            for item in data:
                item_name.append(item[0])
                item_data.append(item[6])
            datalists.append(item_name)
            datalists.append(item_data)
            keys = ['1', '2']
            json_data = dict(zip(keys, datalists))
            # print(type(json_data))
            return json_data
        except:
            print("出错啦")
            return render_template('data.html')

@app.route('/echart_hot',methods =['POST','GET'])
def echart_hot():
    if request.method =='GET':
        return render_template('data.html')
    if request.method =='POST':
        conn = pymysql.connect(host='localhost', user='root', password='123456', database='encryption_currency')
        cur = conn.cursor()
        sql = "SELECT * from correlation"
        try:
            cur.execute(sql)
            u = cur.fetchall()
            symbol_list = []
            result_list = []
            for data in u:
                symbol = data[0]
                symbol_list.append(symbol)
                print(data)
            
            i = -1
            for data in u:
                i = i + 1
                for j in range(0,len(symbol_list)): 
                     
                    result_list.append([symbol_list[i],symbol_list[j],data[j+1]])
        
            print('result_list:')
            print(result_list)
            return {'lable':symbol_list,'data':result_list}
            # return render_template('data.html')
        except:
            print('热力图出错')
            return render_template('data.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
