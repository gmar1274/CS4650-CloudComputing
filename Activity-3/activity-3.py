"""
Gabriel Martinez
CS 4650
Actvity 3
This program reads all csv files from a specified directory and plots the six
different plots: line, bar, histogram, pie, scatter, and 3-D
"""
from pandas import DataFrame, Series
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

def readCSV(file):
    # reading csv file  
    return pd.read_csv(file)
def readDir(dir_path):
    dataframes=[]
    for filename in os.listdir(dir_path):
            if '.csv' in filename:
                file = os.path.join(dir_path,filename)
                dataframes.append(readCSV(file))
    return dataframes
dir_path="C:\\Users\\gnmar\\Desktop\\FALL-2019-HW\\CS4650-CloudComputing\\Dataset\\baseballdatabank-2019.2\\core\\Pitching.csv"
print("Reading dataset(s)...")
df = readCSV(dir_path)
dir_path = 'C:\\Users\\gnmar\\Desktop\\FALL-2019-HW\\CS4650-CloudComputing\\Activity-3'
print("Plotting data in six ways...")

df_subset = df.head(100)
df_subset.set_index('yearID',inplace=True)
df_subset.fillna(0, inplace=True)
#plot line
df_subset.plot.line()
plt.savefig( os.path.join(dir_path,'line-plot.png'))
#plot bar
ax = df_subset.plot.bar(x='teamID', y='W', rot=90)
plt.savefig( os.path.join(dir_path,'bar-plot.png'))
#plot hist
df_subset.plot.hist()
plt.savefig( os.path.join(dir_path,'hist-plot.png'))
#plot pie
df_subset.plot.pie(y='W')
plt.savefig( os.path.join(dir_path,'pie-plot.png'))
#plot scatter
df_subset.plot.scatter(x='W',y='L')
plt.savefig( os.path.join(dir_path,'scatter-plot.png'))
#3d scatter
ax = plt.figure().gca(projection='3d')
ax.scatter(df_subset.index, df_subset['W'], df_subset['L'])
ax.set_xlabel("index")
ax.set_ylabel("wins")
ax.set_zlabel("losses")
plt.savefig( os.path.join(dir_path,'3d-plot.png'))