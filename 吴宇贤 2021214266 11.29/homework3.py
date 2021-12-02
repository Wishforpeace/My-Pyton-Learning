# 编程练习
# 1. 循环输入若干个互不相等正实数，输入0或负实数时终止输入，然后求出这些数的平均数并输出，同时还输出这些数中最大数和最小数。

from typing import Counter


def minimum(a=[]):
    min = a[0]
    index = 0
    for index in range(len(a)):
        if a[index]<min :
            min = a[index]
    return min
def maximum(a=[]):
    max = a[0]
    index = 0
    for index in range(len(a)):
        if a[index]>max :
            max = a[index]
    return max
def average(a=[]):
    sum = 0 
    for index in range(len(a)):
        sum += array[index]
    aver = float(sum / len(a))
    return aver
array = []
while 1:
    n = int(input(""))
    if n <=0 :
        break
    array.append(n)
max = maximum(array)
print(max)
min = minimum(array)
print(min)
aver = average(array)
print(aver)
# 2. 编程输出fibonacci数列（1、1、2、3、5、8、13、21、…，从第3项开始每一项的值都是相邻的前两项之和）的前n项的值，其中n的值通过输入确定，当n的值较大时，每输出5项就另起一行。
# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

n = int(input("请输入你想要的fibonacci数列个数"))
result_list = []
for i in range(1, n + 1): 
    result_list.append(Fibonacci_Recursion_tool(i))
print(result_list[::])
# 3. 据2006年统计，我国人口为13.0756亿人，假定人口的年增长率是1%，请计算哪一年中国人口将超过20亿？
def population(num):
    year = 0
    while num<=20:
        num = num*1.01
        year += 1
    return num
num = 13.0756
year = population(num)
print("人口过20亿需要",int(year),"年")
# 4. 任意输入2个正整数，编程求出并输出这2个数的最大公约数和最小公倍数。
def Greatest_common_divisor(n,m):
    if n > m:
        temp = m
    elif n <= m :
        temp = n
    while 1>0 :
        if n % temp == 0 and m %temp == 0:
            divisor = temp
            break
        temp -=1
        
    return divisor 
def Greatest_common_multiple(n,m):
    if n > m :
        temp = n
    if n <= m:
        temp = m
    while 1>0:
        if temp % n == 0 and temp % m == 0 :
            multiple = temp
            break
        temp +=1
    return multiple
n = int(input("请输入第一个数"))
m = int(input("请输入第二个数"))
divisor = Greatest_common_divisor(n,m) 
print(n,"和",m,"最小公约数是",divisor)
multiple = Greatest_common_multiple(n,m)
print(n,"和",m,"最小公倍数是",multiple)
# 5. 公园门票按照年龄收费，4岁以下免费，满4不满18岁收费5元，满18岁不满65岁收费10元，65岁以上收费5元。循环实现每输入一个表示年龄的正整数，然后输出其应缴费用，当输入为0或负整数时程序.
while 1>0:
    old_year = int(input("请输入游客年龄"))
    if old_year <= 0 :
        break
    if old_year<4:
        print("免费")
    if old_year >= 4 and old_year <18 :
        print("收费5元")
    if old_year >=18 and old_year <65 :
        print("收费10元")
    if old_year >=65 :
        print("收费5元")