from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from matplotlib.pylab import rcParams
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

rcParams['figure.figsize'] = 20, 10


df = pd.read_csv("NSE-TATA.csv")
df.head()
