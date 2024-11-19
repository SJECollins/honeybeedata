import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
data = pd.read_csv("data/bee_virus_data_cleaned.csv")

# Virus columns
virus_columns = ["ABPV", "BQCV", "CBPV", "DWV", "SBV"]

# Replace "weak positive" with "positive" to simplify the analysis
for virus in virus_columns:
    data[virus] = data[virus].replace({"weak positive": "positive"})

# Bar plot of the number of positive samples by virus
positivity_by_virus = data[virus_columns].apply(lambda x: (x == "positive").sum())
positivity_by_virus.plot(kind="bar", title="Number of positive samples by virus")
plt.show()

# Group the data by region and count the number of positive samples
positivity_by_region = data.groupby('Region')[virus_columns].apply(
    lambda x: (x == 'positive').sum()
)

# Heatmap of the number of positive samples by region
sns.heatmap(positivity_by_region, annot=True, cmap="YlOrRd")
plt.title("Number of positive samples by region")
plt.show()