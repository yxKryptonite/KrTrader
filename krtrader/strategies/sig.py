import torch
import numpy as np
import pandas as pd
from strategies.base import BaseStrategy

class SignalStrategy(BaseStrategy):
    def __init__(self, cfg):
        super(SignalStrategy, self).__init__(cfg)
        self.prev_stock_price = {}


    def trade(self, stock_price):
        # stock_price: dict
        # stock_price = {"name": price}
        for key in stock_price.keys():
            if key not in self.prev_stock_price.keys():
                self.prev_stock_price[key] = stock_price[key]
            else:
                if stock_price[key] > self.prev_stock_price[key]:
                    self.buy(key, self.trade_num, stock_price[key])
                elif stock_price[key] < self.prev_stock_price[key]:
                    self.sell(key, self.trade_num, stock_price[key])
                self.prev_stock_price[key] = stock_price[key]


if __name__ == "__main__":
    import sys
    import yaml
    sys.path.append("..")
    from data.read_data import DataReader
    with open("../../config/trade0.yaml", "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    data_reader = DataReader(cfg)
    data = data_reader.get_source_data()
    data_reader.save("cache/data0.csv", src=True)
    # print(data_reader.name)
    # exit(0)

    strategy = SignalStrategy(10000, data_reader.get_time()[0], 100)
    trade_duration = 365 * 1
    net_worth = []
    time_series = []
    for i in range(trade_duration):
        strategy.time = data.index[i]
        data_slice = data.iloc[i]
        stock_price = {}
        for j in range(len(data_reader.name)):
            stock_price[data_reader.name[j]] = data_slice[j]

        strategy.trade(stock_price)
        print(f"{strategy.time} net worth: {strategy.get_net(stock_price)} asset: {strategy.asset} stock: {strategy.stock}")
        net_worth.append(strategy.get_net(stock_price))
        time_series.append(strategy.time)

    import matplotlib.pyplot as plt
    plt.plot(time_series, net_worth)
    plt.show()