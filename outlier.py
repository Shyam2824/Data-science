# outlier
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset= pd.read_csv(r"C:\Users\HP\OneDrive\Documents\dataset.csv")
dataset.head(4)
dataset.describe()
plt.figure(figsize =  (10,5))
sns.boxplot(x="Value", data=dataset)
plt.show()
dataset.shape
q1 = dataset["Value"].quantile(0.25)
q3 = dataset["Value"].quantile(0.75)
q1
q3
IQR =  q3- q1

min_range = q1 - (1.5*IQR)
max_range = q3 + (1.5*IQR)
min_range , max_range

new_dataset = dataset[dataset["Value"]<= max_range] #remove outlier
new_dataset.shape
sns.boxplot(x="Value", data=new_dataset)
plt.show()
sns.distplot(dataset["Value"])

min_range1= dataset["Value"].mean() - (3*dataset["Value"].std())
max_range1= dataset["Value"].mean() + (3*dataset["Value"].std())

min_range1,max_range1
z_score= (dataset["Value"]-dataset["Value"].mean())/(dataset["Value"].std())
dataset["z_score"] = z_score
dataset[dataset["z_score"]<3]