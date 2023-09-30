import numpy as np
import matplotlib.pyplot as plt
import random
data = np.genfromtxt('HousePricing.csv',dtype=float,delimiter=',')

#print(data[1,0])
def plotData(data,a,b):
    X = data[:,0]
    Y = data[:,1]


    plt.scatter(X,Y)

    x = np.linspace(-5, 5, 100)
    y=a*x+b
    plt.plot(x,y)

    plt.show()



def computePredictedValue(x,a,b):
    return a*x + b

def computeLoss(a,b):
    sum = 0
    for i in range(len(data)):
        sum += pow(( computePredictedValue(data[i,0],a,b) - data[i,1] ),2)
    return sum * 1/len(data)

def computeDerivativeLoss(a,b,attr) : # return ka
    sum=0
    if attr ==0: # find kb:
        for i in range(len(data)):
            sum += ( computePredictedValue(data[i,0],a,b) - data[i,1] )
    if attr ==1 : # find ka:
        for i in range(len(data)):
            sum += (( computePredictedValue(data[i,0],a,b) - data[i,1] ) * data[i,0])

    return sum * 2/len(data)

a=  random.random() - 0.5
b = random.random() - 0.5
loop = 2000
learningRate = 0.01
for i in range(loop):
    ka = computeDerivativeLoss(a,b,1)
    kb = computeDerivativeLoss(a,b,0)
    a-= ka*learningRate
    b-= kb*learningRate

print("a-b", a, " - " ,b)
print(computeLoss(a,b))

plotData(data,a,b)