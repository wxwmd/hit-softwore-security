import numpy as np
import pandas as pd

columns=['attribute'+str(i) for i in range(41)]
columns.append('property')
data=pd.read_csv('./dataset/kddcup.data_10_percent',delimiter=',',header=None,error_bad_lines=False,names=columns,low_memory=False)
data_normal=data.query('property=="normal."').values
data_exception=data.query('property=="smurf."').values

data_train=[]
data_test=[]

# 划分normal中的数据
for i in range(len(data_normal)):
    if np.random.rand() < 0.1:
        data_test.append(data_normal[i])
    else:
        data_train.append(data_normal[i])

# 选取2%的异常加入测试集
for i in range(len(data_exception)):
    if np.random.rand()<0.02:
        data_test.append(data_exception[i])

data_train=pd.DataFrame(data_train)
data_test=pd.DataFrame(data_test)
data_train.to_csv('./dataset/train.csv',header=False)
data_test.to_csv('./dataset/test.csv',header=False)