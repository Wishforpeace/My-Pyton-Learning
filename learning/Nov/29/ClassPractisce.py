n = int(input('Please enter a number less than 10 '))
i = 0
while i <10 :
    i += 1
    if i != n:
        print(i)
    if i == n :
        continue
   
print('The final i = ',i)