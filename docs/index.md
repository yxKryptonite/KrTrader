# KrTrader: A Toy Quantitative Trading System

![](assets/logo.png)

[中文文档](Chinese.md)

## Introduction

A toy quantitative trading system based on Python. (still under development)

As a sophomore student majoring in CS, I've never systematically learnt any financial knowledge before (only with one general course). So based on my shallow knowledge, I developed this toy trading system within limited stock pool, using simple signal strategies and some machine learning based algorithms (which is my strength).

The trading details may be shallow and childish, but I'm dedicated to the development of the `model-wrapped strategies` designing patterns, which is the core of this project.

## Features
- [x] Model-wrapped strategies
- [x] Backtesting
- [x] Simulated trading
- [x] Nice plotting
- [ ] Maybe some crawling of alternative data
- [ ] Natural language processing
- [ ] To be continued...

## Installation

```bash
git clone git@github.com:yxKryptonite/KrTrader.git
cd KrTrader
```

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
  See [`tutorials`](https://github.com/yxKryptonite/KrTrader/tree/master/krtrader/tutorials) for more details.

## License

[MIT](https://choosealicense.com/licenses/mit/)