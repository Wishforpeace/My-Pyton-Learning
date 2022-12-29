a = [10,14,21,38,45,47,53,81,87,99]
x = int(input("输入你要查找的数"))
left = 0 
right = len(a)-1
while left <right:
    middle = (left+right)//2
    if a[middle]< x:
        left = middle+1
    elif a[middle]==x:
        print("查找成功",x,"是第",middle+1,"个数")
        break
    else:
        right = middle -1
else:
    print("查找失败")