from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

url="https://tatamumbaimarathon.procam.in/results/race-results"

html=urlopen(url)
print(type(url), url)

soup=bs(html,'lxml')
print(type(soup), soup ,"\n")

title=soup.title
print(type(title),title, "\n")

text=soup.get_text()
print(type(text),soup.text ,"\n")


a=soup.find_all('a','\n')
print(a)
for link in a:
    print(link.get('href'))

rows=soup.find_all('tr')
print(rows)
for row in rows:
    row_td=soup.find_all('td')
print(row_td, "\n")

