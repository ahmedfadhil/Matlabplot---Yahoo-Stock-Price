import matplotlib.pyplot as plt
import urllib
import matplotlib.dates as mdates
import numpy as np


def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    splite_source = source_code.splite('\n')

    for line in splite_source:
        splite_line = line.splite(',')
        if len(splite_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True,
                                                                      converters={
                                                                          0: bytespdate2num('%Y%m%d')
                                                                      })

    plt.title("This is a title")
    plt.xlabel("This is x")
    plt.ylabel("This is y")
    plt.legend()
    plt.show()

    graph_data('TSLA')
