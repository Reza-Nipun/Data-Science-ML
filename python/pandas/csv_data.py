import pandas as pd

# df = pd.read_csv('../../Pandas dataset/ZILL-Z77006_3B.csv')

df = pd.read_csv('../../Pandas dataset/newcsv2.csv', names = ['Date','House_Price'], index_col=0)
print(df.head())