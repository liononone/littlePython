import requests
import re
 
def getHtmlText(url):
    try:
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Cookie': 'mt=ci%3D-1_0; thw=cn; cookie2=1fe768bd537576778883a504ad040dc0; t=fe9ee672fa28f4de8be813cbbab4885d; _tb_token_=e1e37eb874377; UM_distinctid=1700de41a7e47d-0a79f9490d0267-39647b09-fa000-1700de41a7f49e; _samesite_flag_=true; hng=CN%7Czh-CN%7CCNY%7C156; enc=wI3VYO5omU2TWrf7k8nE3tozvm9MhdwxG%2F9RK1raKSS5MUvUA67w%2FtirZtWVMogGIfCL8BFnaidjuQE83GQEfQ%3D%3D; cna=FVqnFn15fUUCAbfKDkiOQRfV; v=0; unb=3981792355; uc3=lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UNk%2FSaVPJUNXWw%3D%3D&nk2=F5RMHljqW0PMFjo%3D&vt3=F8dBxdsWVBWuOYzPTGo%3D; csg=6bf1f243; lgc=tb972347544; cookie17=UNk%2FSaVPJUNXWw%3D%3D; dnk=tb972347544; skt=2d78ffc9f71a6ce1; existShop=MTU4MDgwOTIyNA%3D%3D; uc4=id4=0%40Ug41SKIKX4R4dGqMvWTpyEH7UY9L&nk4=0%40FY4HWy3Npx6mI3g6JjiNb%2FpciUIczg%3D%3D; tracknick=tb972347544; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=45d; _nk_=tb972347544; cookie1=UteFSE9zi5PULb6vuS%2BTMsayouSAHbD20sz7UJzYna4%3D; JSESSIONID=DD88F853C99CE6D3D8067C5205F799A1; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; isg=BIiIZ1zcQpJF0a4XP_ML70_IWfCaMew7ki11vkI51IP2HSiH6kG8yx4flfVtNqQT; l=cBSWKKf7QML1tvy2BOCanurza77OSIRYYuPzaNbMi_5QA6TsA27OoVG2CF96VjWdO8TB4m66axJ9-etXZxNGVi--g3fP.; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xTIkz&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTUOqiucU%2BDNQ%3D%3D&tag=8&lng=zh_CN; mt=ci=0_1'
        }
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("")

def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}\t"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count+=1
        print(tplt.format(count,g[0],g[1]))

    


def main():
    goods="书包"
    depth=2
    
    start_url='https://s.taobao.com/search?initiative_id=staobaoz_20200204&q='+goods
    infolist=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(48*i)
            print("-----------------------------------------------------------")
            html=getHtmlText(url)
            parsePage(infolist,html)
        except:
            continue
    printGoodsList(infolist)

main()
