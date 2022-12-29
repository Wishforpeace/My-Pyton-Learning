import re

f = open("pipei.txt", "r", encoding='utf-8')
byt = f.readlines()
for index in range(len(byt)):
    a_list = re.findall(r'[\u4e00-\u9fa5]', byt[index])
    if len(a_list) != 0:
        print("".join(str(i) for i in a_list))
print("\n")
for index in range(len(byt)):
    a_list = re.findall(r'[\u4e00-\u9fa5]', byt[index])
    if len(a_list)!=0 and len(a_list)==3 and a_list[2]==chr(32593):
        print(a_list[0]+a_list[1]+a_list[2])
