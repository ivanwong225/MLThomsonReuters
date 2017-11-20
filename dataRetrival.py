import json
import requests
import datetime
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

#Basic coindesk API hook
#Need to convert pastPrices to 2-D Array of Time / Price

def getCurrentPrice():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    j_obj = json.loads(response.text)
    x = j_obj["bpi"]["USD"]["rate"]
    return Decimal(x.replace(",", ""))

def getPastPrices(months):
    today = datetime.date.today()
    startDate = today - datetime.timedelta(months*365/12)
    endDate = today - datetime.timedelta(1)
    response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?start=" + str(startDate) + "&end=" + str(endDate))
    j_obj = json.loads(response.text)
    pastPrices = j_obj["bpi"]
    #2D Array Conversion
    PP_array = []
    #Use i to represent day instead of using actual date
    #actual date is a string and not easy to read on graph
    i = 1
    for key, value in pastPrices.items():
        PP_array.append([i, value])
        i += 1

    return PP_array
    #print(PP_array) Need to convert pastPrices to 2-D Array of Time / Price

#Gets data for past 3 months
data= getPastPrices(3)
#Presents data as an array instead of list
data = np.asarray(data)
n = data.shape[0]
X,y = data[:, 0, np.newaxis], data[:, 1, np.newaxis]
X = X.astype(int)
y = y/1000

# print(X)
# x = []
# y = []
# for i in range(len(X)):
#     x.append(X[i][0])
#     y.append(Y[i][0]/1000)
# X = x
#
# print(X)
# print(y)

# z = np.polyfit(x, y, 3)
# z_n = np.poly1d(z)
#
# plt.plot(x, y, 'yo', x, z_n(x), '--')
# plt.show()
def add_column(X):
    assert len(X.shape) == 2 and X.shape[1] == 1

    # raise NotImplementedError("Insert a column of ones to right side of the matrix")
    return np.insert(X, 0, 1, axis=1)

def predict(X, theta):
    """ Computes h(x; theta) """
    assert len(X.shape) == 2 and X.shape[1] == 1
    assert theta.shape == (2, 1)

    X_prime = add_column(X)
    pred = X_prime @ theta
    # raise NotImplementedError("Compute the regression predictions")
    return pred

def loss(X, y, theta):
    assert X.shape == (n, 1)
    assert y.shape == (n, 1)
    assert theta.shape == (2, 1)

    X_prime = add_column(X)
    assert X_prime.shape == (n, 2)

    # raise NotImplementedError("Compute the model loss; use the predict() function")
    loss = ((predict(X, theta) - y)**2).mean()/2
    return loss

theta_init = np.zeros((2, 1))
print(loss(X, y, theta_init))

import scipy.optimize
from functools import partial

def loss_gradient(X, y, theta):
    X_prime = add_column(X)
    loss_grad = ((predict(X, theta) - y)*X_prime).mean(axis=0)[:, np.newaxis]
#     raise NotImplementedError("Compute the model loss gradient; "
#                               "use the predict() function; "
#                               "this also must be vectorized!")
    return loss_grad

assert loss_gradient(X, y, theta_init).shape == (2, 1)

def run_gd(loss, loss_gradient, X, y, theta_init, lr=.0001, n_iter=1500):
    theta_current = theta_init.copy()
    loss_values = []
    theta_values = []

    for i in range(n_iter):
        loss_value = loss(X, y, theta_current)
        theta_current = theta_current - lr*loss_gradient(X, y, theta_current)
        loss_values.append(loss_value)
        theta_values.append(theta_current)

    return theta_current, loss_values, theta_values

result = run_gd(loss, loss_gradient, X, y, theta_init)
theta_est, loss_values, theta_values = result

print('estimated theta value', theta_est.ravel())
print('resulting loss', loss(X, y, theta_est))
plt.ylabel('loss')
plt.xlabel('iter_i')
plt.plot(loss_values)
plt.show()

plt.ylabel('log(loss)')
plt.xlabel('iter_i')
plt.semilogy(loss_values)
plt.show()
plt.scatter(X, y, marker='x', color='r', alpha=0.5)
plt.show()

plt.scatter(X, y, marker='x', color='r', alpha=0.5)
x_start, x_end = 0, 100
plt.xlim(x_start, x_end)
plt.ylim(0, 9)
X_test = np.array([[0], [100]])
y_test = predict(X_test, theta_est)
plt.plot(X_test, y_test)

plt.show()

#Test
print(predict(np.array([[80], [120]]), theta_est))


