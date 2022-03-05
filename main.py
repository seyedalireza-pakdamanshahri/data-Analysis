import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
import datetime as dt
from sklearn.preprocessing import MinMaxScaler , LabelEncoder
from tensorflow.keras.models import Sequential , Model
from tensorflow.keras.layers import Dense , LSTM , Dropout , Input , concatenate
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import LinearRegression , cross_val_score


crypto_currency = ['BTC','ETH','XRP','LTC','BTT','BAT']
def prediction():
  print("Hello World")
  
  
prediction()


def reading_csv():
  df = pd.read_csv('data.csv')



