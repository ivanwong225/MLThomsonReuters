import json
import requests
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as spcs
from decimal import Decimal
from sklearn.base import BaseEstimator
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

	#print(PP_array) Need to convert pastPrices to 2-D Array of Time / Price
	data = np.asarray(PP_array)
	X,y = data[:, 0, np.newaxis], data[:, 1, np.newaxis]
	X = X.astype(int)
	return X, y

def linearRegression(X, y):
	values = spcs.mstats.linregress(X, y)
	slope, intercept = values[0], values[1]
	linearFunc = lambda x: slope * x + intercept
	y2 = list(map(linearFunc, X))
	#plt.plot(X, y, 'ro')
	#plt.plot(X, y2, 'r--')
	#plt.xlim(0, len(X))
	#plt.title("Linear Regression")
	#plt.show()
	
	return [slope, intercept]

def polynomialRegression(X, y, degree):
	x = []
	Y= []

	for i in range(len(X)):
		x.append(X[i][0])
		Y.append(y[i][0])

	fit = np.polyfit(x, Y, degree)
	fit_fn = np.poly1d(fit)

	#plt.plot(X, y, 'ro', x, fit_fn(x), '--')
	#plt.xlim(0, len(X))
	#plt.title("Polynomial Regression")
	#plt.show()
	return fit

def crossValidationDegree(xs, ys):
	x = []
	Y= []

	for i in range(len(xs)):
		x.append(xs[i][0])
		Y.append(ys[i][0])

	estimator = CVPolynomialRegression()
	degrees = np.arange(1, 25)
	cv_model = GridSearchCV(estimator, param_grid={'deg': degrees}, scoring='neg_mean_squared_error')
	cv_model.fit(x, Y);
	return cv_model.best_params_['deg']

class CVPolynomialRegression(BaseEstimator):
	def __init__(self, deg=None):
		self.deg = deg
	
	def fit(self, X, y, deg=None):
		self.model = LinearRegression(fit_intercept=False)
		self.model.fit(np.vander(X, N=self.deg + 1), y)
	
	def predict(self, x):
		return self.model.predict(np.vander(x, N=self.deg + 1))
	
	@property
	def coef_(self):
		return self.model.coef_