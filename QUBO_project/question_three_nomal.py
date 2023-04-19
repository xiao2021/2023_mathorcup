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
for m in range(100):
    for n in range(100):
        if(m==n):
            break
        for l in range(100):
            if(m==l or n==l):
                break
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        pass_rate = PASS_Aarray[i][m]*PASS_Aarray[j][n]*PASS_Aarray[k][l]
                        loss_rate = (LOSS_Array[i][m]+LOSS_Array[j][n]+LOSS_Array[k][l])/3
                        Income = pass_rate*(1-loss_rate)*Rate - pass_rate*loss_rate
                        if(Income>MAX_income):
                            MAX_income = Income
                            MAX_i = i
                            MAX_j = j
                            MAX_k = k
                            MAX_m = m
                            MAX_n = n
                            MAX_l = l
                            print(MAX_income)
    
print("最大收益："+str(MAX_income))

print("最优评分卡1:"+str(MAX_m))
print("阈值::"+str(MAX_i))

print("最优评分卡2:"+str(MAX_n))
print("阈值::"+str(MAX_j))

print("最优评分卡3:"+str(MAX_l))
print("阈值::"+str(MAX_k))


