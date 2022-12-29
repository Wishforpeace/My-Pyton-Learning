# 编程练习
# 1. 输入任意3个正实数，判断以这3个实数为长度的线段能否构成一个三角形，并输出判断结果（输出Y或N即可）。
print("请输入三条边")
a = int(input())
b = int(input())
c = int(input())
if a+b>c and b+c >a and a+c>b:
    print("Y")
else:
    print("N")
# 2. 输入一个任意实数，如果该数小于0输出-1，如果该数等于0输出0，如果该数大于0输出1。要求只能使用简单if语句实现。
num1 = int(input("if语句,求求你输入一个数吧"))
if num1 <0 :
    print(-1)
if num1==0:
    print(0)
if num1>0:
    print(1)
# 3. 输入一个任意实数，如果该数小于0输出-1，如果该数等于0输出0，如果该数大于0输出1。要求只能使用if-else语句实现。
num2 = int(input("if-else,求求你再输入一个吧"))
if  num2>=0:
    if num2==0:
        print(0)
    else:
        print(1)
else :
    print(-1)
# 4. 输入一个任意实数，如果该数小于0输出-1，如果该数等于0输出0，如果该数大于0输出1。要求只能使用if-elif-else语句实现。
num3 = int(input("if-elif-else,再帮帮孩子吧"))
if num3 < 0:
    print(-1)
elif num3 == 0 :
    print(0)
if num3 > 0:
    print(1)
# 5. 一个正整数按照能否被3、5、7整除可分成八种情况，输入任意一个正整数，输出其属于哪一种情况。
num4 = int(input("输入一个正整数"))
if num4 % 3 != 0 and num4 % 5 != 0  and num4 % 7 != 0 :
    print("这个数不能被3/5/7中任何一个整除")
else:
    if num4 %3 == 0 :
        if num4%5 == 0:
            if num4%7 ==0:
                print("prefect,这个数很牛逼,都能除")
            else:
                print("这个数能被3/5整除")   
        else:
            if num4%7==0:
                print("这个数能被3/7整除")
            else :
                print("这个数只能被3整除")
    else:
        if num4%5 == 0:
            if num4%7 ==0:
                print("这个数能被5/7整除")
            else:
                print("这个数能被5整除")   
        else:
            if num4%7==0:
                print("这个数能被7整除")
            
                
# 6. 输入3个互不相等的整数，按照从小到大的顺序输出这3个整数。
arr =input("")
num = [int(n) for n in arr.split()]
num.sort()
print(num)
# 7. 运输公司对用户计算运费。设每公里每吨货物的基本运费为p，货物重量为w，距离为s，折扣为d，则总运费f的计算公式为：f=p×w×s×(1-d)。其中折扣d与距离s之间的关系为：
# 　  s＜250，d=0                   
#     250≤s＜500，d=2％
#     500≤s＜1000,d=5％
#     1000≤s＜2000,d=8％     
#     2000≤s＜3000, d=10％     
#     3000≤s,d=15％              
# 编写一个程序，输入基本运费p、货物重量w和距离s，输出总运费f。
p =int(input("请输入基本运费p:"))
w =int(input("请输入货物质量w:"))
s =int(input("请输入里程s:"))
if s<250 :
    d =0
if s>= 250 and s < 500:
    d=0.02
if  s>= 500 and s < 1000:
    d=0.05
if s>=1000 and s<2000:
    d=0.08
if s>=2000 and s<3000:
    d=0.1
if  s>=3000:
    d =0.15
f=float(p*w*s*(1-d))
print('%.2f'%f)  

