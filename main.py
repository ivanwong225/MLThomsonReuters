import dataRetrival
import webScraper
import excel
import anomaly as an

def main(months, var):
	currentPrice = dataRetrival.getCurrentPrice()
	currentPrice = float(currentPrice)
	pastPricesX, pastPricesY = dataRetrival.getPastPrices(months)
	previousPrice = float(pastPricesY[len(pastPricesY) - 1])
	linearVars = dataRetrival.linearRegression(pastPricesX, pastPricesY)
	degree = dataRetrival.crossValidationDegree(pastPricesX, pastPricesY)
	polyVars = dataRetrival.polynomialRegression(pastPricesX, pastPricesY, degree)
	anomaly = an.checkAnomaly(linearVars, polyVars, len(pastPricesX) + 1, currentPrice, var) #low
	headline = an.createHeadline(anomaly, currentPrice, previousPrice)
	extraInfo = webScraper.extraBTCInfo(2)[0]
	pChange = int(((currentPrice - previousPrice) / (previousPrice)) * 100)
	#excel.WB(currentPrice, anomaly, headline, str(pChange) + "%", extraInfo)
	
main(3, 0)
