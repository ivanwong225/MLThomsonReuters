# -*- coding: utf-8 -*-
"""
Author: echanglc
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

def linearRegressionPlot(X, y, linear_func):
    y2 = list(map(linear_func, X))
    plt.plot(X, y, 'ro')
    plt.plot(X, y2, 'r--')
    plt.xlim(0, len(X))
    plt.title("Linear Regression")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def polynomialRegressionPlot(X, y, poly_func):
    plt.plot(X, y, 'ro', X, poly_func(X), '--')
    plt.xlim(0, len(X))
    plt.title("Polynomial Regression")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def evaluationPlot():
    plt.subplot(223)
    X = [.10,.15,.25]
    y = [0.6785,0.7727,0.8333]
    plt.xticks([.10,.15,.25])
    plt.yticks([.10,.20,.30,.40,.50,.60,.70,.80,.90,1.0], [".10",".20",".30",".40",".50",".60",".70",".80",".90","1.0"])
    plt.plot(X, y, label="Precision Values")
    plt.title("Evaluation for six months of data")
    plt.xlabel("Requirement")
    plt.ylabel("Values")
    y = [0.8636,0.7727,0.6818]
    plt.plot(X, y, label="Recall")
    y = [0.76,0.7727,0.75]
    plt.plot(X, y, label="F1 Values")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()