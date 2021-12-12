#1. 列表a = [6, 3, 5, 7, 0]，编程实现插入排序算法进行递增排序。
def insert_sort(array_list):
    length = len(array_list)
    for j in range(1,length):
        i = j 
        while i > 0 :
            if array_list[i]<array_list[i-1]:
                array_list[i],array_list[i-1] = array_list[i-1],array_list[i]
                i -= 1
            else:
                break
array = [6, 3, 5, 7, 0]
insert_sort(array)
print(array)
#2. 列表a = [6, 3, 5, 7, 0]，编程实现选择排序算法进行递增排序。
def selection_sort(array_list):
    length = len(array_list)
    for i in range(length):
        k = i
        for j in range (i+1,length):
            if array_list[k]>array_list[j]:
                k = j
            array_list[i],array_list[k] = array_list[k],array_list[i]
array2 = [6, 3, 5, 7, 0]
selection_sort(array2)
print(array2)
#3. 编程求出所有的水仙花数（如果三位十进制正整数abc满足条件，abc=a3+b3+c3，则abc是水仙花数，例如153=13+53+33，所以153是水仙花数）。（输出结果： 153，370，371，407 ）
num = int(input("请输入一个数，判断是否为水仙花数"))
a = num%10#个位
b = int((num%100)/10)
c = int(num/100)
if a**3+b**3+c**3==num:
    print(num,"这是水仙花数")
else:
    print(num,"这不是水仙花数")
#4. 输入大于2的正整数n，编程求出2到n之间（含n）所有的完数。所谓完数是指所有小于自身的约数之和等于自身的正整数，比如28所有小于自身的约数为1、2、4、7、14，这些约数之和28，所以28是完数。（10000以内的完数有：6，28，496，8128）
while 1:
    numb = int(input("请输入一个大于2的数字"))
    if numb <= 2:
        print("请重新输入")
    else:
        break
well_numb=[]
for i in range (2,numb):
    k = i
    approximate=[]
    sum = 0
    for j in range(1,i+1):
        if k % j ==0:
            approximate.append(j)
    for j in range(len(approximate)):
        sum += approximate[j]
    if sum == k:
        well_numb.append(sum)
print(numb,"以内的完数有",well_numb)
#5. 输入两个正整数a与b（假定输入的a<=b），编程输出a与b之间所有的素数
def Prime(k):
    for j in range(2,int(k**0.5)+1):
        if k % j == 0:
            return False
    return True
a= int(input("请输入a,b(a<=b)"))
b= int(input())
prime_numb =[] 
for i in range(a,b+1):
    k = i 
    bool = Prime(k)
    if bool:
        prime_numb.append(k)
print(a,"和",b,"之间的所有素数为",prime_numb)
        