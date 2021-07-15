from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()
df=spark.read.format("jdbc")\
    .option("url", "jdbc:mysql://localhost:3306/flask") \
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "coin")\
    .option("user", "root")\
    .option("password", "20010501come").load()


print("--------------------1.100种货币当日价格----------------------")
df1=df.select('name','date','open','high','low','close').filter(df['date']=='2021-07-11 00:00:00')
df1=df1.sort(df1.open.desc())  #按开盘价从高到底排序
df1.show()  #默认显示前20名
#df1.show(n=df1.count())  #100种货币全部显示


print("--------------------2.100种货币近一天内涨跌幅----------------------")
df2_new=df.select('name','close').filter(df['date']=='2021-07-11 00:00:00').withColumnRenamed("close","close_new") #今日收盘价
df2_old=df.select('name','close').filter(df['date']=='2021-07-10 00:00:00').withColumnRenamed("name","name2").withColumnRenamed("close","close_old")  #昨日收盘价
df2=df2_old.join(df2_new,df2_old.name2==df2_new.name,'inner')  #两表合并

rise_or_fall=(df2.close_new-df2.close_old)/df2.close_old*100  #计算涨跌幅
df2=df2.withColumn('one_day_%',F.lit(rise_or_fall)).withColumn('one_day_%',F.bround('one_day_%',scale=2))  #把涨跌幅加入表
df2=df2.select('name','close_old','close_new','one_day_%')\
    .withColumnRenamed("close_new","close_today").withColumnRenamed("close_old","close_one_day_ago") #选取展示属性，避免拼接后处理麻烦，把有相同字段的属性重命名
df2=df2.sort('one_day_%',ascending=False)  #按涨跌幅从高到底排序，ascending=False为降序，ascending=True为升序
df2.show()  #默认显示前20名


print("--------------------3.100种货币近7天内涨跌幅----------------------")
df3_new=df.select('name','close').filter(df['date']=='2021-07-11 00:00:00').withColumnRenamed("close","close_new") #今日收盘价
df3_old=df.select('name','close').filter(df['date']=='2021-07-04 00:00:00').withColumnRenamed("name","name2").withColumnRenamed("close","close_old")  #昨日收盘价
df3=df3_old.join(df3_new,df3_old.name2==df3_new.name,'inner')  #两表合并

rise_or_fall=(df3.close_new-df3.close_old)/df3.close_old*100  #计算涨跌幅
df3=df3.withColumn('one_week_%',F.lit(rise_or_fall)).withColumn('one_week_%',F.bround('one_week_%',scale=2))  #把涨跌幅加入表
df3=df3.select('name','close_old','close_new','one_week_%')\
    .withColumnRenamed("name","name3").withColumnRenamed("close_old","close_one_week_ago") #选取展示属性，避免拼接后处理麻烦，把有相同字段的属性重命名
df3=df3.sort('one_week_%',ascending=False)  #按涨跌幅从高到底排序，ascending=False为降序，ascending=True为升序
df3.show()  #默认显示前20名


print("--------------------4.100种货币近一个月内涨跌幅----------------------")
df4_new=df.select('name','close').filter(df['date']=='2021-07-11 00:00:00').withColumnRenamed("close","close_new") #今日收盘价
df4_old=df.select('name','close').filter(df['date']=='2021-06-11 00:00:00').withColumnRenamed("name","name2").withColumnRenamed("close","close_old")  #昨日收盘价
df4=df4_old.join(df4_new,df4_old.name2==df4_new.name,'inner')  #两表合并

rise_or_fall=(df4.close_new-df4.close_old)/df4.close_old*100  #计算涨跌幅
df4=df4.withColumn('one_month_%',F.lit(rise_or_fall)).withColumn('one_month_%',F.bround('one_month_%',scale=2))  #把涨跌幅加入表
df4=df4.select('name','close_old','close_new','one_month_%')\
    .withColumnRenamed("name","name4").withColumnRenamed("close_old","close_one_month_ago") #选取展示属性，避免拼接后处理麻烦，把有相同字段的属性重命名
df4=df4.sort('one_month_%',ascending=False)  #按涨跌幅从高到底排序，ascending=False为降序，ascending=True为升序
df4.show()  #默认显示前20名


print("--------------------5.把三个时段的涨跌幅（df2,df3,df4）拼接在一起（按今日涨跌幅降序排名）----------------------")
df5=df2.join(df3,df2.name==df3.name3,'inner').join(df4,df2.name==df4.name4,'inner')  #三表合并
df5=df5.select('name','close_today','close_one_day_ago','one_day_%','close_one_week_ago','one_week_%','close_one_month_ago','one_month_%')  #选取展示属性
df5=df5.sort('one_day_%',ascending=False)  #按涨跌幅从高到底排序，ascending=False为降序，ascending=True为升序
# print(df5.count()) #输出表行数
df5.show()


print("--------------------6.把100种货币当日价格导出为csv文件（按开盘价从高到低排序）----------------------")
print("--------------------包含当天开盘价、最高价、最低价、收盘价----------------------")
#注：为了保证排序按照降序的准确性，可以先把dataframe表导出为csv文件，再把csv文件导入数据库
df1.toPandas().to_csv('D:/Dataset/sparksql/coin_price.csv',header=True,index=False)
#先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成csv，不为行建立索引
print("哈哈哈哈哈，导出为csv文件成功了！！！")


print("--------------------7.把涨跌幅导出为csv文件（按当天涨跌幅从高到低排序）----------------------")
print("--------------------包含当天，近七天，近一个月的涨跌幅和四个时间点的收盘价----------------------")
#注：为了保证排序按照降序的准确性，可以先把dataframe表导出为csv文件，再把csv文件导入数据库
df5.toPandas().to_csv('D:/Dataset/sparksql/coin_rise_fall.csv',header=True,index=False)
#先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成csv，不为行建立索引
print("哈哈哈哈哈，导出为csv文件成功了！！！")
