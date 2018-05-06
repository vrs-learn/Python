# This program is to collect the values of a stock and its open, previous close , current price  from NSE India (www.nseindia.com)
#

""" Steps to be performed for extracting the data .

1. Create the URL for the Stock to be searched  
2. using Beautiful Soup extract the div item with ID as soup.select("div#responseDiv")[0].string
3. remove the extra spaces , tabs by first splitting the entire content into list by using split() and then joining it with join()
4. Use json.loads() to convert the string into the Dictionary 
5. extract the dictionary value for the "data" keys
6. again convert the output into dictionary and extract the values for 


"""

#page = requests.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=PNB&illiquid=0&smeFlag=0&itpFlag=0")
#tree = html.fromstring(page.content)
#curr_price = tree.xpath('//ul[@class="stock"]//span[@id="previousClose"]/text()')
#curr_price = tree.xpath('//span[@id="previousClose"]/text()')
#print(curr_price)

def get_prices(stock):
	url_link = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock + "&illiquid=0&smeFlag=0&itpFlag=0"
	#url = requests.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=PNB&illiquid=0&smeFlag=0&itpFlag=0")
	url = requests.get(url_link)
	url_text = url.text
	soup = BeautifulSoup(url_text, "lxml")
	values = soup.select("div#responseDiv")[0].string
	values = ''.join(values.split())

	values_json = json.loads(values)
	values_data = values_json["data"][0]

	#print(type(values_data))
	#print(values_data["lastPrice"])

	curr_price = values_data["lastPrice"]
	prev_close = values_data["previousClose"]
	open_price = values_data["open"]
	symbol = values_data["symbol"]

	print("Prices of : " + symbol + "\n"\
	"Current Price : " + curr_price + "\n" + \
	"Previous Close : " + prev_close + "\n" + \
	"Open Price : " + open_price + "\n" + \
	"Close Price : " + prev_close + "\n")


from lxml import html
import requests
from bs4 import BeautifulSoup
import json

list_of_stocks = ["PNB" , "SBIN", "CENTRALBK", "HDFCBANK", "ICICIBANK", "BANKINDIA" , "INDIANB" , "KOTAKBANK", "BANKBARODA"]

for stock in list_of_stocks:
	get_prices(stock)