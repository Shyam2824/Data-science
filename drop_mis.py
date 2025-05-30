# drop missing data in row or column
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



###########  DROP MISSING DATA IN ROW AND COLUMN

#remove column

# Drop the 'Variable_code' column
dataset.drop(columns=["Variable_code"], inplace=True)

# Check shape before dropping missing values
print("Shape before dropping missing values:", dataset.shape)

# Drop rows with any missing values
dataset.dropna(inplace=True)  # inplace=True avoids reassigning the variable

# Check for any remaining missing values
print("Missing values in each column:\n", dataset.isnull().sum())

# Check shape after dropping missing values
print("Shape after dropping missing values:", dataset.shape)

# Visualize missing values (should be empty after dropna)
sns.heatmap(dataset.isnull(), cbar=False, cmap='viridis')
plt.title("Heatmap of Missing Values")
plt.show()