#Complete Evaluation is for evaluation of our model
#Created by Rohan Johar
import dataRetrival
import datetime
import anomaly as an

def completeEvaluation(listDates, manualAnomalyList):
	months = 1
	rl = []
	for i in range(0, 3):
		for var in range(0, 3):
			rl.append(precisionRecallF1(listDates, manualAnomalyList, months, var))
		if(months == 1):
			months = 3
		elif(months == 3):
			months = 6
	return rl
	
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
	recall = trueP / (trueP + falseN)
	F1 = 2 * (precision * recall) / (precision + recall)
	accuracy = (trueP + trueN) / (trueP + trueN + falseP + falseN)
	#print('\nEVALUATION RESULTS')
	#print('Precision: ' + str(precision))
	#print('Recall: ' + str(recall))
	#print('F1: ' + str(F1))

	return precision, recall, F1, accuracy, months, var

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
	endDate = datetime.date(2017, 12, 14) #Manual Entry
	currentPrice, pastPricesX, pastPricesY = anomalyEvalSetUp(date, months)
	linearVars = dataRetrival.linearRegression(pastPricesX, pastPricesY)
	degree = dataRetrival.crossValidationDegree(pastPricesX, pastPricesY)
	polyVars = dataRetrival.polynomialRegression(pastPricesX, pastPricesY, degree)
	anomaly = an.checkAnomaly(linearVars, polyVars, len(pastPricesX) + 1, currentPrice, var)
	LinearPred = an.LinearPrediction(linearVars, len(pastPricesX))
	PolyPred = an.PolynomialPrediction(polyVars, len(pastPricesX))
	pChange = an.AccuraryChange(currentPrice, LinearPred, PolyPred)
	headline = an.createHeadline(anomaly, currentPrice, pChange)
	print(headline)
	return anomaly

listDates = [datetime.date(2017, 1, 4),
			 datetime.date(2017, 3, 18),
			 datetime.date(2017, 5, 11),
			 datetime.date(2017, 5, 24),
			 datetime.date(2017, 5, 27),
			 datetime.date(2017, 6, 6),
			 datetime.date(2017, 6, 10),
			 datetime.date(2017, 7, 16),
			 datetime.date(2017, 7, 20),
			 datetime.date(2017, 8, 14),
			 datetime.date(2017, 9, 1),
			 datetime.date(2017, 9, 14),
			 datetime.date(2017, 10, 9),
			 datetime.date(2017, 11, 3),
			 datetime.date(2017, 11, 10),
			 datetime.date(2017, 11, 12),
			 datetime.date(2017, 11, 16),
			 datetime.date(2017, 11, 27),
			 datetime.date(2017, 12, 1),
			 datetime.date(2017, 12, 6),
			 datetime.date(2017, 12, 7),
			 datetime.date(2017, 12, 9),
			 datetime.date(2017, 1, 15),
			 datetime.date(2017, 2, 11),
			 datetime.date(2017, 2, 15),
			 datetime.date(2017, 3, 30),
			 datetime.date(2017, 4, 10),
			 datetime.date(2017, 4, 17),
			 datetime.date(2017, 4, 27),
			 datetime.date(2017, 5, 4),
			 datetime.date(2017, 5, 16),
			 datetime.date(2017, 6, 14),
			 datetime.date(2017, 6, 26),
			 datetime.date(2017, 7, 4),
			 datetime.date(2017, 7, 7),
			 datetime.date(2017, 7, 28),
			 datetime.date(2017, 8, 1),
			 datetime.date(2017, 8, 26),
			 datetime.date(2017, 9, 10),
			 datetime.date(2017, 9, 20),
			 datetime.date(2017, 9, 25),
			 datetime.date(2017, 10, 6),
			 datetime.date(2017, 10, 25),
			 datetime.date(2017, 11, 9)
]

manualAnomalyList = [True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
True,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False,
False]

anomalyDetect(datetime.date(2017, 12, 7), 1, 0)
anomalyDetect(datetime.date(2017, 12, 8), 1, 0)
anomalyDetect(datetime.date(2017, 12, 9), 1, 0)

anomalyDetect(datetime.date(2017, 12, 7), 6, 0)
anomalyDetect(datetime.date(2017, 12, 8), 6, 0)
anomalyDetect(datetime.date(2017, 12, 9), 6, 0)


