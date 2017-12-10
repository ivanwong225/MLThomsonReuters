# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

def linearRegressionPlot(X, y, linear_func):
    y2 = list(map(linearFunc, X))
    plt.plot(X, y, 'ro')
    plt.plot(X, y2, 'r--')
    plt.xlim(0, len(X))
    plt.title("Linear Regression")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def polynomicalRegessionPlot(X, y, poly_func):
    plt.plot(X, y, 'ro', x, fit_fn(x), '--')
    plt.xlim(0, len(X))
    plt.title("Polynomial Regression")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def evaluationPlot():
    plt.subplot(223)
    X = [.10,.15,.25]
    y = [.625,.75, 1.0]
    plt.plot(X, y, label="Precision Values")
    plt.title("Evaluation for three months of data")
    plt.xlabel("Requirement")
    plt.ylabel("Values")
    y = [.6,.6,.466]
    plt.plot(X, y, label="Recall")
    y = [.645, .7, .733]
    plt.plot(X, y, label="F1 Values")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    
