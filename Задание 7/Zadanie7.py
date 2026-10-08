import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_series = pd.read_csv('task5_983784.csv')
data_series.index += 1
def exponential_smothing(series, alpha):
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1 - alpha) * result[index - 1])
    return result
data_series['y_exp_norm_user'] = exponential_smothing(data_series['y'].to_list(), 0.2)
plt.figure(figsize=(20, 8))
plt.plot('y', data = data_series)
plt.plot('y_exp_norm_user', data = data_series)
plt.xlabel('Time step')
plt.ylabel('y')
# plt.show()
# data_series = data_series.loc[[50]]
# data_series = data_series['y_exp_norm_user'].loc[[50]]
data_series['y_exp_norm'] = data_series['y'].ewm(alpha = 0.2, adjust = False).mean()
# print(data_series)
plt.figure(figsize=(20, 8))
plt.plot('y', data = data_series)
plt.plot('y_exp_norm', data = data_series)
plt.plot('y_exp_norm_user', data = data_series)
plt.xlabel('Time step')
plt.ylabel('y')
#plt.show()
y50 = data_series['y_exp_norm_user'].loc[[50]]
data_series['y_exp_norm'] = data_series['y'].ewm(alpha= 0.2, adjust= False).mean()
plt.figure(figsize=(20, 8))
plt.plot('y', data = data_series)
plt.plot('y_exp_norm', data = data_series)
plt.plot('y_exp_norm_user', data = data_series)
plt.xlabel('Time step')
plt.ylabel('y')
#plt.show()
(data_series['y_exp_norm'] == data_series['y_exp_norm_user']).unique()
x = data_series.index.to_numpy()
y = data_series['y'].to_numpy()
poly = np.polyfit(x, y, 1)
a = round(poly[0], 2)
b = round(poly[1],2)
x = np.arange(1, 101)
data_series['lin_trend'] = a * x + b
plt.figure(figsize=(20, 8))
plt.plot('y', data=data_series)
plt.plot('lin_trend', data=data_series)
plt.xlabel('Time step')
plt.ylabel('y')
f_i = data_series['lin_trend']
y_avg = data_series['y'].mean()
R2 = 1 - ((y - f_i) ** 2).sum() / ((y - y_avg) ** 2).sum()
y_101 = a * 101 + b 
print(round(y_101, 0))