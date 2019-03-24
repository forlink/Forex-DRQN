from config import getConfig
from read_dataset import readData

if __name__ == '__main__':
	FLAG = getConfig()
	
	BuyPriceMap, SellPriceMap, Dates = readData(FLAG['datapath'], FLAG['year'], FLAG['month'], FLAG['dataType'], FLAG['currency1'], FLAG['currency2'])
	
#	forex = Forex(PriceMap = SellPriceMap, count = FLAG['count'])
	
#	RL = DeepNetwork(forex = forex, dates = dates, featureNum = featureNum, config = FLAG)
#	RL.train()