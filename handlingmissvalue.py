# Handling missing data in row or column
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data-science/dataset.csv")
print(dataset.head(3))


# Check the shape of the dataset
print("Dataset shape:", dataset.shape)

# Check the number of missing values in each column
print("Missing values per column:\n", dataset.isnull().sum())

# Fill missing values with a constant (e.g., 100)
dataset_filled_100 = dataset.fillna(100)

# Fill missing values using backward fill (next valid value)
dataset_bfill = dataset.fillna(method="bfill")

# Fill missing values across columns using forward fill
dataset_ffill_axis1 = dataset.fillna(method="ffill", axis=1)

# Check dataset info after fill operations
print("\nDataset Info:")
dataset.info()

# Fill missing values in 'Variable_code' column with its mode
mode_value = dataset["Variable_code"].mode()[0]
dataset["Variable_code"] = dataset["Variable_code"].fillna(mode_value)

# Check missing values only in object (categorical) columns
missing_objects = dataset.select_dtypes(include="object").isnull().sum()
print("\nMissing values in object columns:\n", missing_objects)