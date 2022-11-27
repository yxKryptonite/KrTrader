import torch
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from logging import getLogger


class BaseStrategy(object):
    def __init__(self, cfg):
        super(BaseStrategy, self).__init__()
        self.asset = cfg["init_asset"]
        self.time = cfg["start"]
        self.trade_num = cfg["trade_num"]
        self.stock = {}
        self.net_worth = []
        self.stamp = cfg["stamp"]
        self.logger = getLogger(__name__)
        self.logger.setLevel("INFO")

    def __call__(self):
        pass

    def __str__(self):
        return f"Strategy Info --- asset: {self.asset}, stock: {self.stock}"

    def __repr__(self):
        return self.__str__()

    def visualize(self):
        pass

    def log(self, time, name, num, price, mode="buy", done=True):
        log_file = open(f"../logs/{self.stamp}.log", "a")
        sys.stdout = log_file
        if done:
            if mode == "sell":
                self.logger.info(f"{time} --> sell {num} {name} at {price}")
            elif mode == "buy":
                self.logger.info(f"{time} --> buy {num} {name} at {price}")
        else:
            if mode == "sell":
                self.logger.info(f"{time} --> no {name} stock to sell")
            elif mode == "buy":
                self.logger.info(f"{time} --> no enough money to buy {name}")
        
        sys.stdout = sys.__stdout__
        log_file.close()
        

    def sell(self, name, num, price):
        for key in self.stock.keys():
            if key == name and self.stock[key] >= num:
                self.asset += num * price
                self.stock[key] -= num
                self.log(self.time, name, num, price, mode="sell", done=True)
                return

        self.log(self.time, name, num, price, mode="sell", done=False)

    def buy(self, name, num, price):
        if self.asset >= num * price:
            self.asset -= num * price
            if name in self.stock.keys():
                self.stock[name] += num
            else:
                self.stock[name] = num
            self.log(self.time, name, num, price, mode="buy", done=True)
        else:
            self.log(self.time, name, num, price, mode="buy", done=False)

    def trade(self, stock_price):
        '''depending on specific strategy'''
        pass

    def get_net(self, stock_price):
        # stock_price: dict
        # stock_price = {"name": price}
        net = self.asset
        for key in self.stock.keys():
            net += self.stock[key] * stock_price[key]
        return net

    
    def plot(self):
        plt.plot(self.time, self.net_worth)
        plt.show()