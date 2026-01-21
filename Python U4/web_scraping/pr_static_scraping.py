from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

url="https://tatamumbaimarathon.procam.in/results/race-results"

html=urlopen(url)
print(type(url), url)

soup=bs(html,'lxml')
print(type(soup), soup)

title=soup.title
print(type(title),title)

text=soup.get_text()
print(type(text),soup.text)