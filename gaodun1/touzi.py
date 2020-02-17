cf0,cf1,cf2,cf3=-300,45,80,200
r=0.10

npv = cf0 + cf1/(1+r) + cf2/(1+r)**2 + cf3/(1+r)**3

if npv>0:
    print("该项目值得投资,NPV为"+str(npv)+"万元.")
else:
    print("该项目不值得投资,NPV为"+str(npv)+"万元.")