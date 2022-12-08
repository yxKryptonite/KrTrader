# KrTrader: A Toy Quantitative Trading System

![](assets/logo.png)

[中文](Chinese.md)

## Introduction

A toy quantitative trading system based on Python.

As a sophomore student majoring in CS, I've never systematically learnt financial knowledge before (except for one general course). So based on my shallow knowledge, I developed this toy trading system **from scratch** within limited stock pool, using simple signal strategies and some machine learning based algorithms (which is my strength).

The trading details may be primitive or imperfect, but I'm dedicated to the development of the `model-wrapped strategies` designing patterns, which is the core of this project.

## Features
- [x] Model-wrapped strategies
  
  👉 You can easily design your own strategies based on a [BaseStrategy](https://github.com/yxKryptonite/KrTrader/blob/master/krtrader/strategies/base.py) template by wrapping your model into a strategy class.
- [x] Machine learning based algorithms
  
  👉 You can design your models for trading based on a [BaseModel](https://github.com/yxKryptonite/KrTrader/blob/master/krtrader/models/base.py) template, using PyTorch.
- [x] Simulated trading & backtesting
  
  👉 No explanation needed!
- [x] Unified configuration frameworks
  
  👉 You can use a unified configuration for all tasks in this project, including training, inferencing, backtesting... see [template.yaml](https://github.com/yxKryptonite/KrTrader/blob/master/config/template.yaml) for more details.
- [x] Nice plotting
  
  👉 Based on [Matplotlib](https://matplotlib.org/), you can plot the trading details in a nice way.
- [x] Crawling of alternative data
  
  👉 Based on [Selenium](https://selenium-python.readthedocs.io), you can crawl alternative data from yahoo finance, sina finance, etc.
- [x] Natural language processing
  
  👉 Based on [BERT](https://arxiv.org/abs/1810.04805), you can extract features from the news for stock predictions.
- [ ] To be continued...

## Getting Started

```bash
git clone git@github.com:yxKryptonite/KrTrader.git
cd KrTrader
```

## Dependencies

- [Python3](https://www.python.org/downloads/)
- [pip3](https://pip.pypa.io/en/stable/installation/)
- [PyTorch](https://pytorch.org/get-started/locally/)
- Required packages
  ```bash
  pip3 install -r requirements.txt
  ```
- If you're in mainland China, please get a stable VPN to access data.

## Architecture

- Trade
  - Data reading
  - Strategies
    - Models
      - Train
      - Inference
    - Buy & Sell signals
  - Plotting
- Data analysis
  - Data Crawling
  - Data processing
  - Visualization

## Usage

Tip: all the following commands are run in the root directory of the project.

- Trade using `strategies`
  ```bash
  python3 krtrader/strategies/sig.py --yaml config/trade0.yaml
  ```
- Wrapping `models` with `strategies`
  - Train models
    ```bash
    python3 krtrader/train.py --yaml config/stock_train.yaml
    ```
  - Inference models
    ```bash
    python3 krtrader/backtest.py --yaml config/stock_inference.yaml
    ```
- Others
  
  See [tutorials](https://github.com/yxKryptonite/KrTrader/tree/master/krtrader/tutorials) for more details.

## License

[MIT](https://github.com/yxKryptonite/KrTrader/blob/master/LICENSE)