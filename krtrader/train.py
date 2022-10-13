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

cfg = get_config()

try:
    device = torch.device(cfg["device"])
except:
    device = torch.device("cpu")

# Load data
data = dr.data.get_data_yahoo(cfg.name, start=cfg.start, end=cfg.end)
data = data[cfg.features]
data = data.values # (T,)
dataset = StockDataset(data, cfg.window_size)
dataset = dataset.to(device)

strategy = LSTMStrategy()
strategy = strategy.to(device)
dataloader = DataLoader(dataset, batch_size=cfg.batch_size, shuffle=True)

num_epochs = cfg.epochs
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(strategy.parameters(), lr=cfg.learning_rate)

for epoch in tqdm(range(num_epochs)):
    for i, (x, y) in enumerate(dataloader):
        y_pred = strategy(x)
        loss = criterion(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch + 1) % 10 == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
        if cfg.save:
            torch.save(strategy.state_dict(), cfg.model_save_path)