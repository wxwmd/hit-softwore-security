import pandas as pd
from kd_tree import distance
from kd_tree import KNNKdTree


def str2float(s: str) -> float:
    """
    将字符串处理成float，便于建立KD树
    :param s: 要处理的字符串
    :return: 该字符串对应的浮点数
    """
    sum1 = 0.
    for ch in s:
        sum1 += ord(ch)
    return sum1 / 255


def transfrom_df(df: pd.DataFrame):
    """
    将dataframe中包含的字符串处理成浮点数
    :param df: 要处理的dataframe
    :return: None
    """
    df['attribute1'] = df['attribute1'].apply(str2float)
    df['attribute2'] = df['attribute2'].apply(str2float)
    df['attribute3'] = df['attribute3'].apply(str2float)


columns = ['attribute' + str(i) for i in range(41)]
columns.append('property')
data_df = pd.read_csv('./dataset/train.csv', header=None, names=columns)
transfrom_df(data_df)
data_train = data_df.values
data_train = data_train[:, 0:41]

# tree = KDTree(data_train)

# 测试KD-Tree的准确率
threshold = 110

data_test_df = pd.read_csv('./dataset/test.csv', header=None, names=columns)
transfrom_df(data_test_df)
data_test = data_test_df.values
x_test = data_test[:, 0:41]
y_test = data_test[:, 41]

kdtree = KNNKdTree()
kdtree.fit(data_train, [1] * len(data_train))

correct_num = 0
wubao_num=0
loubao_num=0
for i in range(len(x_test)):
    nearest = kdtree.predict(x_test[i])[0][0].data
    d = distance(nearest, x_test[i])
    print(d)
    if (d > 100 and y_test[i] != 'normal.') or (d <= 100 and y_test[i] == 'normal.'):
        correct_num += 1
    elif d < 100 and y_test[i] == 'smurf.':
        loubao_num+=1
    else:
        wubao_num+=1

print('分类的正确率是：', round(100*correct_num / len(y_test),2),'%')
print('误报率是：', round(100*wubao_num / len(y_test),2),'%')
print('漏报率是：', round(100*loubao_num / len(y_test),2),'%')
