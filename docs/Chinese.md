# KrTrader: 一个简易的量化交易系统

![](assets/logo.png)

[English](index.md)

## 简介

一个基于 Python 的简易量化交易系统。（开发中）

作为一名 CS 专业的大二学生，除了一门通识课程外，我之前从未系统地学习过任何金融知识。基于我浅薄的知识，我在有限的股票池中开发了这个简易的交易系统，使用了简单的信号策略和一些基于机器学习的算法。

交易细节可能很肤浅或不完备，但我致力于开发“模型包装策略”设计模式，这是该项目的核心。

## 特性
- [x] 模型包装策略
  
  👉 你可以通过将模型包装到策略类中，基于 [BaseStrategy](https://github.com/yxKryptonite/KrTrader/blob/master/krtrader/strategies/base.py) 模板轻松设计自己的策略。
- [x] 基于机器学习的算法 
  
  👉 你可以使用 PyTorch ，基于 [BaseModel](https://github.com/yxKryptonite/KrTrader/blob/master/krtrader/models/base.py) 模板设计自己的模型。
- [x] 模拟交易 & 回测
  
  👉 无需赘述
- [x] 统一的配置框架
  
  👉 你可以使用统一的配置文件来配置各种任务，包括训练、推理、回测... 请参阅 [template.yaml](https://github.com/yxKryptonite/KrTrader/blob/master/config/template.yaml) 。
- [x] 绘图功能
  
  👉 基于 [Matplotlib](https://matplotlib.org/) ，你可以绘制各种图表，包括股票价格、资金曲线、策略收益曲线、模型预测曲线...
- [x] 另类数据的爬取
  
  👉 基于 [Selenium](https://selenium-python.readthedocs.io/) ，你可以爬取各种另类数据，包括新闻、社交媒体、财务数据...
- [x] 自然语言处理
  
  👉 基于 [BERT](https://arxiv.org/abs/1810.04805) ，你可以使用自然语言处理技术来提取新闻的特征，以便于预测股票价格。
- [ ] 其他...

## 开始

首先，请参考[这里](https://github.com/yxKryptonite/KrTrader#preparations)进行一些必要的准备工作。

然后运行以下的命令将仓库克隆到本地：

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
  ```bash
  python3 krtrader/strategies/sig.py --yaml config/trade0.yaml
  ```
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