import dataRetrival
import webScraper
import excel
import testing

def main(months):
	currentPrice = dataRetrival.getCurrentPrice()
	currentPrice = float(currentPrice)
	pastPricesX, pastPricesY = dataRetrival.getPastPrices(3)
	previousPrice = float(pastPricesY[len(pastPricesY) - 1])
	linearVars = dataRetrival.linearRegression(pastPricesX, pastPricesY)
	polyVars = dataRetrival.polynomialRegression(pastPricesX, pastPricesY)
	anomaly = testing.checkAnomaly(linearVars, polyVars, len(pastPricesX) + 1, currentPrice, 0) #low
	headline = testing.createHeadline(anomaly, currentPrice, previousPrice)
	extraInfo = webScraper.extraBTCInfo(2)[0]
	pChange = int(((currentPrice - previousPrice) / (previousPrice)) * 100)
	excel.WB(currentPrice, anomaly, headline, str(pChange) + "%", extraInfo)
	
main(3)

