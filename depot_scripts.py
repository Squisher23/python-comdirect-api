from create_dataframe import get_df

def depot_transactions(outputdir):
	header = ['businessDate','quantity.value','instrument.wkn','instrument.shortName','instrument.staticData.instrumentType','executionPrice.value','transactionValue.value']
	newheader = ['Date','Quantity','WKN','Name','Type','UnitPrice','TotalPrice']
	df = get_df(outputdir+'/'+"depot_transactions.json", header, newheader)
	return df
	
def depot_positions():
	header = ['wkn','custodyType','quantity.value','currentPrice.price.value','currentPrice.priceDateTime','purchasePrice.value','currentValue.value','purchaseValue.value']
	newheader = ['WKN','Type','Quantity','CurrentUnitPrice','Date','PurchaseUnitPrice','CurrentTotalPrice','PurchaseTotalPrice']
	df2 = get_df(outputdir+'/'+"depot_positions.json", header, newheader)
	return df2
