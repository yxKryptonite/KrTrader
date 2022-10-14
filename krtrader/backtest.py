import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from models.lstm import LSTMModel
from data.load_data import StockDataset
from data.read_data import DataReader
import matplotlib.pyplot as plt
import yaml
import configargparse

def get_config():
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="config/stock_inference.yaml")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg

class BackTest():
    def __init__(self, cfg):
        # Load data
        data_reader = DataReader(cfg)
        data = data_reader.get_data()
        self.data = torch.from_numpy(data).float().reshape(len(data), 1)
        self.time = data_reader.get_time()

        # Load model
        self.model = eval(cfg["model"])()
        self.model.load_state_dict(torch.load(cfg["model_save_path"]))

    def inference(self):
        """Predict future prices"""
        self.model.eval()
        x, y = self.data[:-1, :], self.data[1:, :]
        y_pred = self.model(x)
        plt.plot(self.time, y_pred.detach().numpy(), label='pred')
        plt.plot(self.time, y.detach().numpy(), label='true')
        plt.legend()
        plt.show()

    def run(self):
        """Trading"""
        pass


def main():
    cfg = get_config()
    backtest = BackTest(cfg)
    backtest.inference()


if __name__ == "__main__":
    main()