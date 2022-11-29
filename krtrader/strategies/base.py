import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import logging
from logging import getLogger


class BaseStrategy(object):
    def __init__(self, cfg):
        super(BaseStrategy, self).__init__()
        self.asset = cfg["init_asset"]
        self.time = cfg["start"]
        self.trade_num = cfg["trade_num"]
        self.stock = {}
        self.net_worth = []
        self.log_stamp = cfg["log_stamp"]
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

    def log(self, data, mode, done=True):
        logging.basicConfig(filename = f"{ROOT_DIR}/krtrader/logs/{self.log_stamp}.log",
                            filemode = "w",
                            level = logging.INFO)
        if mode == "sell":
            if done:
                self.logger.info(f"{data['time']} --> sell {data['num']} {data['name']} at {data['price']}")
            else:
                self.logger.info(f"{data['time']} --> no {data['name']} stock to sell")

        elif mode == "buy":
            if done:
                self.logger.info(f"{data['time']} --> buy {data['num']} {data['name']} at {data['price']}")
            else:
                self.logger.info(f"{data['time']} --> no enough money to buy {data['name']}")
            
        elif mode == "net":
            self.logger.info(f"{data['time']} net worth: {data['net']} asset: {data['asset']} stock: {data['stock']}")
        

    def sell(self, name, num, price):
        for key in self.stock.keys():
            if key == name and self.stock[key] >= num:
                self.asset += num * price
                self.stock[key] -= num
                self.log({"time": self.time, "name": name, "num": num, "price": price}, 
                        mode="sell", 
                        done=True)
                return

        self.log({"time": self.time, "name": name, "num": num, "price": price}, 
                mode="sell", 
                done=False)

    def buy(self, name, num, price):
        if self.asset >= num * price:
            self.asset -= num * price
            if name in self.stock.keys():
                self.stock[name] += num
            else:
                self.stock[name] = num
            self.log({"time": self.time, "name": name, "num": num, "price": price},
                    mode="buy",
                    done=True)
                
        else:
            self.log({"time": self.time, "name": name, "num": num, "price": price},
                    mode="buy",
                    done=False)

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

    
    def plot(self, time, net_worth):
        plt.plot(time, net_worth)
        plt.xlabel("Time")
        plt.ylabel("Net Worth")
        plt.show()