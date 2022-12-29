# 获取资源，直接导包
from urllib.request import urlopen

url ="http://www.baidu.com"

resp = urlopen(url)

# print(resp.read().decode("utf-8"))

with open("mybaidu.html",mode="w") as f:
    f.write(resp.read().decode("utf-8")) # 读取网页源代码
print("over")