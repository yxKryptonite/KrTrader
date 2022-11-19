# Add the parent directory to the path
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parentdir) 

from models.lstm import LSTMModel
from data.read_data import DataReader
from strategies.base import BaseStrategy

class LSTMStrategy(BaseStrategy):
    def __init__(self, init_asset, init_time, trade_num, cfg):
        super(LSTMStrategy, self).__init__(init_asset, init_time)
        self.models = [] # list of LSTMModels
        self.num = 100
        self.thres = 0.1


    def trade(self, stock_price):
        # stock_price: dict
        # stock_price = {"name": price}
        for idx, model in enumerate(self.models):
            output = model(stock_price[idx])
            if output > stock_price[idx]["close"] * (1 + self.thres):
                self.buy(stock_price[idx]["name"], self.num, stock_price[idx]["close"])
            elif output < stock_price[idx]["close"] * (1 - self.thres):
                self.sell(stock_price[idx]["name"], self.num, stock_price[idx]["close"])
            


if __name__ == "__main__":
    print("test")