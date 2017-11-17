import numpy as np
import pandas as pd
from sklearn import datasets
from matplotlib import pyplot as plt
import random
import time


def grad_disc(x, y, theta, iterations, alpha):
    # print(x.shape)
    # print(y.shape)
    # print(theta.shape)
    for i in range(0,iterations):
        theta -= (alpha/x.shape[0]) * (np.dot(x.transpose(), (np.dot(x, theta) - y)))
        print(theta)
    return theta


def make_prediction(pred_val, theta):
    return np.dot(theta.transpose(), pred_val)


def gen_data(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y


def plot_model(x, y, w):
    plt.plot(x[:,1], y, "x")
    plt.plot(x[:,1], x * w, "r-")
    plt.show()


x,y = gen_data(100, 25, 10)
#plt.scatter(x[:,1],y) Just for plotting
#plt.show()
y = y[:, np.newaxis]
iterations = 1500
alpha = 0.01
theta = np.ones((x.shape[1], 1))

print(x.shape)
print(y.shape)
print(theta.shape)


answer_theta = grad_disc(x, y, theta, iterations, alpha)
print(answer_theta)

"""
print("Making prediction")
pred_val = np.array([1, 6.1101]) #x0 as 1, x1 6.1101 the value for which we ant to precict y
precicted_answer = make_prediction(pred_val, answer_theta)
print(precicted_answer)
"""