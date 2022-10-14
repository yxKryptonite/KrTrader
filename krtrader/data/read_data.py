import pandas as pd
import pandas_datareader as dr
import numpy as np
from tqdm import tqdm
import configargparse
import yaml

class DataReader():
    def __init__(self, cfg):
        self.source_data = dr.data.get_data_yahoo(cfg["name"], start=cfg["start"], end=cfg["end"])
        self.data = self.source_data[cfg["features"]]
        self.data = self.data.values # (T,)

    def get_data(self):
        return self.data

    def get_time(self):
        return self.source_data.index[1:]

    def save(self, path, src=True):
        if src:
            self.source_data.to_csv(path)
        else:
            np.save(path, self.data)


if __name__ == "__main__":
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="config/stock_inference.yaml")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    data_reader = DataReader(cfg)
    print(data_reader.get_time())