import numpy as np
import pandas as pd


def grad_disc(x, y, theta, iterations, alpha):
    # print(x.shape)
    # print(y.shape)
    # print(theta.shape)
    for i in range(0,iterations):
        theta -= (alpha/x.shape[0]) * (np.dot(x.transpose(), (np.dot(x, theta) - y)))
    return theta


def make_prediction(pred_val, theta):
    return np.dot(theta.transpose(), pred_val)

training = np.genfromtxt("ex1data1.txt", delimiter=",")
x_0 = np.ones((training.shape[0],1)) #Nasty piece of hack
"""
Turns out that dimensions (97,) and (97,1) are different
All np.append,np.concatenate, np.hstack only works if there is a second dimension.
np.append(x_0, training, 1)
np.concatenate((x_0, training), 1)
np.hstack((x_0, training))

"""
training = np.hstack((x_0, training))


x, y = training[:, :2], training[:, 2] #Seperating training and results, x and y
y = y[:, np.newaxis] #To convert (97,) to (97,1)
print(x)
print("----------------------------------")
print(y)

theta = np.zeros((x.shape[1],1))
print("----------------------------------")
print(theta)

iterations = 1500
alpha = 0.01

answer_theta = grad_disc(x, y, theta, iterations, alpha)
print(answer_theta)

print("Making prediction")
pred_val = np.array([1, 6.1101]) #x0 as 1, x1 6.1101 the value for which we ant to precict y
precicted_answer = make_prediction(pred_val, answer_theta)
print(precicted_answer)