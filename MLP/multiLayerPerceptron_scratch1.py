import numpy as np
from abc import ABC, abstractmethod

class Layer(ABC):
    @abstractmethod
    def forward(self,priorForward):
        pass

    def backward(self, priorLoss,learningRate):
        pass

class NetworkLayer(Layer):
    def __init__(self, numberOfInput, numberOfOutput):
        self.weights = np.random.rand(numberOfInput,numberOfOutput) - 0.5
        self.bias = np.random.rand(1,numberOfOutput) - 0.5

    def forward(self,priorForward):
        self.input = priorForward
        self.output = np.dot(priorForward,self.weights) + self.bias
        return self.output


    def backward(self, priorLoss,learningRate):
        self.weights += (np.dot(self.input.T ,priorLoss) * learningRate)
        self.bias += (priorLoss* learningRate)

        return np.dot(priorLoss,self.weights.T)


class ActivationLayer(Layer):
    def forward(self,priorForward):
        self.input = priorForward
        self.output= 1/(1+np.exp(-priorForward))
        return self.output

    def backward(self, priorLoss, learningRate):

        return np.multiply(self.output,(1-self.output)) * priorLoss


class Model:
    layers = []
    data = []
    expectedResults = []
    def add(self, layer):
        self.layers.append(layer)
    def fit(self, data, expectedResults):
        self.data = data
        self.expectedResults = expectedResults
    def predict(self, input):
        output = input
        for i in range(len(self.layers)):
            output = self.layers[i].forward(output)
        return output

    # def train(self, epoch, learningRate):
    #     for j in range(epoch):
    #         loss = 0
    #         d_loss = 0
    #         for t in range(len(self.data)):
    #             output = self.data[t]
    #             for i in range(len(self.layers)):
    #                 output = self.layers[i].forward(output)
    #             d_loss += (output - self.expectedResults[0, t])*-1
    #             loss += np.square(output - self.expectedResults[0,t])
    #         print("Loss: ",loss/len(self.data))
    #
    #         d_loss = d_loss*2 * (1/len(self.data))
    #         print("D_Loss:",d_loss)
    #         for i in reversed(range(len(self.layers))):
    #             d_loss = self.layers[i].backward(d_loss,learningRate)
    #
    #         print("--------")

    # Try with SGD FIX!!
    def train(self, epoch, learningRate):
        for j in range(epoch):
            loss = 0

            for t in range(len(self.data)):
                d_loss = 0
                output = self.data[t]
                for i in range(len(self.layers)):
                    output = self.layers[i].forward(output)
                d_loss = (output - self.expectedResults[0, t])*-1
                loss += np.square(output - self.expectedResults[0,t])

                d_loss = d_loss * 2 * (1 / len(self.data))
                print("D_Loss:", d_loss)
                for i in reversed(range(len(self.layers))):
                    d_loss = self.layers[i].backward(d_loss, learningRate)

            print("Loss: ",loss/len(self.data))
            print("--------")


model = Model()
model.add(NetworkLayer(2,2))
model.add(ActivationLayer())
model.add(NetworkLayer(2,1))

data = np.array([[[0,0]],[[0,1]],[[1,0]],[[1,1]]])
result = np.array([[0,1,1,0]])

model.fit(data,result)
model.train(5000,0.1)

print("Start predicting")
print(model.predict([0,0]))
print(model.predict([0,1]))
print(model.predict([1,0]))
print(model.predict([1,1]))