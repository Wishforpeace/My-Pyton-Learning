from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

wait_time = 10
with open("cookies文件.pickle", 'rb') as file:
    cookiesList = pickle.load(file)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.bilibili.com/')
input("请输入任意键继续...")
for cookie in cookiesList:
    browser.add_cookie(cookie)

browser.get('https://www.bilibili.com/')
time.sleep(1)
# print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())
input("请输入任意键继续...")

# 寻找BV
wait = ui.WebDriverWait(browser, wait_time)

try:
    wait.until(lambda driver: driver.find_elements(By.XPATH,
                                                   "/html/body/div[2]/div/main/div[2]/div[1]/div[1]/div/div[2]/div/div/h3/a"))

    buttons = browser.find_elements(By.XPATH, "/html/body/div[2]/div/main/div[2]/div[1]/div[1]/div/div[2]/div/div/h3/a")

except Exception as error1:

    buttons = browser.find_elements(By.XPATH, "/html/body/div[2]/div/main/div[2]/div[1]/div[1]/div/div[2]/div/div/h3/a")

    time.sleep(10)

length = len(buttons)
urls = {}
for i in range(0, length):  # 遍历列表的循环，使程序可以逐一点击
    links = browser.find_elements(By.XPATH,
                                  "/html/body/div[2]/div/main/div[2]/div[1]/div[1]/div/div[2]/div/div/h3/a")  # 在每次循环内都重新获取a标签，组成列表
    link = links[i]  # 逐一将列表里的a标签赋给link
    url = link.get_attribute('href')
    urls[link.text] = url

input("请输入任意键获取首页推荐视频链接")
for title, url in urls.items():
    print(title, " : ", url)

input("按任意键查询评论")
for title, url in urls.items():
    browser.get(url)
    browser.implicitly_wait(10)

    # print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())

    wait = ui.WebDriverWait(browser, 10)
    try:
        wait.until(lambda driver: driver.find_elements(By.XPATH, "//span[@class='reply-content root-reply']"))
        buttons = browser.find_elements(By.XPATH, "//span[@class='reply-content root-reply']")
    except Exception as error1:
        buttons = browser.find_elements(By.XPATH, "//span[@class='reply-content root-reply']")
        time.sleep(10)
    print("title:%s\n", title)
    count = 1
    for button in buttons:
        print('comment[%d]:%s'%(count, button.text))
        count += 1
    input("请输入任意键继续...")
input("请输入任意键继续...")
browser.quit()
