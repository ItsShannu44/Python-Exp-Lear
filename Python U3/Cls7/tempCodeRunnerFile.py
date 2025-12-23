import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('sensor_read.csv')
print(df.shape)
#convert the str to numeric data
print(df.columns)
df['Timestamp']=pd.to_numeric(df['Timestamp'],errors='coerce')

print(df.dtypes)

#convert timestamp to standart format
df['Timestamp']=pd.to_datetime(df['Timestamp'],unit='s') #unit=s tels the pandas that the numbers represent the seconds
print(df.head())