import numpy as np

#Using a low percentage difference gives more anomalies, high percentage differences gives less
low = 0.05
med = 0.10
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

def createHeadline(anomaly, currentPrice, previousPrice):
	if(anomaly == False):
		return "-"
	if(previousPrice < currentPrice):
		return "BTC has gone up from $" + str(previousPrice) + " to $" + str(currentPrice)
	elif(previousPrice > currentPrice):
		return "BTC has gone down from $" + str(previousPrice) + " to $" + str(currentPrice)
	else:
		return '-'

