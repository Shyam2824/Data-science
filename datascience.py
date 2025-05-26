import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data-science/dataset.csv")
print(dataset.head(3))

print("Shape:", dataset.shape)
print("Total Missing Values:", dataset.isnull().sum().sum())
print("Total Non-Missing Values:", dataset.notnull().sum().sum())
print("Missing Percentage:", (dataset.isnull().sum().sum()/(dataset.shape[0]*dataset.shape[1]))*100)

print("Missing values per column:")
print(dataset.isnull().sum())

print("Missing percentage per column:")
print(dataset.isnull().sum()/dataset.shape[0])

# Show heatmap
sns.heatmap(dataset.isnull())
plt.show()
