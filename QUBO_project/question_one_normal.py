import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

Card_id = np.arange(0,100,1)
Threshold = np.arange(0,10,1)

#假设贷款资金为1
Income = 0
Rate = 0.08 #收益率为8%
MAX_income =  0
Income_Height = np.zeros((len(Threshold),len(Card_id)),dtype=np.float32)
for j in range(10):
    for i in range(100):
        Income = PASS_Aarray[j][i]*(1-LOSS_Array[j][i])*Rate - PASS_Aarray[j][i]*LOSS_Array[j][i]
        Income_Height[j][i]=Income
        if(Income>MAX_income):
            MAX_income = Income
            MAX_i = i
            MAX_j = j


# print(Income_Height)

X,Y = np.meshgrid(Card_id,Threshold)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X,Y,Income_Height,cmap='jet')
plt.show()


print("最大收益："+str(1000000*MAX_income))
print("评分卡:"+str(MAX_i))
print("阈值："+str(MAX_j))
##输出结果
#所有从0开始计数
# 最大收益：0.061172
# max_i:48
# max_j:0



