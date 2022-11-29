import pandas as pd
import pandas_datareader as dr
import numpy as np
from tqdm import tqdm
import configargparse
import yaml

class DataReader():
    def __init__(self, cfg):
        if type(cfg["name"]) is not list:
            # This branch is not used anymore, only for insurance
            self.source_data = dr.data.get_data_yahoo(cfg["name"], start=cfg["start"], end=cfg["end"])[cfg["features"]]
        else:
            self.source_data = dr.data.get_data_yahoo(cfg["name"][0], start=cfg["start"], end=cfg["end"])[cfg["features"]]
            for name in cfg["name"][1:]:
                self.source_data = pd.concat([self.source_data, dr.data.get_data_yahoo(name, start=cfg["start"], end=cfg["end"])[cfg["features"]]], axis=1)
                
        self.data = self.source_data.values # (T,)
        self.name = cfg["name"]

    def get_data(self):
        return self.data

    def get_source_data(self):
        return self.source_data

    def get_time(self):
        return self.source_data.index[1:]

    def save(self, path, src=True):
        if src:
            self.source_data.to_csv(path)
        else:
            # np to csv
            np.save(path, self.data, allow_pickle=False)


if __name__ == "__main__":
    parser = configargparse.ArgumentParser()
    parser.add_argument("--yaml", type=str, default="config/stock_inference.yaml")
    args = parser.parse_args()
    with open(args.yaml, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    data_reader = DataReader(cfg)
    print(data_reader.get_time())