import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd

rg1 = st.norm(160, 5)
rg2 = st.norm(160, 10)

# 度数分布
data1 = rg1.rvs(10000)
data2 = rg2.rvs(10000)

# 確率密度分布
kde1 = st.gaussian_kde(data1)
kde2 = st.gaussian_kde(data2)
plot_x = np.linspace(130, 200, 100)
density1 = kde1(plot_x)
density2 = kde2(plot_x)

plt.fill(plot_x, density1, alpha=0.5, label="class1")
plt.fill(plot_x, density2, alpha=0.5, label="class2")

plt.show()

# 図の数を指定
_, axes =plt.subplots(nrows=2)

# normed=TRUE 確率密度分布
axes[0].hist(data1, 20,range=(130,200), normed=True)
axes[0].plot(plot_x, density1)
axes[1].hist(data2, 20,range=(130,200), normed=True)
axes[1].plot(plot_x, density2)

plt.show()

