# 导入mysql驱动
import pymysql


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


# 查询传入sql语句，返回result结果
def query(sql):
    con = conn()
    cursor = con.cursor()
    # noinspection PyBroadException
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise e
    finally:
        cursor.close()
        con.close()


# 新增数据库信息，新增前需要确保可以新增成功
def insert(sql):
    con = conn()
    cursor = con.cursor()
    # noinspection PyBroadException
    try:
        cursor.execute(sql)
        con.commit()
        return True
    except Exception as e:
        raise e
    finally:
        cursor.close()
        con.close()
