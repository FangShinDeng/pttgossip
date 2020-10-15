import requests
import lxml
from bs4 import BeautifulSoup as BS

payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
URL18 = "https://www.ptt.cc/ask/over18"
URL = "https://www.ptt.cc/bbs/Gossiping/index.html"
rs = requests.session()
res = rs.post(URL18 ,data = payload, headers = headers)
res = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html", headers = headers)

# print(res.text)

soup = BS(res.text, features = "html.parser")

for entry in soup.select('.r-ent'):
    print(entry.select('.title')[0].text, entry.select('.author')[0].text, entry.select('.date')[0].text)
    pass