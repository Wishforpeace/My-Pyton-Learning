﻿#4_1 输入字符串

#   前面的程序中变量都是通过赋值获取值，可以通过调用input函数实现在程序运行过程中，
#   用户从键盘输入信息赋值给变量，系统将从键盘获取的输入信息当做字符串类型处理。

#   input()函数的调用形式为：变量名=input(字符串)，input()函数被调用时程序将中止执行，
#   等待用户从键盘输入信息，输入完毕后按回车键，系统获取用户的输入信息保存到赋值运算
#   符左边的变量中，然后程序继续往下执行。

#   input后面括号里面的字符串（函数input的参数）是输入时给用户的提示信息。
#   如果input后面括号里面是空的（函数input不带参数），则在用户输入时不会得到任何提示信息

#   先看下面这个例子

message=input()

print(message)

#   上面这段代码开始执行时，程序没有任何反应，其实此刻程序是等待用户输入一串信息；
#   编写程序的人知道这一点，但是使用程序的人（没学过python的菜鸟）未必知道；
#   所以调用input()函数时给一个提示信息是一个推荐的编程好习惯！

message=input("你说神马，我会学你说神马，不信就试试看？")

print(message)

#   在命令行模式下运行上面的代码，将print(message)改为message，再运行看看结果！ 

#   可以发现在命令行模式下面询问变量message的值时，系统输出的是带单引号的字符串信息！

#   总结一下，调用input()函数实现输入时，括号里的参数是给用户的输入提示，
#   然后输入的信息作为函数调用的结果赋值给左边的变量。

name = input("Please enter your name: ")
print("Hello, " + name + "!")











