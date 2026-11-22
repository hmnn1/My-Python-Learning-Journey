# 导入 numpy 和pandas 库, 约定俗成别名为 np和pd
import numpy as np
import pandas as pd
from scipy.stats import pearsonr    

raw_data = pd.read_csv("data.csv")
print(raw_data)

#计算皮尔逊相关
age = raw_data['Age']
weight = raw_data['Weight']
age_weight_corr = np.corrcoef(age, weight)
print(age_weight_corr)
print(pearsonr(age, weight))




