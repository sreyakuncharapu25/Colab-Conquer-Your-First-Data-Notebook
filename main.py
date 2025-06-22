import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from local file
df = pd.read_csv("dataset.csv")

# Basic Info
print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Info:")
df.info()

print("\n🔹 Columns:")
print(df.columns.tolist())

print("\n🔹 Mean:\n", df.mean(numeric_only=True))
print("\n🔹 Median:\n", df.median(numeric_only=True))
print("\n🔹 Std Dev:\n", df.std(numeric_only=True))
print("\n🔹 Describe:\n", df.describe())

# Missing values
print("\n🔹 Missing values:\n", df.isnull().sum())

# Plot histograms
print("\n🔹 Plotting histograms...")
df.hist(figsize=(15, 10), bins=20, edgecolor='black')
plt.suptitle("Histograms of All Features", fontsize=16)
plt.tight_layout()
plt.show()
