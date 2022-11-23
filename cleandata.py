import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import StandardScaler

df1 = pd.read_csv('Domain1_csv/Subject1-0-1.csv')
df2 = pd.read_csv('Domain1_csv/Subject1-0-2.csv')
df3 = pd.read_csv('Domain1_csv/Subject1-0-3.csv')


def standarization(data):
    scaler = StandardScaler()
    data.iloc[:, 0:-3] = scaler.fit_transform(data.iloc[:, 0:-3])
    return data

standarization(df1.iloc[:,1])
