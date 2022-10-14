import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from models.lstm import LSTMModel
from data.load_data import StockDataset
from data.read_data import DataReader
from tqdm import tqdm
import configargparse
import yaml

def get_config():
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="config/stock_train.yaml")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg

class Trainer():
    def __init__(self, cfg=None):
        if cfg is None:
            cfg = get_config()
            
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        # Load data
        data_reader = DataReader(cfg)
        data = data_reader.get_data()
        dataset = StockDataset(data, cfg["window_size"])

        self.model = eval(cfg["model"])()
        self.model = self.strategy.to(self.device)
        self.dataloader = DataLoader(dataset, batch_size=cfg["batch_size"], shuffle=True)

        self.num_epochs = cfg["epochs"]
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.strategy.parameters(), lr=cfg["learning_rate"])
        self.save = cfg["save"]
        self.model_save_path = cfg["model_save_path"]

    def train(self):
        for epoch in tqdm(range(self.num_epochs)):
            for i, (x, y) in enumerate(self.dataloader):
                x = x.to(self.device)
                y = y.to(self.device)
                y_pred = self.model(x)
                loss = self.criterion(y_pred, y)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                
            if (epoch + 1) % 10 == 0:
                print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, self.num_epochs, loss.item()))
                if self.save:
                    torch.save(self.model.state_dict(), self.model_save_path)


def main():
    cfg = get_config()
    trainer = Trainer(cfg)
    trainer.train()


if __name__ == "__main__":
    main()