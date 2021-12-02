n=int(input('输入一个正整数n='))
i=1

while 1:  #while后面的条件表达式只有一个常数1，python将非0的常数都当做True来处理
          #这种情况下循环条件与变量i没有任何关系，所以如果后面的break语句不被执行的话，循环不会被终止

    if i==n+1:  #当i等于n+1时执行break语句，强行终止循环
        break
    
    print(i)
        
    i+=1  #i+=1是i=i+1的简化表示

    

print("循环结束后i=",i)