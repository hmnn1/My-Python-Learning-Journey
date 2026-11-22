import pandas as pd    
df = pd.read_excel('data.xlsx', sheet_name=1) 
print(df)
#head()返回DataFrame前几行（默认为5行）
print(df.head(10))   
print(df.head())   


import pandas as pd    
df = pd.read_excel('data.xlsx', sheet_name = 'Height') 
print(df.head())     

#当 sheet_name 传入列表时，pd.read_excel() 返回一个字典（dict），
#而不是单个 DataFrame。字典的键是列表中的元素（0、1、'Merge'），值是对应工作表的 DataFrame。
import pandas as pd    
df = pd.read_excel('data.xlsx', sheet_name = [0,1,'Merge']) 
print(type(df))
for key, values in df.items():
    print(key, values)


    

