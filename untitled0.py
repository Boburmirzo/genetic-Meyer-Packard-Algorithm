# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:58:56 2018

@author: bumurzokov
"""

from bs4 import BeautifulSoup as bs
import urllib.request  as urllib2 

def get_historical_data(name, number_of_days):
	data = []
	url = "https://finance.yahoo.com/quote/" + name + "/history/"
	rows = bs(urllib2.urlopen(url).read(), "lxml").findAll('table')[0].tbody.findAll('tr')

	for each_row in rows:
		divs = each_row.findAll('td')
		if divs[1].span  != 'Dividend': #Ignore this row in the table
			#I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
			data.append({'Date': divs[0].span.text, 'Adj close': float(divs[1].span.text.replace(',',''))})

	return data[:number_of_days]

#Test
print (get_historical_data('amzn', 15))