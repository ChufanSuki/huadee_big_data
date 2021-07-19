# 预测会趋于平均值
print("--------------------未来五天10种热门货币价格预测---------------------------")
# !/usr/bin/env python
# coding: utf-8

# 导入所需的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import datetime

#修改文件名
stockFile = 'D:/Dataset/sparksql/SOL.csv'

print("--------------------第一处修改---------------------------")
# 读取文件
df = pd.read_csv(stockFile, header=None, names=['ID','name','symbol','Date', 'Open', 'High', 'Low', 'Close'])

# 当前数据大小
dataLen = len(df)

# 训练用的数据大小
trainLen = len(df)  # 预测后20天的数据

# 用 n 天数据来训练和预测 n 天后一天的数据
nLen = 10

# 验证的数据大小
validLen = dataLen - trainLen

print("dataLen=%d validLen=%d nLen=%d" % (dataLen, validLen, nLen))

print("--------------------第二处修改---------------------------")
# 定义 DataFrame 来保存数据，只需要 Date 和 Close 两列数据
new_data = pd.DataFrame(index=range(0, dataLen), columns=['Date', 'Low'])

print("--------------------第三处修改---------------------------")
for i in range(0, dataLen):
    new_data['Date'][i] = df['Date'][i]
    new_data['Low'][i] = df['Low'][i]

# 设置日期作为索引
new_data.index = new_data.Date
# 把日期列删除掉
new_data.drop('Date', axis=1, inplace=True)

# 创建训练集和验证集
dataset = new_data.values
# print(dataset)

# 把数据转到 0-1 区间
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# 按每 nLen 天作为特征输入
x_train, y_train = [], []
for i in range(nLen, trainLen):
    x_train.append(scaled_data[i - nLen:i, 0])
    y_train.append(scaled_data[i, 0])

x_train = np.array(x_train)
y_train = np.array(y_train)

# 把 x_train 数组维数改变
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# print(x_train)

# 创建和拟合LSTM网络
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=200, batch_size=100, verbose=2)  #修改训练轮数

# 使用过去值来预测 validLen 个值
start = dataLen - validLen - nLen
print("dataLen=%d validLen=%d nLen=%d start=%d" % (dataLen, validLen, nLen, start))

inputs = new_data[start:start + nLen].values
print(len(inputs))

inputs = scaler.transform(inputs)

inputLen = inputs.shape[0]
print('inputLen=%d' % (inputLen))

inputData = []
for i in range(nLen, inputLen + 1):
    inputData.append(inputs[i - nLen:i, 0])

inputData = np.array(inputData)
print('type=%s shape[0]=%d shape[1]=%d  ' % (type(inputData), inputData.shape[0], inputData.shape[1]))
# print(inputData)

# 开始预测

# 定义预测的天数(此时数据的最后20天数据为验证值)
predictNum = 20
validLen = predictNum

preducts = []
for i in range(predictNum):
    x_test = np.reshape(inputData, (inputData.shape[0], inputData.shape[1], 1))
    #     print(x_test)

    predictVal = model.predict(x_test)
    preducts.append(predictVal[0])

    #     print('predictVal=%10.5f' % (predictVal) )

    # 去掉最前面的第一个数据
    inputData = inputData[:, 1:]

    # 把预测值加到最后面
    inputData = np.insert(inputData, [nLen - 1], predictVal, axis=1)
#     print(inputData)

# 恢复成标准数据
preducts = scaler.inverse_transform(preducts)
# print(len(preducts))
# print(preducts)

# 绘图
train = new_data[:trainLen]
valid = new_data[trainLen:trainLen + validLen]

# 避免警告
valid2 = valid.copy()
valid2['Predictions'] = np.reshape(preducts, -1)

print(valid2)

# # 设置图形大小
# rcParams['figure.figsize'] = 19, 10
#
# plt.plot(train['Close'], color='green')
#
# plt.plot(valid2[['Close']], color='blue')
# plt.plot(valid2[['Predictions']], color='red')
#
# plt.show()
