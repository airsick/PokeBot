import numpy as np
import math

X = np.array(([16, 0, 11, 16, 1, -1, 9, -1, 14, -1, 15, 5, 9, -1, 16, 95, 0, 130, 15, 110, 8, 0]), dtype=float)

class NeuralNetwork(object):
  def __init__(self):
    #parameters
    self.inputSize = 22
    self.hiddenSize1 = 18
    self.hiddenSize2 = 15
    self.outputSize = 9

    #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize1) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize1, self.hiddenSize2) # (3x1) weight matrix from hidden to output layer
    self.W3 = np.random.randn(self.hiddenSize2, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    np.array((X),dtype=float)
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    self.z4 = self.sigmoid(self.z3) # dot product of hidden layer (z2) and second set of 3x1 weights
    self.z5 = np.dot(self.z4, self.W3) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z5) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))
