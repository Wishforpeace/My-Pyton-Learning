class Washer():

    # 定义_init_，添加实例属性
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}，高度是{self.height}')


haier1 = Washer()
haier1.print_info()

# _init_()方法自动调用，不需要手动创建
# _init(self)self参数也不需要传递，解释器会自动引用传递
