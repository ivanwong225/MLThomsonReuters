import dataRetrival
import datetime
import anomaly as an

def anomalyEvalSetUp(endDate, months):
	X, y = dataRetrival.getPastPrices(endDate, months)
	currentPrice = y[len(y) - 1][0]
	X = X[:-1]
	y = y[:-1]
	return currentPrice, X, y

def precisionRecallF1(listDates, manualAnomalyList, months, var):
	trueP = 0.0
	falseP = 0.0
	falseN = 0.0
	trueN = 0.0
	for i in range(0, len(listDates)):
		eval = precisionRecallHelper(listDates[i], months, var, manualAnomalyList[i])
		if(eval == 0):
			trueP = trueP + 1
		if(eval == 1):
			falseP = falseP + 1
		if(eval == 2):
			falseN = falseN + 1
		if(eval == 3):
			trueN = trueN + 1
	precision = trueP / (trueP + falseP)
	recall = trueP / (trueP + falseP)
	
	F1 = 2 * (precision * recall) / (precision + recall)
	print('\nEVALUATION RESULTS')
	print('Precision: ' + str(precision))
	print('Recall: ' + str(recall))
	print('F1: ' + str(F1))

def precisionRecallHelper(date, months, var, manualAnomaly):
	programAnomaly = anomalyDetect(date, months, var)
	if(programAnomaly and manualAnomaly):
		#True Positive
		return 0
	if(programAnomaly and manualAnomaly == False):
		#False Positive
		return 1
	if(programAnomaly == False and manualAnomaly):
		#False Negative
		return 2
	if(programAnomaly == False and manualAnomaly == False):
		#True Negative
		return 3
	return None

def anomalyDetect(date, months, var):
	endDate = datetime.date(2017, 9, 14) #Manual Entry
	currentPrice, pastPricesX, pastPricesY = anomalyEvalSetUp(date, months)
	linearVars = dataRetrival.linearRegression(pastPricesX, pastPricesY)
	degree = dataRetrival.crossValidationDegree(pastPricesX, pastPricesY)
	polyVars = dataRetrival.polynomialRegression(pastPricesX, pastPricesY, degree)
	anomaly = an.checkAnomaly(linearVars, polyVars, len(pastPricesX) + 1, currentPrice, var)
	return anomaly

precisionRecallF1([datetime.date(2017, 9, 14)], [True], 3, 0)