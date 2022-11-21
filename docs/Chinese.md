# KrTrader: 一个简易的量化交易系统

![](assets/logo.png)

[English](index.md)

## 简介

一个基于 Python 的简易量化交易系统。（仍在开发中）

作为一名 CS 专业的大二学生，我之前从未系统地学习过任何金融知识（只学过一门通识课程）。基于我浅薄的知识，我在有限的股票池中开发了这个玩具交易系统，使用了简单的信号策略和一些基于机器学习的算法。

交易细节可能很肤浅和幼稚，但我致力于开发“模型包装策略”设计模式，这是该项目的核心。

## 特性
- [x] 模型包装策略
- [x] 回测
- [x] 模拟交易
- [x] 绘图
- [ ] 另类数据的爬取
- [ ] 自然语言处理
- [ ] 其他...

## 安装

```bash
git clone git@github.com:yxKryptonite/KrTrader.git
cd KrTrader
```

## 架构

- 交易
  - 数据读取
  - 策略
    - 模型
      - 训练
      - 验证/测试
    - 买卖信号
  - 绘图
- 数据分析
  - 数据抓取
  - 数据处理
  - 数据可视化

## 使用

提示：以下所有命令均在项目根目录下运行。

- 使用 `strategies` 交易
- 用 `strategies` 包装 `models`
  - 训练模型
    ```bash
    python3 krtrader/train.py --yaml config/stock_train.yaml
    ```
  - 验证/测试模型
    ```bash
    python3 krtrader/backtest.py --yaml config/stock_inference.yaml
    ```
- 其他
  
  详见 [tutorials](https://github.com/yxKryptonite/KrTrader/tree/master/krtrader/tutorials) 。

## 开源协议

[MIT](https://choosealicense.com/licenses/mit/)