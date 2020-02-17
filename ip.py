import requests
url="https://m.ip138.com/"
try:
    r=requests.get(url+'202.204.112.10:80')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")