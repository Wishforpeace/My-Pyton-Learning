a=[1, 2, 32, 8, 17, 19, 42, 13, 0]
n=len(a)
x=int(input("输入一个整数x="))
posi=-1  #变量posi表示x在列表a中的位置，默认其不在a中
for i in range(n):
    if x==a[i]:
        posi=i
print(posi)

