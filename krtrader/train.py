import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from models.lstm import LSTMStrategy
from data.dataset import StockDataset
from tqdm import tqdm
import configargparse
import yaml

def get_config():
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="../config/stock.yaml")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg

class Trainer():
    def __init__(self, cfg=None):
        if cfg is None:
            cfg = get_config()
            
        try:
            self.device = torch.device(cfg["device"])
        except:
            self.device = torch.device("cpu")

        # Load data
        data = dr.data.get_data_yahoo(cfg["name"], start=cfg["start"], end=cfg["end"])
        data = data[cfg["features"]]
        data = data.values # (T,)

        self.dataset = StockDataset(data, cfg["window_size"])
        self.dataset = self.dataset.to(self.device)

        self.strategy = LSTMStrategy()
        self.strategy = self.strategy.to(self.device)
        self.dataloader = DataLoader(self.dataset, batch_size=cfg["batch_size"], shuffle=True)

        self.num_epochs = cfg["epochs"]
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.strategy.parameters(), lr=cfg["learning_rate"])
        self.save = cfg["save"]
        self.model_save_path = cfg["model_save_path"]

    def train(self):
        for epoch in tqdm(range(self.num_epochs)):
            for i, (x, y) in enumerate(self.dataloader):
                y_pred = self.strategy(x)
                loss = self.criterion(y_pred, y)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                
            if (epoch + 1) % 10 == 0:
                print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, self.num_epochs, loss.item()))
                if self.save:
                    torch.save(self.strategy.state_dict(), self.model_save_path)