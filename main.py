import pandas as pd
import matplotlib.pyplot as plt
from read_dataset import read_data

# import dataset
datapath='data/'
year='2019'
month='02'
option='Cash'
currency1='USD'
currency2='NTD'
read_data(datapath, year, month, option, currency1, currency2)
