import torch
import numpy as np
import pandas as pd
from strategies.base import BaseStrategy

class SignalStrategy(BaseStrategy):
    def __init__(self):
        super(SignalStrategy, self).__init__()
        self.buy = []
        self.sell = []

    def __call__(self, now, prev):
        """momentum"""
        return now > prev

    def trade(self, result):
        self.buy.append(result)
        self.sell.append(not result)
        return self.buy, self.sell