class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def printf_info(self):
        print(f'洗衣机的宽度为{self.width}')
        print(f'洗衣机的高度为{self.height}')


haier1 = Washer(10, 20)
haier1.printf_info()

haier2 = Washer(30, 40)
haier2.printf_info()
