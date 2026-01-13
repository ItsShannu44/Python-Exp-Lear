from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import matplotlib.pyplot as plt
 
#   Url which contains data
url="https://tatamumbaimarathon.procam.in/results/race-results"

#   pass url to urlopen() to get html of page
html=urlopen(url)
print(type(html),html)

#   construct BeautifulSoup obj using the html
soup=bs(html,'lxml')

# Extract teh title of the Webpage
title=soup.title
print(title)
print(type(title))

# Extract the text of the webpage
text=soup.get_text()
print(soup.text,type(text))
print("\n \n")
# print(text,type(text)) #both are same res

#   Extract the useful html tags within the page
soup.find_all('a')

#   Print the hyperlinks
all_links=soup.find_all('a')
for link in all_links:
    print(link.get('href'))

#   Extract tabular data
rows=soup.find_all('tr')
print(rows)
print("\n")
print(type(rows))

#   Get all table rows in a list form and convert into a DF
for row in rows:
    row_td=row.find_all('td')
print(row_td)
print("\n\n")
print(type(row_td))

#   Extract the data without the html tags
str_cell=str(row_td)
cleantext=bs(str_cell, 'lxml').get_text()
print(cleantext)
print("\n\n")
print(type(cleantext))

#   Extract the Data without html tags using regex
list_row=[]
for row in rows:
    cells=row.find_all('td')
    str_cell=str(cells)
    clean=re.compile('<.*?>')
    clean_l=(re.sub(clean,'',str_cell))
    list_row.append(clean_l)
    print(list_row)

df=pd.DataFrame(list_row)
print(df.head(10))

#   Data Manipulation and Cleaning
df1=df[0].str.split(',',expand=True)
print(df1.head(5))

# Remove the opening square braces
df1[0]=df1[0].str.strip('[')
print(df1.head(5))

df1[4]=df1[4].str.strip(']')
print(df1.head(5))

#   Accessing the title for the cols
col_labels=soup.find_all('th')
print(col_labels)
print('\n\n')
print(type(col_labels))
all_head=[]
col_str=str(col_labels)
clean_text=bs(col_str,'lxml').get_text() #Removes all the tags from the text
all_head.append(clean_text)
print(all_head)

#   convert to df
df2=pd.DataFrame(all_head)
print(df2)

#splitting
df3=df2[0].str.split(',',expand=True)
print(df3.head(5))

# Remove the opening square braces
df3[0]=df3[0].str.strip('[')
df3[4]=df3[4].str.strip(']')
print(df3.head(5))
print("\n\n")

#--------MERGE THE TWO DF------------
frames=[df3,df1]
df4=pd.concat(frames)
print(df4.head(5))

# -- Assign the 1st row to be the table header
df5=df4.rename(columns=df4.iloc[0])
print(df5.head(5))

#---Drop all rows with missing vals
df5=df5.dropna(axis=0,how='any')
print(df5.head(5))

#---Drop row 0
df5=df5.drop(index=0)
print(df5.head(5))
print("\n")
df5.info()
print(df5.shape)

#____Processing of DF_________

#a. convert the finish time to total no of minutes.
df5.columns = df5.columns.str.strip().str.replace('\n',' ', regex=False)

time_mins = [
    (int(h)*3600 + int(m)*60 + int(s)) / 60
    for h,m,s in (t.split(':') for t in df5['FINISH TIME'])
]

# Convert Finish Time (HH:MM:SS) to total minutes

#add the new col as run_mins
df5['Run_mins'] = time_mins


#a.--Get the mean time taken by each nationalty
df5.groupby('NATIONALITY')['Run_mins'].mean()


#b/---Find the no of runners per nationality
df5['NATIONALITY'].value_counts()


#c.---Get the difference of minutes between each runners
df5['Diff_mins'] = df5['Run_mins'].diff()


#d.Define the category of the runners based on the time taken
df5['CATEGORY']=pd.cut(
    df5['Run_mins'],
    bins=[0,120,140,160,200],
    labels=['Elite','Strong','Moderate','Slow']
)
print(df5)

#____VISUALIZE THE DATA______

plt.hist(df5['Run_mins'],bins=10)
plt.xlabel('Minutes')
plt.ylabel('Frequency')
plt.show()

#--create box plot for time duration
plt.boxplot(df5['Run_mins'])
plt.ylabel('Minutes')
plt.show()

#create bargraphs for each nationality 
nat_c=df5['NATIONALITY'].value_counts()
nat_c.plot(kind='bar')
df5.groupby('NATIONALITY')['Run_mins'].mean().plot(kind='bar')
plt.show()


#create scatter plots
plt.scatter(df5['RANK'],df5['Run_mins'])
plt.xlabel('RANK')
plt.ylabel('Finish time (mins)')
plt.show()

#create horizontal bar graphs
top10=df5.nsmallest(10,'Run_mins')
plt.barh(top10['NATIONALITY'],top10['Run_mins'])
plt.show()

top10=df5.nsmallest(10,'Run_mins')
plt.barh(top10['NAME'],top10['Run_mins'])
plt.show()
#create line graphs
plt.plot(df5['Run_mins'].expanding().mean())
plt.show()
  