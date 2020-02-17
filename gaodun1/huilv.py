#提示用户输入汇率信息
print("美元货币单位为USD,人民币货币单位为CNY")
print("汇率为直接标价法,CNY/USD,含义为 1美元=?人民币")
exchande_rate=input("请输入今日汇率:")
currency=input("请输入带有货币单位的金额:")

#转换汇率
if currency[-3:]=='USD':
    rmb=eval(currency[0:-3])*eval(exchande_rate)
    print(currency+"相当于"+str(rmb)+'CNY')
elif currency[-3:]=='CNY':
    dollar=eval(currency[0:-3])/eval(exchande_rate)
    print(currency+"相当于"+str(dollar)+'USD')
else:
    print("输入格式错误,请重新输入")