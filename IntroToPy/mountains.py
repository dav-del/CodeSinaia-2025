import pandas as pd
df = pd.read_csv("IntroToPy/mountains_db.tsv", sep="\t", header=None, names=["Name", "Elevation", "Country", "Code"])
print(len(df['Code'].unique()))
null_count = df['Elevation'].isnull().sum()
print(f"There are {null_count} with NULL mountains with no elevation data")
vals = df["Elevation"].dropna()
print(vals.describe())
