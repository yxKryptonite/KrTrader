import torch
import numpy as np
import pandas as pd

class BaseStrategy(object):
    def __init__(self):
        super(BaseStrategy, self).__init__()
        pass

    def trade(self):
        pass

    def __call__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def visualize(self):
        pass