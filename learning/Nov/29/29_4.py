#continue结束循环
n = int(input('Please enter a number less than 10 '))
for i in range(1,10):
    if i == n :
        continue
    print(i)
print('The final num i = ',i)