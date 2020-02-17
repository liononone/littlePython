import requests
kv={'q':'ahahahahhahahahaha'}
r=requests.get('http://www.so.com/s',params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))