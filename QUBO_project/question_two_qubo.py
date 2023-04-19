import pandas as pd
import numpy as np
# neal是模拟退火的库 
import neal 
# pyqubo 可以使用Binary定义变量，Constarint定义约束
from pyqubo import Binary, Constraint 

def process():
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
    # Income = 0
    Rate = 0.08 #收益率为8%
    # MAX_income =  0

    X_select=[]

    for i in range(1000):
        X_select.append(Binary('x'+str(i)))

    arr_pass = np.zeros(1000)
    arr_loss = np.zeros(1000)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                n=100*i+10*j+k
                pass_num=PASS_Aarray[j][0]*PASS_Aarray[j][1]*PASS_Aarray[k][2]
                arr_pass[n]=pass_num

    for i in range(10):
        for j in range(10):
            for k in range(10):
                n=100*i+10*j+k
                loss_num=LOSS_Array[j][0]*LOSS_Array[j][1]*LOSS_Array[k][2]
                arr_loss[n]=loss_num

    M = 100
    H = (- Rate * Double_array_pass_sum(arr_pass,X_select)
         +(1+Rate)*Double_array_pass_loss_sum(arr_pass,arr_loss,X_select)
         + M * Constraint(((np.sum(X_select)-1)**2), label='1000 have one right choice') 
    )

    model = H.compile()
    qubo, offset = model.to_qubo() 
    print(qubo)
    # print(offset)
    sampler = neal.SimulatedAnnealingSampler()
    raw_solution = sampler.sample_qubo(qubo)
    a = raw_solution.first.sample
    print(a)
    return a


def Double_array_pass_sum(pass_arr,x_select):
    list=[]
    for i in range(1000):
        list.append(pass_arr[i]*x_select[i])
    return np.sum(list)


def Double_array_pass_loss_sum(arr_pass,arr_loss,X_select):
    list=[]

    for i in range(1000):
        list.append(arr_loss[i]*arr_pass[i]*X_select[i])
    
    return np.sum(list)

            
if __name__=='__main__':
    list = process()
    
    for i in range(1000):
        if(list["x"+str(i)]!=0):
            num=i
            print("x"+str(i))
    
    print("评分卡1阈值："+str(int(num/100)+1))
    print("评分卡2阈值："+str(int(num // 10 % 10)+1))
    print("评分卡3阈值："+str(int(num % 10)+1))


        
    


