import pandas as pd

# Read raw data
df = pd.read_csv("raw_data/customers.csv")

# Clean data
df = df.dropna()
df.columns = df.columns.str.lower()

# Filter data
df_poland = df[df["country"] == "Poland"]

# Save cleaned data
df_poland.to_csv("cleaned_data/customers_poland.csv", index=False)

print("Pipeline finished successfully")
