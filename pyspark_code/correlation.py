from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from heatmap import heatmap, corrplot


# spark = SparkSession.builder.getOrCreate()
# df=spark.read.format("jdbc")\
#     .option("url", "jdbc:mysql://localhost:3306/flask") \
#     .option("driver", "com.mysql.jdbc.Driver")\
#     .option("dbtable", "coin")\
#     .option("user", "root")\
#     .option("password", "20010501come").load()
#
# print("--------------------1.筛选出100种货币近2个月的闭盘价并导出----------------------")
# df1=df.select('name','symbol','date','close').filter((df['date']<='2021-07-11 00:00:00')&(df['date']>='2021-05-13 00:00:00'))
# print(df1.count())
# df1.show()
# df1.toPandas().to_excel('D:/Dataset/sparksql/corr_original_data.xlsx',header=True,index=False)
# #先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成excel，不为行建立索引
# print("哈哈哈哈哈，导出为excel文件成功了！！！")


# 在excel里将数据筛选出所需格式，并存入数据库corr_original_data.sql

# data=pd.read_excel(r'D:/Dataset/sparksql/corr_original_data.xlsx')

spark = SparkSession.builder.getOrCreate()
data=spark.read.format("jdbc")\
    .option("url", "jdbc:mysql://localhost:3306/flask") \
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "corr_original_data")\
    .option("user", "root")\
    .option("password", "20010501come").load()

data=data.toPandas()
data.drop(['date'], axis=1, inplace=True)  #删除无关的列
corr = data.corr()  #计算相关系数矩阵
print(data)
print(corr)

print("--------------------把相关系数导出为csv文件----------------------")
#注：为了保证排序按照降序的准确性，可以先把dataframe表导出为csv文件，再把csv文件导入数据库
corr.to_csv('D:/Dataset/sparksql/correlation.csv',header=True,index=True)
#先把pyspark.sql.dataframe格式转换成pandas.dataframe格式，再转化成csv，为行建立索引
print("哈哈哈哈哈，导出为csv文件成功了！！！")


# 第一种热力图
# plt.subplots(figsize=(9, 9))
# sns.heatmap(corr, annot=False, vmax=1, square=True, cmap="Blues")
# plt.show()
#
# 第二种热力图
# sns.set()
# ax = sns.heatmap(corr, cmap="rainbow")   # cmap是热力图颜色的参数
# plt.show()
#
# 第三种热力图
# plt.figure(figsize=(12, 12))
# corrplot(corr,size_scale=2000)
# plt.show()
