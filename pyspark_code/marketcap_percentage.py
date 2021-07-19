from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()
df=spark.read.format("jdbc")\
    .option("url", "jdbc:mysql://localhost:3306/flask") \
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "coin")\
    .option("user", "root")\
    .option("password", "20010501come").load()


print("--------------------1.今日市值及其占比（按市值降序排名）----------------------")
df1=df.select('name','symbol','date','market_cap').filter(df['date']=='2021-07-11 00:00:00')
# df_sum=df1.groupby('date').sum('market_cap')  #计算获得总市值为1375258721100
sum_market_cap=df1.toPandas().market_cap.sum()  #计算获得总市值
print(sum_market_cap)  #打印总市值
percentage=df1.market_cap/sum_market_cap  #计算百分比
df1=df1.withColumn('percentage',F.lit(percentage)).withColumn('percentage',F.bround('percentage',scale=4))  #把市值占比加入表
df1=df1.sort(df1.market_cap.desc())  #按市值降序排名
df1.show()  #默认显示前20名

df_top5=df1.limit(5)  #获取前五行数据
others5_market_cap=sum_market_cap-df_top5.toPandas().market_cap.sum()  #今日除去前五名的市值
others5_percentage=1-df_top5.toPandas().percentage.sum()  #今日除去前五名的百分比
print(others5_market_cap)
print(others5_percentage)

df_top6=df1.limit(6)  #获取前六行数据
others6_market_cap=sum_market_cap-df_top6.toPandas().market_cap.sum()  #今日除去前六名的市值
others6_percentage=1-df_top6.toPandas().percentage.sum()  #今日除去前六名的百分比
print(others6_market_cap)
print(others6_percentage)

df_top7=df1.limit(7)  #获取前七行数据
others7_market_cap=sum_market_cap-df_top7.toPandas().market_cap.sum()  #今日除去前七名的市值
others7_percentage=1-df_top7.toPandas().percentage.sum()  #今日除去前七名的百分比
print(others7_market_cap)
print(others7_percentage)


print("--------------------2.把100种货币今日市值及其占比导出为csv文件（按市值降序排名）----------------------")
print("--------------------包含当天开盘价、最高价、最低价、收盘价----------------------")
#注：为了保证排序按照降序的准确性，可以先把dataframe表导出为csv文件，再把csv文件导入数据库
df1.toPandas().to_csv('D:/Dataset/sparksql/marketcap_percentage.csv',header=True,index=False)
#先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成csv，不为行建立索引
print("哈哈哈哈哈，导出为csv文件成功了！！！")

