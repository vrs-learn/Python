#
# BOKEH is a Data visualization Library
#
# pip install bokeh
# pip install bkcharts

# from bkcharts import Scatter

# Building a Scatter Plot

# Below are the graphs which we will be learning in this session :
#Line Graphs
#Plotter Graphs
#Time Series Graphs

# THere are 3 kind of interfaces to create a Bokeh plotting graph :
# bokeh.models  - low level
# bokeh.plotting - medium level
# bokeh.charts - high level

# 1 Scatter Plot :


########
# Time Series Plot :
########

# We will use below link to get the data from google finance of a stock, which we will use to plot a finance graph
# http://finance.google.com/finance/historical?cid=4112&startdate=Jan+1%2C+2009&enddate=Aug+2%2C+2012&num=30&ei=YhIzWsipFIqMjAH6m5TwDg&output=csv

from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_csv("http://finance.google.com/finance/historical?cid=4112&startdate=Jan+1%2C+2009&enddate=Aug+2%2C+2012&num=30&ei=YhIzWsipFIqMjAH6m5TwDg&output=csv",parse_dates=["Date"])
p = figure(width=500,height=250,x_axis_type="datetime",responsive=True)
p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)
output_file("TimeSeries.html")
show(p)
