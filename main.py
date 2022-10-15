# Import Module
import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_csv('addresses.csv')
addresses = df.addresses
# Website URL
URL = addresses[50]
# class list set
class_list = set()
# Page content from Website URL
page = requests.get(URL)
# parse html content
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.findAll('table', {'class':'wikitable'})

print(len(table))
table = table[1] # 0= Title w/Year, 1= Release Date 2= Artists
df = pd.read_html(str(table))
print(df)