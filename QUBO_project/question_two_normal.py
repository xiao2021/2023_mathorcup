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

#假设贷款资金为1
Income = 0
Rate = 0.08 #收益率为8%
MAX_income =  0

for i in range(10):
    for j in range(10):
        for k in range(10):
            pass_rate = PASS_Aarray[0][i]*PASS_Aarray[0][j]*PASS_Aarray[0][k]
            loss_rate = (LOSS_Array[0][i]+LOSS_Array[0][j]+LOSS_Array[0][k])/3
            Income = pass_rate*(1-loss_rate)*Rate - pass_rate*loss_rate
            print(Income)
            if(Income>MAX_income):
                MAX_income = Income
                MAX_i = i
                MAX_j = j
                MAX_k = k
    
print("最大收益："+str(MAX_income))
print("评分卡0阈值:"+str(MAX_i))
print("评分卡1阈值:"+str(MAX_j))
print("评分卡2阈值:"+str(MAX_k))

# 最大收益：0.037313191520000004
#所有从0开始计数
# 评分卡0阈值:3
# 评分卡1阈值:3
# 评分卡2阈值:3


