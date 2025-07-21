import pandas as pd

date = pd.read_csv('IntroToPy/mountains_db.tsv', sep='\t', header=None, names=['Mountain', 'Height', "Country", "Code"])
print(len(date['Code'].unique()))
print(f'There are {len(date["Code"].unique())} unique countries in the dataset.')
# Count the number of NULL values in the 'Height' column
null_count = (date['Height'] == 'NULL').sum()
print(f'The "Height" column has {null_count} NULL values.')
print (date['Height'].max())
print (date['Height'].min())
print (date['Height'].mean())
print (date['Height'].std())
print (date['Height'].median())
