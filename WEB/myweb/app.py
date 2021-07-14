from os import name
from flask import Flask,render_template,redirect,request,url_for
import pymysql
import mysql
# from flask_login import LoginManager

app = Flask(__name__)
app.debug = True

def conn():
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="encryption_currency",
        charset="utf8mb4",
    )
    return con
    # soup = bs(re)

def query(con):
    cur = con.cursor()
    sql = """
    select * from coin limit 0,10
    """
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    return result

@app.route('/index')
def index():
    infos = []
    con = conn()
    data = query(con)
    for item in data:
        print(item)
    return render_template("index.html")
    # return render_template("register.html")

@app.route('/login1',methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('index.html')
    user = request.form.get('username')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == '123':
        # session['user_info'] = user
        return redirect('/show')
    else:
        return render_template('index.html')


@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('/login1'))
    return render_template("register.html")

@app.route('/show',methods = ['GET','POST'])
def show():
    if request.method == 'POST':
        return redirect(url_for('/index'))
    return render_template("data.html")


if __name__ == '__main__':
    app.run()