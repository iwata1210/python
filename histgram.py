import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd

record = pd.read_csv("seiseki.csv")
subject = record["kokugo"]

# ヒストグラム
frequency, cls ,_=plt.hist(subject)

# 度数
print(frequency)
# 階級(中央地)
print(cls)
# 相対度数
frequency = frequency / frequency.sum()
print(frequency)

plt.show()