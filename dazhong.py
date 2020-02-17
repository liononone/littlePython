import re
import requests
from lxml import etree
from bs4 import BeautifulSoup
 

def getHtmlText(url):
    r=open("/Users/liononone/Desktop/little/dazhonghuoguo.html","r",encoding="utf=8")
    r=r.read()
    return r.text

 
def getShopList(list,html):
    try:
        slt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        flt=re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(slt)):
            shop=eval(slt[i].split(':')[1])
            food=eval(flt[i].split(':')[1])
            ilt.append([shop,food])
    except:
        print("")


def getShopInfo(list,url,fpath):
    try:
        tplt="{:10}\t{:30}\t"
        print(tplt.format("商店名","特色菜"))
        count=0
        for g in list:
            count+=1
            print(tplt.format(count,g[0],g[1]))

        with open(fpath,encoding='utf-8')as f:
            f.write(str(list)+'\n')
    except:
        return " "


def main():
    url='/Users/liononone/Desktop/little/dazhonghuoguo.html'
    outpath='/Users/liononone/Desktop/little'
    alist=[]
    html=getHtmlText(url)
    getShopList(alist,html)
    getShopInfo(alist,url,outpath)


main()