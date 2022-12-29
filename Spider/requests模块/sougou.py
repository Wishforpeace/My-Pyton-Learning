import requests

# step 1：制定url
url = "https://www.sougou.com"
# step 2:发送请求
response = requests.get(url=url)
# step 3:获取响应数据,text返回字符串形式的响应数据
page_text = response.text
print(page_text)
# step 4:持久化存储
with open("./sougou.html", 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print("爬取数据结束")
