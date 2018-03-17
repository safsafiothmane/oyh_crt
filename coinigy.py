import sys
import time 
import datetime
from optparse import OptionParser
import coinigy_api_rest as api
import indicators as ind

#You're account infos to connect to coinigy
acct = {
  "api_key": "enter_here",
  "api_secret": "enter_here",
  "endpoint": "https://api.coinigy.com/api/v1/",
  "api_exch_id": 7,
  "api_nickname": "My New Exchange Account"
}

conn = api.CoinigyREST(acct)

ticker = {
  "exchange_code": "BINA",
  "exchange_market": "ADA/BTC"
}

pair = ticker["exchange_market"]

#Here we connect to the api, you need to enter a valid period
def main(argv):
	i = 0
	prices = []
	parser = OptionParser()
	try :
		parser.add_option("-p", "--period", dest="periods")
		#parser.add_option("-h",  dest="help")
		(opts, args) = parser.parse_args(argv)
	except OptionParser.OptionError:
		print ("trading_bot.py parse_error")
		sys.exit(2)
	arg = float(opts.periods)
	if (arg in [1,10,60,300,900,1800,7200,14400,86400]):
		period = arg
	else:
		print ('Required periods in 1,10,60,300,900,1800,7200,14400, or 86400 second increments')
		sys.exit(2)
	macd = 0.
	while True:
		data = conn.request("ticker", query=ticker, json=False)				
		prices.append(float(data["bid"][0]))
		if len(prices) >= 30 : 
			(slow,fast,temp) = ind.macd(prices)
			print(str(datetime.datetime.now())+"\n Period: %ss \n Pair: %s \n Ask: %s \n Bid: %s \n Macd: %s" % (period,pair,data["ask"][0],data["bid"][0],temp))
			if temp*macd < 0:
				if temp > 0:
					print("BUY"+" \n Ancient macd: %s \n Nouveau macd: %s" % (macd,temp))
				else : 
					print("SELL"+" \n Ancient macd: %s \n Nouveau macd: %s" % (macd,temp))
			macd = temp
		print("\n next")
		time.sleep(period)

	#for dests in ["period"]:
	#	if dests == '-h':
	#		print ('trading-bot.py -p <period length> -c <currency pair> -n <period of moving average>')
	#		sys.exit()
	#	elif dest == "period":
	#		if (int(arg) in [300,900,1800,7200,14400,86400]):
	#			period = arg
	#		else:
	#			print ('Poloniex requires periods in 300,900,1800,7200,14400, or 86400 second increments')
	#			sys.exit(2)
	#	elif opt in ("-c", "--currency"):
	#	elif opt in ("-n", "--points"):
	#		lengthOfMA = int(arg)
	#	elif opt in ("-s"):
	#		startTime = arg
	#	elif opt in ("-e"):
	#		endTime = arg


if __name__ == "__main__":
	main(sys.argv[1:])
