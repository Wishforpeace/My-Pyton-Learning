#5_4 通过continue语句终止某次循环

# 循环过程中因为突发状况需要终止本次循环，可以使用continue语句

# continue语句只能终止本次循环，如果循环条件依然成立，则继续下一次循环

# 输入一个小于10的正整数n，输出1到9中除n以外的其它正整数 

n=int(input('输入一个小于10的正整数n='))

for i in range(1,10):
    
    if i==n:  
        continue
    
    print(i)

print("循环结束后i=",i)

#while循环中也可以使用continue语句，本例程序使用while循环实现，该如何修改？    


















