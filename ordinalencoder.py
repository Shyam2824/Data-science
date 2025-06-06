# ordinal encoder

import pandas as pd
df= pd.DataFrame({"size":["s","m","l","xl","xxl","s","m","l","s","s","xl","m","l"]})
df.head(3)

ord_data= [["s","m","l","xl","xxl"]]

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(categories=ord_data)
oe.fit(df[["size"]])

df["size_en"] = oe.transform(df[["size"]])
ord_data1= {"s":0,"m":1,"l":2,"xl":3,"xxl":4}
df["size_en_map"] = df["size"].map(ord_data1)
df
