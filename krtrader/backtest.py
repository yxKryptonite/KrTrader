import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from models.lstm import LSTMModel
from data.load_data import StockDataset
from data.read_data import DataReader
import matplotlib.pyplot as plt
import yaml
import sys
import configargparse
from strategies.sig import SignalStrategy

YEAR_DAYS = 365

def get_config():
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="config/stock_inference.yaml")
    parser.add_argument("--mode", type=str, default="inference")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg, args


class BackTest():
    def __init__(self, cfg=None):
        if cfg is None:
            self.cfg = get_config()
        else:
            self.cfg = cfg

        # Load data
        data_reader = DataReader(cfg)
        data = data_reader.get_data()
        self.data = torch.from_numpy(data).float().reshape(len(data), 1)
        self.time = data_reader.get_time()
        self.net_worth = None

        # Load model
        self.model = eval(cfg["model"])(cfg)
        self.model.load_state_dict(torch.load(cfg["model_save_path"]))

        # Load Strategy
        self.strategy = eval(cfg["strategy"])(cfg)


    @torch.no_grad()
    def inference(self):
        """Predict future prices"""
        self.model.eval()
        x, y = self.data[:-1, :], self.data[1:, :]
        y_pred = self.model(x)
        self.gt = y
        self.pred = y_pred


    @torch.no_grad()
    def run(self, init_asset, trade_num=100, num_years=1):
        """Trading"""
        with open("config/trade0.yaml", "r") as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)

        data_reader = DataReader(cfg)
        data = data_reader.get_source_data()
        data_reader.save("strategies/cache/data0.csv", src=True)
        # print(data_reader.name)
        # exit(0)

        strategy = SignalStrategy(init_asset, data_reader.get_time()[0], trade_num)
        trade_duration = YEAR_DAYS * num_years
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

        self.time = time_series
        self.net_worth = net_worth


    def plot(self, mode=None):
        if mode == "inference":
            plt.plot(self.time, self.pred.detach().numpy(), label='pred')
            plt.plot(self.time, self.gt.detach().numpy(), label='true')
            plt.legend()
            plt.show()
        elif mode == "trade":
            plt.plot(self.time_series, self.net_worth)
            plt.show()


def main():
    cfg, args = get_config()
    backtest = BackTest(cfg)
    if args.mode == "inference":
        backtest.inference()
        backtest.plot(mode="inference")
    elif args.mode == "trade":
        backtest.run(100000, trade_num=100, num_years=1)
        backtest.plot(mode="trade")


if __name__ == "__main__":
    main()