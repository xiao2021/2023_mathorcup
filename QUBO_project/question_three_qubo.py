import pandas as pd
import numpy as np
# neal是模拟退火的库 
import neal 
import itertools
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


    #做优化，比如123，132，321，213，231，312是一种情况，就可以不必计算
    pass_arr = np.zeros([1000000,1000])
    loss_arr = np.zeros([1000000,1000])
    digits = range(100)
    combos = itertools.combinations(digits, 3)

    # 输出所有可能的三个数字的无序组合
    for combo in combos:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    n = combo[0]*10000+combo[1]*100+combo[2]
                    m = 100*i+10*j+k
                    pass_arr[n][m] = PASS_Aarray[i][combo[0]]*PASS_Aarray[j][combo[1]]*PASS_Aarray[k][combo[2]]
                    loss_arr[n][m] = LOSS_Array[i][combo[0]]*LOSS_Array[j][combo[1]]*LOSS_Array[k][combo[2]]
                


    X_select = []
    Y_select= []
    for i in range(1000):
        Y_select.append(Binary('y'+str(i)))

    
    for i in range(1000000):
        X_select.append(Binary('x'+str(i)))
    

    M = 10
    H = (- Rate * Double_array_pass_sum(pass_arr,X_select,Y_select)
         +(1+Rate)*Double_array_pass_loss_sum(pass_arr,loss_arr,X_select,Y_select)
         + M * Constraint(((np.sum(X_select)-1)**2+(np.sum(Y_select)-1)**2), label='each have one right choice') 
    )

    model = H.compile()
    qubo, offset = model.to_qubo() 
    # print(qubo)
    # print(offset)
    sampler = neal.SimulatedAnnealingSampler()
    raw_solution = sampler.sample_qubo(qubo)
    a = raw_solution.first.sample
    print(a)
    return a


def Double_array_pass_sum(PASS_Aarray,X_select,Y_select):
    list=[]
    for i in range(1000000):
        for j in range(1000):
            list.append(PASS_Aarray[i][j]*X_select[i]*Y_select[j])
    return np.sum(list)


def Double_array_pass_loss_sum(pass_arr,loss_arr,X_select,Y_select):
    list=[]
    for i in range(1000000):
        for j in range(1000):
            list.append(loss_arr[i][j]*pass_arr[i][j]*X_select[i]*Y_select[j])

    return np.sum(list)


if __name__=='__main__':
    list = process()
    
