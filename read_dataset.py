import pandas as pd
import matplotlib.pyplot as plt

def readData(datapath, year, month, dataType, currency1, currency2):
	filename=currency1+currency2+"_"+year+month
	dataset = pd.read_csv(datapath+filename+".csv")
	dates = [str(date)[4:] for date in dataset['Date']]
#    print(dates)
	cashbuy = list(dataset['CashBuy'])
	spotbuy = list(dataset['SpotBuy'])
	cashsell= list(dataset['CashSell'])
	spotsell= list(dataset['SpotSell'])
	# plot chart - Cash trading\
	plt.xlabel("Date")
	plt.ylabel("Price (NTD)")
	plt.title(filename+" "+dataType)	
	if dataType=='Cash':
		plt.plot(dates, cashbuy, label=dataType+'Buy')
		plt.plot(dates, cashsell,label=dataType+'Sell')
#		plt.savefig(filename+"_"+dataType+".png",dpi=300,format="png")		
		plt.show()	
		return cashbuy, cashsell, dates
	if dataType=='Spot':
		plt.plot(dates, spotbuy, label='SpotBuy')
		plt.plot(dates, spotsell,label='SpotSell')
#		plt.savefig(filename+"_"+dataType+".png",dpi=300,format="png")		
		plt.show()		
		return spotbuy, spotsell, dates