import numpy as np
import math
import scipy.stats as st

#Using a low percentage difference gives more anomalies, high percentage differences gives less
low = 0.10
med = 0.15
high = 0.20

#Takes linearVars as [slope, yintercept] and polyVars as [coefficients..., yintercept], and current as today's value
#currentPrice as the price for today, and receptivity as 0, 1, 2 as low, medium, high
def checkAnomaly(linearVars, polyVars, current, currentPrice, receptivity):
	linearFunc = lambda x: (linearVars[0] * x) + linearVars[1]
	linearPrediction = linearFunc(current)
	polyFunc = np.poly1d(polyVars)
	polyPrediction = polyFunc(current)

	#Compare Predictions with Actual
	if(receptivity == 0):
		return checkAnomalyHelper(linearPrediction, polyPrediction, currentPrice, low)
	elif(receptivity == 1):
		return checkAnomalyHelper(linearPrediction, polyPrediction, currentPrice, med)
	elif(receptivity == 2):
		return checkAnomalyHelper(linearPrediction, polyPrediction, currentPrice, high)
	return False

def checkAnomalyHelper(linearPredict, polyPredict, currentPrice, recepVal):
	linearLowerBound, linearUpperbound = linearPredict - (linearPredict * recepVal), linearPredict + (linearPredict * recepVal)
	polyLowerBound, polyUpperbound = polyPredict - (polyPredict * recepVal), polyPredict + (polyPredict * recepVal)

	#Testing
	print("CurrentPrice")
	print(currentPrice)
	print("Bounds")
	print(linearLowerBound, linearUpperbound)
	print(polyLowerBound, polyUpperbound)
	print("Predictions")
	print(linearPredict, polyPredict)

	if((currentPrice < linearLowerBound or currentPrice > linearUpperbound) and (currentPrice < polyLowerBound or currentPrice > polyUpperbound)):
		return True
	return False

def LinearPrediction(linearVars, current):
	linearFunc = lambda x: (linearVars[0] * x) + linearVars[1]
	linearPrediction = linearFunc(current)
	return linearPrediction

def PolynomialPrediction(polyVars, current):
	polyFunc = np.poly1d(polyVars)
	polyPrediction = polyFunc(current)
	return polyPrediction

def AccuraryChange(currentprice,linearPred, PolyPred):
	LinChange = ((currentprice - linearPred)/ linearPred) * 100
	PolyChange = ((currentprice - PolyPred)/PolyPred) * 100
	pChange = [0,0]
	print(LinChange, PolyChange)
	if (math.fabs(LinChange) > math.fabs(PolyChange)):
		pChange[0] = PolyChange
		pChange[1] = PolyPred
	else:
		pChange[0] =LinChange
		pChange[1] = linearPred

	return pChange

def createHeadline(anomaly, currentPrice, pChange):
	if(anomaly == False):
		return "-"
	if(pChange[0] > 0 ):
		return "BTC Hits Unusual High - Breaking predicted values by " + str(math.ceil(pChange[0])) + "%! "
	elif(pChange[0] < 0):
		return "BTC Hit New Lows - Going below Predicted Values by " + str(math.ceil(pChange[0])) + "% " "from $" + str(pChange[1]) + " to $" + str(currentPrice)
	else:
		return '-'

