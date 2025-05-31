#encoding data using the one hot variable and dummies variable
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data-science/dataset.csv")
print(dataset.head(3))


dataset.isnull().sum()
dataset["Value"].fillna(dataset["Value"].mode()[0],inplace=True) # fill the missing data
dataset.isnull().sum()

en_data=dataset[["Value","Gender"]]
en_data
pd.get_dummies(en_data) # encoding for dummies data that see to dummies formate
pd.get_dummies(en_data).info() # that use to see the binary form

############ One hot encoder
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop="first") #ohe is objecet
ar=ohe.fit_transform(en_data).toarray() #that check the data and fit to change
ar

pd.DataFrame(ar,columns=["Gender_female","Gender_male"])