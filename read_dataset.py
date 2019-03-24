import pandas as pd
import matplotlib.pyplot as plt

def read_data(datapath, year, month, option, currency1, currency2):
	filename=currency1+currency2+"_"+year+month
	dataset = pd.read_csv(datapath+filename+".csv")
	dates = [str(date)[4:] for date in dataset['Date']]
#    print(dates)
	cashbuy = list(dataset['CashBuy'])
	spotbuy = list(dataset['SpotBuy'])
	cashsell= list(dataset['CashSell'])
	spotsell= list(dataset['SpotSell'])
	# plot chart - Cash trading
	if option=='Cash':
		plt.plot(dates, cashbuy, label='CashBuy')
		plt.plot(dates, cashsell,label='CashSell')
	if option=='Spot':
		plt.plot(dates, spotbuy, label='SpotBuy')
		plt.plot(dates, spotsell,label='SpotSell')		
	plt.xlabel("Date")
	plt.ylabel("Price (NTD)")
	plt.title(filename+" "+option)
	plt.show()
#	plt.savefig(filename+"_"+option+".png",dpi=300,format="png")	
