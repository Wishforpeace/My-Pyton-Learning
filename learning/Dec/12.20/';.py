#已知某企业奖金计算方式如下：
#利润(I)低于或等于10万元时，奖金可提10%；高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到100万之间时，高于20万元的部分，可提成5%；高于100万元时，超过100万元的部分按1%提成。奖金按月结算。请为该企业设计计算发放奖金数额的程序。
I = int(input("请输入这个月的利润(万）"))
award = 0 
if I<=10:
    award = I*0.1
if I >10 and I <=20:
    award = 10*0.1+(I-10)*0.075
if I >20 and I <=100:
    award = 10*0.1+10*0.075+(I-20)*0.05
if I >100:
    award = 10*0.1+10*0.075+80*0.05+(I-100)*0.01
print(award)