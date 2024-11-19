import pandas as pd

def clean_data():
    data = pd.read_excel("data/bee_virus_data.xlsx", sheet_name=None, header=1)

    dataframes = []
    for region_name, df in data.items():
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [' '.join(col).strip() for col in df.columns.values]
        df.columns = ["No", "Sample", "ABPV", "BQCV", "CBPV", "DWV", "SBV"]
        
        df = df.dropna(how='all')
        
        df = df.copy()
        df["Region"] = region_name
        
        dataframes.append(df)
    
    # print(dataframes)

    combined_df = pd.concat(dataframes, ignore_index=True)

    combined_df['Sample Type'] = combined_df['Sample'].str[-1].map({'A': 'Adult', 'B': 'Brood'})

    combined_df = combined_df.fillna('unknown')

    combined_df.to_csv("data/bee_virus_data_cleaned.csv", index=False)
    
    return combined_df

data = clean_data()
# print(data.head())