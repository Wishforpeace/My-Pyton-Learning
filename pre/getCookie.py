from selenium import webdriver
import time
import pickle
browser = webdriver.Chrome()
browser.get('https://www.bilibili.com/')
time.sleep(5)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())
input("请输入任意键继续...")



time.sleep(5)
with open("cookies文件.pickle",'wb') as file:
    pickle.dump(browser.get_cookies(),file)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())



input("请输入任意键继续...")
browser.delete_all_cookies()
browser.get('https://www.bilibili.com/')

time.sleep(5)
print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())
