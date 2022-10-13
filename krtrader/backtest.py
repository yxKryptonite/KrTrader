import pandas as pd
import pandas_datareader as dr
import numpy as np
import torch
import models

# Load data
data = dr.data.get_data_yahoo('AAPL', start='2010-01-01', end='2020-01-01')
data = data[['Close']]
data = data.values
data = data.astype('float32')
data = data.reshape(-1, 1)
# data = data / data.max(axis=0)
# data = data.tolist()
# data = pd.DataFrame(data)

# Load model

if __name__ == "__main__":
    print(type(data))