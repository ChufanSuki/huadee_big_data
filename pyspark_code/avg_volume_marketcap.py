from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()
df=spark.read.format("jdbc")\
    .option("url", "jdbc:mysql://localhost:3306/flask") \
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "coin")\
    .option("user", "root")\
    .option("password", "20010501come").load()


print("--------------------1.今日交易额、市值（按市值降序排名）----------------------")
df1=df.select('name','symbol','date','volume','market_cap').filter(df['date']=='2021-07-11 00:00:00')
df1=df1.withColumnRenamed("volume","volume_today").withColumnRenamed("market_cap","market_cap_today")  #修改列名为今天的交易额、市值
#df1=df1.sort(df1.market_cap_today.desc())  #按市值降序排名
df1.show()  #默认显示前20名
#df1.show(n=df1.count())  #100种货币全部显示


print("--------------------2.近7天每日平均交易额、平均市值（按市值降序排名）----------------------")
df2=df.select('name','volume','market_cap').filter((df['date']<='2021-07-11 00:00:00')&(df['date']>='2021-07-05 00:00:00'))
df2=df2.groupby('name').avg('volume','market_cap').withColumnRenamed("avg(volume)","avg_volume_week")\
    .withColumnRenamed("avg(market_cap)","avg_market_cap_week").withColumnRenamed("name","name2")
    #计算平均值并重命名列，避免拼接后处理麻烦，把有相同字段的属性重命名
df2=df2.withColumn('avg_volume_week',F.bround('avg_volume_week',scale=0))  #改为整数值
df2=df2.withColumn('avg_market_cap_week',F.bround('avg_market_cap_week',scale=0))  #改为整数值
#df2=df2.sort(df2.avg_market_cap_week.desc())  #按市值降序排名
df2.show()


print("--------------------3.近一个月每日平均交易额、平均市值（按市值降序排名）----------------------")
df3=df.select('name','volume','market_cap').filter((df['date']<='2021-07-11 00:00:00')&(df['date']>='2021-06-12 00:00:00'))  #选取时间和属性
df3=df3.groupby('name').avg('volume','market_cap').withColumnRenamed("avg(volume)","avg_volume_month")\
    .withColumnRenamed("avg(market_cap)","avg_market_cap_month").withColumnRenamed("name","name3")
    #计算平均值并重命名列，避免拼接后处理麻烦，把有相同字段的属性重命名
df3=df3.withColumn('avg_volume_month',F.bround('avg_volume_month',scale=0))  #改为整数值
df3=df3.withColumn('avg_market_cap_month',F.bround('avg_market_cap_month',scale=0))  #改为整数值
#df3=df3.sort(df3.avg_market_cap_month.desc())  #按市值降序排名
df3.show()


print("--------------------4.把以上三张表拼接在一起（按今日市值降序排名）----------------------")
df4=df1.join(df2,df1.name==df2.name2,'inner').join(df3,df1.name==df3.name3,'inner')  #三表合并
df4=df4.drop('name2').drop('name3')  #删除重复列
df4=df4.sort(df4.market_cap_today.desc())  #按今日市值降序排名
#print(df4.count()) #输出表行数
df4.show()


# print("--------------------5.把拼接好的表df4写入数据库（按今日市值降序排名）----------------------")
# #注：直接导入数据库会导致排序有些问题，但大体是从高到低，问题的出现可能是因为每条记录写入时间有差别
# df4.write.jdbc('jdbc:mysql://localhost:3306/flask?useSSL=false',
# 	'avg_volume_marketcap',
# 	mode='overwrite',
# 	properties={"user": "root", "password": "20010501come"})
# print("哈哈哈哈哈，导入数据库成功了！！！")


print("--------------------6.把拼接好的表df4导出为csv文件（按今日市值降序排名）----------------------")
print("--------------------包含当天、近七天、近一个月每日的平均交易额和平均市值----------------------")
#注：为了保证排序按照降序的准确性，可以先把dataframe表导出为csv文件，再把csv文件导入数据库
df4.toPandas().to_csv('D:/Dataset/sparksql/avg_volume_marketcap.csv',header=True,index=False)
#先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成csv，不为行建立索引
print("哈哈哈哈哈，导出为csv文件成功了！！！")
