def Fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

for i in range(1,11):
    print(Fibonacci(i))
