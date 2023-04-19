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
    Y_select=[]
    for i in range(100):
        X_select.append(Binary('x'+str(i)))

    for j in range(10):
        Y_select.append(Binary('y'+str(j)))
    M = 10
    H = (- Rate * Double_array_pass_sum(X_select,Y_select,PASS_Aarray)
         +(1+Rate)*Double_array_pass_loss_sum(X_select,Y_select,LOSS_Array,PASS_Aarray)
         + M * Constraint(((np.sum(X_select)-1)**2+
                           (np.sum(Y_select)-1)**2), label='only one x and y') 
    )
    model = H.compile()
    qubo, offset = model.to_qubo() 
    print(qubo)
    # print(offset)
    sampler = neal.SimulatedAnnealingSampler()
    raw_solution = sampler.sample_qubo(qubo)
    print(raw_solution.first.sample)


def Double_array_pass_sum(X_select,Y_select,pass_arr):
    arr = np.array(pass_arr)
    list=[]
    for i in range(100):
        for j in range(10):
            list.append(arr[j][i]*X_select[i]*Y_select[j])
    return np.sum(list)

def Double_array_pass_loss_sum(X_select,Y_select,loss_arr,pass_arr):
    arr = np.array(loss_arr)
    list=[]
    for i in range(100):
        for j in range(10):
            list.append(arr[j][i]*pass_arr[j][i]*X_select[i]*Y_select[j])
    return np.sum(list)

            
if __name__=='__main__':
    process()
        
    