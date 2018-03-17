import datetime
import numpy as np


#Implementation of MACD and RSI


def moving_average(x, n=9, type='simple'):
    """
    compute an n period moving average.
    type is 'simple' | 'exponential'
    """
    x = np.asarray(x)
    if type == 'simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))
    weights /= weights.sum()
    a = np.dot(x[-n:],weights).sum()
    return a


def relative_strength(prices, n=14):
    """
    compute the n period relative strength indicator
    http://stockcharts.com/school/doku.php?id=chart_school:glossary_r#relativestrengthindex
    http://www.investopedia.com/terms/r/rsi.asp
    """
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed >= 0].sum()/n
    down = -seed[seed < 0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1. + rs)
    for i in range(n, len(prices)):
        delta = deltas[i - 1]  # cause the diff is 1 shorter
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up*(n - 1) + upval)/n
        down = (down*(n - 1) + downval)/n
        rs = up/down
        rsi[i] = 100. - 100./(1. + rs)
    return rsi[-1]

def relative_strength_update(prices, , deltas, n=14): 
    l=len(prices)
    deltas[l-1]=prices[l-1]-prices[l-2]
    delta = deltas[-n:]
    up = delta[delta >= 0].sum()/n
    down = -delta[delta < 0].sum()/n
    rs = up/down
    
    return rsi
def macd(x, nslow=26, nfast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    emaslow = moving_average(x, n=nslow, type='exponential')
    emafast = moving_average(x, n=nfast, type='exponential')
    return emaslow, emafast, emafast - emaslow



