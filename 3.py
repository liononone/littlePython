import requests
res.encoding='utf-8'
url='http://news.baidu.com/'
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text,'html.parser')
except:
    print('爬取失败')