import torch
import numpy as np
import pandas as pd

class BaseStrategy(object):
    def __init__(self, init_asset, init_time):
        super(BaseStrategy, self).__init__()
        self.asset = init_asset
        self.time = init_time
        self.stock = {}

    def __call__(self):
        pass

    def __str__(self):
        return f"asset: {self.asset}, stock: {self.stock}"

    def visualize(self):
        pass

    def sell(self, name, num, price):
        for key in self.stock.keys():
            if key == name and self.stock[key] >= num:
                self.asset += num * price
                self.stock[key] -= num
                print(f"{self.time} --> sell {num} {name} at {price}")
                return

        print(f"{self.time} --> no {name} stock to sell")

    def buy(self, name, num, price):
        if self.asset >= num * price:
            self.asset -= num * price
            if name in self.stock.keys():
                self.stock[name] += num
            else:
                self.stock[name] = num
            print(f"{self.time} --> buy {num} {name} at {price}")
        else:
            print(f"{self.time} --> no enough money to buy {name}")

    def trade(self, stock_price):
        pass

    def get_net(self, stock_price):
        # stock_price: dict
        # stock_price = {"name": price}
        net = self.asset
        for key in self.stock.keys():
            net += self.stock[key] * stock_price[key]
        return net