import requests
from bs4 import BeautifulSoup
res=requests.get('http://www.dianping.com/shop/9183273/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
for news  in soup.select('.list_14'):
    if(len(news.select('a'))>0):       
        h=news.select('li')[0].text
        a=news.select('a')[0]['href']
                
        print(h,a)         
