import requests
from bs4 import BeautifulSoup

link = "https://quotes.toscrape.com/"
res = requests.get(link)
soup = BeautifulSoup(res.text,"html.parser")

#To print first span text
print(soup.find('span'))
print("-"*100)

#To print first span text where class name is "text"
print(soup.find('span', class_ = 'text'))
print("-"*100)

#To print only text without html tags
print(soup.find('span', class_ = 'text').text)
print("-"*100)

#To print only text without doubt qoute 
print(soup.find('span', class_ = 'text').text[1:-1])
print("-"*100)

#To print all span text without html tags and double qoute
print(soup.find_all('span', class_='text'))

#Store all text in one var

qoutes = []

for span in soup.find_all('span', class_='text'):
    qoutes.append(span.text[1:-1])

print("-"*100)

for sp in qoutes:
    print(sp)

