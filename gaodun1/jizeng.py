"""
编写者:liononone
时间:2020.2.16
功能:计算不同条件下现金流的FV,PV,EAR
"""

#计算FV
pv=100  #现值
rate=0.1    #提现利率
t=10    #投资期限

fv = pv*(1+rate)**t
print("FV值为:",fv)

#计算pv
fv=100  
rate=0.1    
t=10    
pv = fv/(1+rate)**t

print("PV值为:"+str(pv))

#已知报价利率计算有效年利率
sar=0.03
m=10
ear=(1+sar/m)**m - 1

print("有效年利率为:",ear)
