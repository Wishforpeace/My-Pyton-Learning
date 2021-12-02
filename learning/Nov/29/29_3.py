#Use break to stop for circulation
n = int(input('Please enter a number less than 10  '))
for i in range(1,10):
    if i == n+1 :
        break
    print(i)
print("After the circulation stopped,i=",i)
