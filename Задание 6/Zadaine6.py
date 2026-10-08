import pandas as pd
import numpy as np
data = pd.read_csv('task4_720376 (1).csv', delimiter=',', decimal='.', index_col='ID')
data = 1 - np.exp(1 - data/data.min())
data['SUM'] = 0
data['SUM'] = data['DISTANCE'] + data['STOP_COUNT'] + data['COST']
data = data.sort_values(by = ['SUM'])
print(','.join(map(str, data.head(3).index)))
