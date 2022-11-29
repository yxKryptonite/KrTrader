import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_data(driver, mode="XPATH", selector=None):
    data = driver.find_elements(eval(f"By.{mode}"), selector)
    return data # list


if __name__ == "__main__":
    '''Just a simple example of how to crawl data, you can crawl your own!'''
    ticker = "AMZN" # you can change the ticker
    url = f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}"
    driver = get_driver(url)
    table = get_data(driver, mode="XPATH", selector="//*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section")
    print(table[0].text)
    driver.close()
