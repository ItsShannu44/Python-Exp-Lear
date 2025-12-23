import pandas as pd

df=pd.read_csv('sales_r.csv')

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head(2))
print(df.tail(3))

#CHeck for NAN values
print(df.isna())
print(df.isna().sum())

#Check NAN in rows
print(df.isna().any(axis=1))
print(df.isna().any(axis=1).sum())

#Check for not NAN values in columns
print(df.notna())
print(df.notna().sum())

#Check for not NAN values in ROws

print(df.notna().any(axis=1))
print(df.notna().any(axis=1).sum())

print(df.columns)

#Clean the column names.
df.columns=df.columns.str.strip()
print(df.columns)

print(df.head)
print(df.tail)

#Remove a quotes, commas from a particular column.


#Convert column amount to str
#Replace quotes
#Replace comma
#Extract the numeric digits.

df['Amount']=(
    df['Amount'].astype(str)
    .str.replace('"','',regex=False)
    .str.replace(',','',regex=False)
    .str.extract(r'(\d+)',expand=False)
)

print(df.dtypes)

#NAN values can be replaced with
# 1. mean-mid value
# 2. median- avg value
# 3. mode- value with hightest freq

#Convert column to Numeric

df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
    #first parameter - column that has to be converted
    #errors = coerce -all non numeric chars will be converted as NAN
print(df.dtypes)

#Fill NaN Values with median

df['Amount']=df['Amount'].fillna(df["Amount"].median())
print(df['Amount'])

print(df['Qty'])

#Replace in Qty with mean
df['Qty']=pd.to_numeric(df['Qty'],errors='coerce')

print(df.dtypes)
print(df['Qty'])

#Fill Qty's NaN valuess with mean
df['Qty']=df['Qty'].fillna(df['Qty'].mean())
print(df['Qty'])

print(df.head)

#Drop Columns
# 1. If the column contains too many NAN
# 2. it is unwanted column


df=df.dropna(axis=1, how='all')
print(df.columns)

df=df.dropna(axis=1, how='any')
print(df.columns)

# df=df.drop(columns=['Unnamed: 6'])

# df=df.iloc[:,:-1] 
# #This works only for last columns.
# df=df.loc[:,~df.columns.str.contains('^Unnamed')]
#  #works when the exact column name is not known
# print(df)



print(df['Region'])


#standardize text columns
df['Region']=df['Region'].str.strip().str.lower()

print(df['Region'])

#Remove quotes in all cols
df=df.apply(lambda c: c.astype(str).str.replace('"','',regex=False))
print(df)

#Convert the Region to numeric. All no numeric becpomes NAN
#Create boolean mask. It is true when Region is 500 or 800. Replace all such rows as north
df.loc[pd.to_numeric(df['Region'],errors='coerce').isin([500,800]),'Region']='north'
print(df)


print(df['Amount'])

#Filter the data based on the conditions
df['Amount']=pd.to_numeric(df['Amount'],errors='coerce')
hsales=df['Amount']>2000
print(type(hsales))
print(hsales)

#Create a df based on the filter.
df_high=df[hsales]
print(type(df_high))
print(df_high)

# To count the num of rec or rows in a DF

print(len(df))
print(len(df_high))


#Filterig Based on Multiple conditions

c_amount=df['Amount']>2000
c_region=df['Region']=='south'
print(type(c_amount),type(c_region))

#Conditions can be & or | 
df_t1=df[c_amount & c_region]
df_t2=df[c_amount | c_region]
df_t3=df[c_region | c_amount]
df_t4=df[c_region & c_amount]
print(len(df_t1),len(df_t2),len(df_t3),len(df_t4))

#Sort the values in column
sf_sort=df.sort_values('Amount') # Ascending by deafult
print(sf_sort)
print('\n')
df_sort=df.sort_values('Amount', ascending=False)
print(df_sort)
print('\n')
df_s1=df.sort_values(['Region','Amount'])
print(df_s1)
print('\n')
df_s1=df.sort_values(['Region','Amount'], ascending=[True,False]) #Sorts the Region in asce and Amt in desc
print(df_s1)

#Create new columns based on existing cols

df['Tax']=df['Amount']*0.18
print(df.columns)
print('\n')
print(df)

print('\n')
df['Total_Tax']=df['Amount']+df['Tax']
print(df['Total_Tax'])
print(df.columns)

#-------------------PRofiling the cols------
#Count the values

print(df['Region'].value_counts())
print(df['Amount'].value_counts())
print('\n')


#summarize the DF

print(df['Amount'].describe())
print('\n')

print(df['Region'].describe())
print('\n')


df.columns=df.columns.str.strip()
print(df.columns)
print(df['City'].describe())
print('\n')

#Gouping the data
grp_reg=df.groupby('Region')
print(type(grp_reg),len(grp_reg),grp_reg)
print('\n')

#------------View the Grouped data-------

#view the grouped names
print(grp_reg.groups.keys())
print('\n')

#view the row index that belongs to each grp
print(grp_reg.groups)
print('\n')

#view specific group
print(grp_reg.get_group('north'))
print('\n')


#loop through all the grps 
for n, g in grp_reg:
    print(f'Group:{n}')
    print(g)
print('\n')

#Grping based on mul cols

grp_mul=df.groupby(['Region','City'])
print(grp_mul.groups)
print('\n')

#sum of the amount of each region
sales_reg=grp_reg['Amount'].sum()
print(sales_reg)

#Multiple Aggregations 
region_summary=grp_reg['Amount'].agg(['sum','mean','count'])
print(region_summary)
print('\n')

#Custom Aggregation
summary=df.groupby('Region').agg(Total_Amt=('Amount','sum'),Avg_Amt=('Amount','mean'),Avg_Tax=('Tax','mean'),Unique_City=('City','nunique'))
print(type(summary), summary)
print('\n')