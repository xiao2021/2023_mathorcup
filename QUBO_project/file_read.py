# 读取数据
import pandas as pd
import numpy as np
data = pd.read_csv("data_100.csv")
data = np.array(data)
list_pass=[]
list_loss=[]
PASS_Aarray=[]
LOSS_Array=[]
for j in range(10):
    for i in range(100):
        list_pass.append(data[j][2*i])
        list_loss.append(data[j][2*i+1])
    PASS_Aarray.append(list_pass)
    LOSS_Array.append(list_loss)
    list_pass=[]
    list_loss=[]
# 以下内容为测试
# print(len(PASS_Aarray[0]))
print("行数："+str(len(PASS_Aarray)))
print("通过率第一行数据")
print(PASS_Aarray[0])
print("坏账率第一行数据")
print(LOSS_Array[0])


