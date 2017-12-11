import dataRetrival
import webScraper
import excel
import anomaly as an
import datetime

def main(months, var):
	currentPrice = dataRetrival.getCurrentPrice()
	currentPrice = float(currentPrice)
	pastPricesX, pastPricesY = dataRetrival.getPastPrices(datetime.date.today() - datetime.timedelta(1), months)
	previousPrice = float(pastPricesY[len(pastPricesY) - 1])
	linearVars = dataRetrival.linearRegression(pastPricesX, pastPricesY)
	degree = dataRetrival.crossValidationDegree(pastPricesX, pastPricesY)
	polyVars = dataRetrival.polynomialRegression(pastPricesX, pastPricesY, degree)
	anomaly = an.checkAnomaly(linearVars, polyVars, len(pastPricesX) + 1, currentPrice, var) #low
	LinearPred = an.LinearPrediction(linearVars, len(pastPricesX))
	PolyPred = an.PolynomialPrediction(polyVars, len(pastPricesX))
	pChange = an.AccuraryChange(currentPrice, LinearPred, PolyPred)
	headline = an.createHeadline(anomaly, currentPrice, pChange)
	print(headline)
	extraInfo = webScraper.extraBTCInfo(2)[0]

	#excel.WB(currentPrice, anomaly, headline, str(pChange) + "%", extraInfo)

main(3, 0)
