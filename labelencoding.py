import pandas as pd
df=pd.DataFrame({"name":["Shyam","cow","dog","elephant","black"]})
df

from sklearn.preprocessing import LabelEncoder
df
dataset= pd.read_csv(r"C:\Users\HP\OneDrive\Documents\dataset.csv")
dataset.head(4) # r - raw string 
la = LabelEncoder()
le = LabelEncoder()
df["en_name"] = le.fit_transform(df["name"])
#fit = that train the label when u convert then transform it , that is used when the model is build or deployed
la.fit(dataset["Variable_category"])

la.transform(dataset["Variable_category"])
dataset["Variable_category"].unique()
dataset["Variable_category"]= la.transform(dataset["Variable_category"])
