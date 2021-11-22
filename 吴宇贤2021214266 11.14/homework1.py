# 编程练习
# 1. 将一条消息存储到变量中，再将其打印出来。

a = "hello world"
print(a)

# 2. 将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。

b = "I love python"
print(b)
b = "I love golang"
print(b)

# 3. 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。

usrname1 = "Donald Trump"
print(usrname1 + ", would you like to learn some Python today?")
# 4. 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。

usrname2 = "john biden"
print(usrname2.lower())
print(usrname2.upper())
print(usrname2.title())

# 5. 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：Jackie Chan once said, “I made a mistake, which all the man may make.”

print ("鲁迅once said,\"我没有说过这句话\"")

# 6. 重复上一题，但将名人的姓名存储在变量famous_person中，再创建要显示的消息，并将其存储在变量message中，然后打印这条消息。

famous_person = "鲁迅"
saying = "我没有说过这句话"
full = famous_person+"once said"+","+"\""+saying+"\""
print(full)