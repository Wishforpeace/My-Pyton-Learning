from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import xlwt
import time

wait_time = 10


def get_source():
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


def next_page(page_num):
    WAIT = ui.WebDriverWait(browser, 5)
    try:
        next_btn = WAIT.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='i_cecream']/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button[10]")))
        next_btn.click()
        WAIT.until(EC.text_to_be_present_in_element(
            (By.XPATH,
             "//button[@class = 'vui_button vui_button--active vui_button--active-blue vui_button--no-transition vui_pagenation--btn vui_pagenation--btn-num']"),
            str(page_num)
        ))
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)


def save_to_excel(soup):
    infos = soup.find_all(class_='bili-video-card')
    for info in infos:
        print("info\n",info)
        title = info.find('h3').get('title')
        href = info.find('a').get('href')
        date = info.find(class_='bili-video-card__info--date').text.strip()
        up = info.find(class_='bili-video-card__info--author').string.strip()

        global n
        sheet.write(n, 0, title)
        sheet.write(n, 1, date)
        sheet.write(n, 2, up)
        sheet.write(n, 3, href)
        n += 1


if __name__ == '__main__':
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()

    n = 1
    excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
    content = input("输入你要查询的内容")
    sheet = excel.add_sheet(content, cell_overwrite_ok=True)
    sheet.write(0, 0, '标题')
    sheet.write(0, 1, '上传时间')
    sheet.write(0, 2, 'up主')
    sheet.write(0, 3, '视频链接')

    input("请输入任意键继续......")
    browser.get('https://www.bilibili.com/')
    time.sleep(1)
    # 刷新一下，防止搜索button被登录弹框遮住
    browser.refresh()
    input("按回车开始搜索......")
    input_content = browser.find_element(By.XPATH, "//input[@class='nav-search-input']")
    button = browser.find_element(By.XPATH, "//div[@class='nav-search-btn']")
    print(browser.current_url)
    input_content.send_keys(content)
    button.click()
    time.sleep(1)
    all_h = browser.window_handles
    browser.switch_to.window(all_h[1])

    wait = ui.WebDriverWait(browser, wait_time)
    try:
        wait.until(lambda driver: driver.find_elements(By.XPATH,
                                                       "//*[@id='i_cecream']/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button"))
        total_btn = browser.find_elements(By.XPATH,
                                          "//*[@id='i_cecream']/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button")
    except Exception as error1:
        total_btn = browser.find_elements(By.XPATH,
                                          "//*[@id='i_cecream']/div[1]/div[1]/div[2]/div/div/div[2]/div/div/button")
        time.sleep(10)

    count = 0
    for total in total_btn:
        count += 1
        print(total.text)

    all = int(total_btn[count - 2].text)

    get_source()
    for i in range(2, 6):
        next_page(i)

    filename = content + '.xls'
    excel.save(filename)

    input("按任意键退出......")

    browser.quit()

    print(f'共爬取了{n - 1}调信息')
