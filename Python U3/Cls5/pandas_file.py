import pandas as pd

data={'Name':['Amora','Beast','Steve'],
      'Age':[25,30,25],
      'City':['New York','London','Paris']
      }

df=pd.DataFrame(data)
print(df)

print('\n \n')

#Create a dataframe from a list
data=[["Deadpool",25,'New York'],
      ['Elektra',24,'paris'],
      ['Falcon',30,'London']]

df1=pd.DataFrame(data)
print(df1)


print('\n ')
df.to_csv("for_pandas.csv", index=False)
df1.to_csv("for_1pandas.csv")

# #Create a dataframe from a file
df2=pd.read_csv('for_pandas.csv')
print(df2)

print('\n')

df3=pd.read_json('for_pandas.json')
print(df3)
print('\n')

df4=pd.read_excel('VideoSales.xlsx')
print(df4)

df5=pd.DataFrame()
print(df5)


#Inspection Methods
print("\n\n \n\n")

print(df4.head())
print(df4.tail())

print(df4.loc[0:3])
print(df4.iloc[4:9])
