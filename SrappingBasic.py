import requests

link = "https://quotes.toscrape.com/"
res = requests.get(link)
print(res)
print("-"*50)

print(res.text)
html = res.text
fd = open("main.html","w",encoding="utf-8")
fd.write(html)
fd.close()