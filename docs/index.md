# KrTrader: A Toy Quantitative Trading System

![](assets/logo.png)

## Introduction

A toy quantitative trading system based on Python. (still under development)

## Installation

```bash
git clone git@github.com:yxKryptonite/KrTrader.git
cd KrTrader
```

## Usage

- Train
  ```bash
  python3 krtrader/train.py --yaml config/stock_train.yaml
  ```
- Inference
  ```bash
  python3 krtrader/backtest.py --yaml config/stock_inference.yaml
  ```

## License

[MIT](https://choosealicense.com/licenses/mit/)