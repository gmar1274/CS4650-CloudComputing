"""
Gabriel Martinez
CS 4650
Actvity 2
This program reads all csv files from a specified directory and
performs the tasks required for activity 2. 
"""
from pandas import DataFrame, Series
import pandas as pd
import os
import matplotlib.pyplot as plt
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
dir_path="C:\\Users\\gnmar\\Desktop\\FALL-2019-HW\\CS4650-CloudComputing\\Dataset\\baseballdatabank-2019.2\\core"
print("1) Reading dataset(s)...")
data_frames = readDir(dir_path)
print("2) Displaying the first 50 rows...")
for df in data_frames:
    print(df.head(50))
print("3) Displaying statistical summary...")
for df in data_frames:
    print(df.describe())
print("4) Selecting a subset of rows...")
for df in data_frames:
    print(df[10:40].head(10))
print("5) Selecting a subset of columns...")
for df in data_frames:
    print(df.iloc[:,0:2].head(10))    
print("6) Filtering out the empty data...")
for df in data_frames:
    print(df.dropna(axis = 0, how ='any').head(50))
print("7) Displaying the rows with missing data...")
for df in data_frames:
    print(df[df.isnull().any(axis=1)].head(10))
print("8) Manipulating the data")
for df in data_frames:
    print("Original: ")
    print(df.head(10))
    try: 
        df.iloc[:,2] +=  100
    except:
        df.iloc[:,2] +=  "100"
    print("After: ")
    print(df.head(10))
#evertthing works so far...
print("9) Sorting data from (8) in descending order...")
for df in data_frames:
    col_name = df.columns[2]
    df.sort_values(by=col_name, ascending=False,na_position='first',inplace=True)
    print(df.head(10))
print("10) Grouping data from (9) by category... ")
for df in data_frames:
    col_name = df.columns[2]
    gb = df.groupby(col_name)
    print(gb.first())
def myPlot(i,df):
    df_subset = df.select_dtypes(include=["float", 'int'])
    df_subset.fillna(0, inplace=True)
    if(len(df_subset.columns)<2):
        print("dataset:{} doesn\'t have any numeric columns. {}".format(i,df_subset.head(1)))
        return
    df_subset = df_subset.head(50)
    x_col = df_subset.columns[0]
    y_col = df_subset.columns[1]
    df_subset.plot(x =x_col, y=y_col, kind = 'scatter')
    plt.savefig('scatter-plot-{}.png'.format(i))
    df_subset.plot(x =x_col, y=y_col, kind = 'line')
    plt.savefig('line-plot-{}.png'.format(i))
    df_subset.plot(x =x_col, y=y_col, kind = 'bar')
    plt.savefig('bar-plot-{}.png'.format(i))
print("11) (Optinal) Plotting data in three ways: scatter,line, and bar: ...")
for i, df in enumerate(data_frames): 
    myPlot(i,df)
