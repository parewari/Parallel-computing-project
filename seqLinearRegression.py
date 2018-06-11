import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import time
from random import randint

def tran(data):
    return [[row[i] for row in data] for i in range(len(data[0]))]
def multi(A,B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]
def getData(num=4):
    filename=str(num)+"-datapoint.txt"
    text_file = open(filename, "r")
    X=[]
    Y=[]
    for line in text_file:
        x,y =line[:-1].split(",")
        X.append(int(x))
        Y.append(int(y))
    text_file.close()
    return X,Y

## Get Data
x,y1=getData(10000) 
y=[]
y.append(y1)

start = time.time()

matXT=[[1]*len(x),x]
matX=tran(matXT)
matT=tran(y)
matXTT=np.matrix(multi(matXT,matT))
matXTX=np.matrix(multi(matXT,matX))
matW = inv(matXTX)
matW=matW*matXTT

listW = matW.tolist()
listW= [listW[0][0],listW[1][0]]

print("The Slope =",listW)
done = time.time()
## time exc
print("Time diff =",done-start)
    
## plot

plt.scatter(x[:100],y1[:100],color="m",marker="o",s=30)

x_pred=np.arange(-2000,2000,1)

plt.plot(x_pred,listW[1]*x_pred+listW[0],color='g')
##plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([-2000,2000,-2000,2000])
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()

