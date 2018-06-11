from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import time
from random import randint
def multiply(a):
    x=a[0]
    y=a[1]
    return sum(i[0] * i[1] for i in zip(x, y))
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

if __name__ == '__main__':

##  GET DATA POINT
    x2,y=getData(10000)

    
    ## parallel compute
    start = time.time()
    
    x1=[1]*len(x2)
    multi = [[x1,x1],[x1,x2],[x2,x2],[x1,y],[x2,y]]
    pool = Pool(processes=4)
    ans=pool.map(multiply, multi)

    inver=inv(np.array([ans[:2],ans[1:3]]))
    temp=np.array(ans[3:5])
    listW=inver.dot(temp)
    
    print("The Slope =",listW)
    done = time.time()
    ## time exc
    print("Time diff =",done-start)
    
    ## plot
    
    plt.scatter(x2[:100],y[:100],color="m",marker="o",s=30)

    x_pred=np.arange(-2000,2000,1)

    plt.plot(x_pred,listW[1]*x_pred+listW[0],color='g')
    plt.axis([-2000,2000,-2000,2000])
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    plt.show()
