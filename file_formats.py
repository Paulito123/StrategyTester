from __future__ import (absolute_import, division, print_function, unicode_literals)
import backtrader as bt
import datetime


class alpha_vantage_csv(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d %H:%M:%S'),
        ('nullvalue', 0.0),
        ('reverse', False),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
        ('timeframe', bt.TimeFrame.Minutes),
        ('compression', 60),
    )

class finnhub_csv(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d %H:%M:%S'),
        ('nullvalue', 0.0),
        ('reverse', False),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
    )