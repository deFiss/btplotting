import datetime

import backtrader as bt

from btplotting import BacktraderPlottingLive
from btplotting.schemes import Blackly

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    data = bt.feeds.YahooFinanceCSVData(
        dataname="datas/orcl-1995-2014.txt",
        fromdate=datetime.datetime(2000, 1, 1),
        todate=datetime.datetime(2001, 2, 28),
        reverse=False,
        swapcloses=True,
    )
    cerebro.adddata(data)
    data1 = cerebro.resampledata(data, timeframe=bt.TimeFrame.Weeks, compression=1)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio)

    cerebro.addanalyzer(BacktraderPlottingLive, volume=False, scheme=Blackly(
        hovertool_timeformat='%F %R:%S'), lookback=120, port=1234)

    cerebro.run()
    cerebro.plot()

