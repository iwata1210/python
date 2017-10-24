#ライブラリ

#Numpy関連
#NumPy 数値計算
#SciPy 価格計算
#Matplotlib グラフ作成
#Pandas 表計算
#Jupyter
#scikik-learn 機械学習

#その他
#SQLAlchemy 様々なDBとの接続
#PyMongo Nosql
#Cython c python
#Request http
#beautifulSoup HTMLのパーサー

# ライブラリの読み込み
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as sa

# 多次元配列 n dimesion array
x = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]],
    dtype=np.float)

# スカラー倍
x = x * 4
print(x)
# サイズ
print("サイズ: " , x.shape)
print("最大値: " , np.max(x))
print("列別最大値: " , np.max(x, axis=0))
print("行別最大値: " , np.max(x, axis=1))



# DataFrame ndarray + 複数の型を扱える

d = pd.DataFrame({
    "col1" : [1,2,3],
    "col2" : [1.0, -1.5, 2.5],
    "col3" : ["l1", "l2", "l3"]
})

print(d)
print("平均: ", d["col1"].mean())
print("標準偏差: ", d["col1"].std())

# 散布図
# データ読み込み
iris_data = pd.read_csv("iris.csv")

for name, type in zip(("setosa", "versicolor", "virginica"),("o","s","p")):
    data = iris_data[iris_data["species"] == name]
    plt.plot(data["petal_length"], data["petal_width"], type, label=name)
plt.xlabel("petal_length")
plt.ylabel("petal_width")
# ラベル名を表示
plt.legend(loc=0)
plt.show()

#棒グラフ
iris_data_mean = iris_data.mean()

print(iris_data_mean)
# rot ラベルの回転
iris_data_mean.plot(kind="bar", rot=5)
plt.show()

grouped_data = iris_data.groupby("species")
group_mean = grouped_data.mean()
group_mean.plot(kind="bar")
plt.show()

# DB
# 接続
engine = sa.create_engine("sqlite:///iris.db")
iris_data = pd.read_sql("SELECT * FROM iris WHERE species = '{0}'".format("virginica") , engine)
print(iris_data)

import scipy.stats as st
import matplotlib.pyplot as plt

# 期待値、標準偏差
rg = st.norm(160, 10)
# 件数指定
data = rg.rvs(40)