import pandas as pd
import time


#Reading poloniex api, period is in seconds, start is timestamp for 1/1/2017, pair is USDT ETH.
pair = "USDT_ETH"
start = "1483228800"
period = "300"

#Since the API gives a json file we directly transform it to pandas dataframe.
df = pd.read_json("https://poloniex.com/public?command=returnChartData&currencyPair="+pair+"&start="+start+"&end=9999999999&period="+period)


#Save to csv file, replace by df.to_excel to get excel file.
df.to_csv()

#testing some of the columns.
#print(df["date"])
#print(df["low"])
#print(df["high"])
#print(df["open"])
#print(df["close"])