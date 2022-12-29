from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("http://www.opgg.cn/champion/Annie/mid/build")
browser.implicitly_wait(10)

# print("字典长度:\n",len(browser.get_cookies()),browser.get_cookies())
input("请输入任意键继续...")

# 寻找BV
wait = ui.WebDriverWait(browser, 10)
try:
    wait.until(lambda driver: driver.find_elements_by_xpath("//div[@class='top']//span"))
    buttons = browser.find_elements_by_xpath("//div[@class='top']//span")
except Exception as error1:
    buttons = browser.find_elements_by_xpath("//div[@class='top']//span")
    time.sleep(10)


for button in buttons:
    print("text", button.text)

input("请输入任意键继续...")

browser.quit()