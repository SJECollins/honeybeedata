import pandas as pd

data = pd.read_csv("data/bee_virus_data_cleaned.csv")

print(data.head())

print(data.describe())
print(data["ABPV"].value_counts())
print(data["CBPV"].value_counts())


virus_columns = ["ABPV", "BQCV", "CBPV", "DWV", "SBV"]

for virus in virus_columns:
    data[virus] = data[virus].replace({"weak positive": "positive"})
positivity_by_region = data.groupby("Region")[virus_columns].apply(lambda x: (x == "positive").sum())

print(positivity_by_region)
