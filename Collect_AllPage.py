import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

#link = "https://quotes.toscrape.com/"
#res = requests.get(link)
#soup = BeautifulSoup(res.text,"html.parser")
data=[]
for sp in tqdm(range(1,11)):
    lnk = "https://quotes.toscrape.com/"+"page/"+str(sp)
    res = requests.get(lnk)
    soup = BeautifulSoup(res.text,"html.parser")

    for sp in soup.find_all('div', class_='quote'):
            qoute = sp.find('span', class_='text').text[1:-1]
            author = sp.find('small',class_="author").text
            author_id = sp.find('a').get("href")
            link = "https://quotes.toscrape.com"+author_id
            
            #print("-"*100)
            
            #collecting tag text from class tag
            tags =[]
            for tag in sp.find_all("a",class_="tag"):
                tags.append(tag.text)
            
            # joining the tags by using comma
            tags =", ".join(tags)
            
            #print(qoute,author,author_id,tags)
            data.append([qoute,author,author_id,link,tags])

#for dt in data:
    #print(dt)

#creating data frame with by giving coulumn name
df = pd.DataFrame(data=data,columns=["Quote","Author","Author_ID","Link","Tag"])

#Exporting data to csv file
df.to_csv("Data1.csv")

print(df)   