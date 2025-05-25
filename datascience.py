import pandas as pd
dataset= pd.read_csv(r"C:\Users\HP\OneDrive\Documents\dataset.csv")
dataset.head(3)
dataset.shape #that represent total number of row and column
dataset.isnull().sum().sum() # .sum().sum() represent total false value
dataset.notnull.sum().sum() # that find not null cell
(dataset.isnull().sum().sum()/(dataset.shape[0]*dataset.shape[1]))*100 # overall dataset percentage
dataset.isnull().sum() # represent the value
dataset.isnull().sum()/dataset.shape[0] #total number of percenntage