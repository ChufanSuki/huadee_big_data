from os import name
from flask import Flask,render_template,redirect,request,url_for
import pymysql


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

@app.route('/show',methods = ['GET','POST'])
def show():
    if request.method == 'POST':
        return redirect(url_for('/index'))
    return render_template("data.html")


if __name__ == '__main__':
    app.run()