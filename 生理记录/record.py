import xlrd
import xlwt
from xlutils.copy import copy
import datetime
import random


def write_excel_title(excel_path, value):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("record")
    for i in range(0, len(value)):
        sheet.write(0, i, value[i])
    workbook.save(excel_path)
    print("successfully written title")

    # def write_temperature():
    #     for i in random()


def write_date(excel_path):
    workbook = xlrd.open_workbook(excel_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    for i in range(1, 31):
        Date = str(datetime.date(2022, 9, i))
        new_worksheet.write(i, 0, Date, )

    for i in range(1, 32):
        Date = str(datetime.date(2022, 10, i))
        new_worksheet.write(i + 30, 0, Date)

    for i in range(1, 31):
        Date = str(datetime.date(2022, 11, i))
        new_worksheet.write(i + 61, 0, Date)

    for i in range(1, 17):
        Date = str(datetime.date(2022, 12, i))
        new_worksheet.write(i + 91, 0, Date)
    new_workbook.save(excel_path)

    print("Date write success")


def write_temperature(excel_path):
    workbook = xlrd.open_workbook(excel_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_workbooksheet = new_workbook.get_sheet(0)
    for i in range(1, 108):
        new_workbooksheet.write(i, 1, round(random.uniform(36.3, 36.9), 1))
    new_workbook.save(excel_path)
    print("Temperature write success")


def write_sleep(excel_path):
    workbook = xlrd.open_workbook(excel_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_workbooksheet = new_workbook.get_sheet(0)
    for i in range(1, 108):
        new_workbooksheet.write(i, 2, round(random.uniform(5.5, 8.5), 1))
    new_workbook.save(excel_path)
    print("Sleep write success")


def write_food(excel_path, col_num, food):
    workbook = xlrd.open_workbook(excel_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_workbooksheet = new_workbook.get_sheet(0)

    for i in range(1, 108):
        food_num = random.randint(0, len(food) - 1)
        new_workbooksheet.write(i, col_num, food[food_num])
    new_workbook.save(excel_path)
    print("Food write success")


def write_sport(excel_path, sport):
    workbook = xlrd.open_workbook(excel_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    new_workbook = copy(workbook)
    new_workbooksheet = new_workbook.get_sheet(0)
    for i in range(5, 95):
        row = i + random.randint(-5, 5)
        sport_num = random.randint(0, len(sport) - 1)
        new_workbooksheet.write(row, 6, sport[sport_num][0])
        new_workbooksheet.write(row, 7, sport[sport_num][1])
    new_workbook.save(excel_path)
    print("Sport write success")

path = "record.xls"
value_title = ["日期", "体温", "睡眠", "饮食-早餐", "饮食-午餐", "饮食-晚餐", "户外运动内容", "户外运动时长"]
breakfast = ["肉包、稀饭", "热干面、煎鸡蛋", "热干面、豆浆", "肉包、豆浆", "鸡蛋、豆浆", "油条、稀饭", "鸡蛋、油条、豆浆", "热干面、菜包", "菜包、肉包、豆浆", "酱香饼、豆浆",
             "欧包、咖啡", "热干面、咖啡", "咖啡、鸡蛋", "没吃"]
lunch = ["肉类：2种，蔬菜：1种，主食：米饭", "肉类：1种。蔬菜：0种，主食：面条", "肉类：0种、蔬菜：2种,主食：米饭", "肉类：2种，蔬菜：三种，主食：水饺", "肉类：三种，蔬菜：3种"
    , "肉类：1种，蔬菜：2两种，主食：方便面", "肉类：1种，蔬菜：三种，主食：米饭", "肉类；3种，蔬菜：3种，主食：米线"]
dinner = ["蔬菜：1种，主食：稀饭", "肉类：2种，主食：面条", "肉类：1种，蔬菜：3种，主食：米饭", "肉类：3种，蔬菜：3种，主食：水饺",
          "肉类：1种，蔬菜：1种，主食：米线", "肉类：2种，蔬菜：2两种，主食：面条", "肉类：4种，蔬菜：3种", "肉类：1种，蔬菜：1种，主食：稀饭",
                                                                    "肉类：0，蔬菜：0，主食：面包", "肉类：0，蔬菜：0，没吃晚饭"]

sport = [["跑步", "30min"], ["篮球", "1h"], ["跑步", "10min"], ["跑步", "15min"], ["篮球", "30min"], ["篮球", "35min"],
         ["篮球", "1.5h"], ["篮球", "45min"]]
write_excel_title(path, value_title)
write_date(path)
write_temperature(path)
write_sleep(path)
write_food(path, 3, breakfast)
write_food(path, 4, lunch)
write_food(path, 5, dinner)
write_sport(path, sport)
