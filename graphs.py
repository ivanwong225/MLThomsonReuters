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

def precisionPlot(months):
    X, y = get_Precision_Values(months)
    plt.title("Precision Values")
    plt.xlabel("Requirement")
    plt.ylabel("Precision")
    plt.show()

def recallPlot(months):
    X, y = get_Recall_Values(months)
    plt.title("Recall Values")
    plt.xlabel("Requirement")
    plt.ylabel("Recall")
    plt.show()

def f1Plot(months):
    X, y = get_f1_Values(months)
    plt.title("F1 Values")
    plt.xlabel("Requirement")
    plt.ylabel("F1")
    plt.show()
    