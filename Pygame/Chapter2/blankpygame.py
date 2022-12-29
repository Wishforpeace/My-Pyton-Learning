import pygame, sys #导入pygame和sys模块
#import语句 使用这种格式，不是普通的import modulename
from pygame.locals import *
pygame.init()#初始化

DISPLAYSURF = pygame.display.set_mode((400,300)) #400*300的像素窗口
pygame.display.set_caption('Hello world!')
while True:# main game loop  游戏循环和游戏状态
    #游戏循环代码处理三件事：
    #1.处理事件
    #2.更新游戏状态
    #3.在屏幕上绘制游戏状态
    for event in pygame.event.get():#event列表包含了上次调用pygame.event.get()之后所发生的所有事件
        #event对象有一个名为type的成员变量
        #如果Event对象是一个停止事件，就会调用pygame.quit()  sys.exit()函数
        if event.type == QUIT:
            pygame.quit()
        #将pygame.display.set_mode((400,300))所返回的surface对象绘制到屏幕上，
        pygame.display.update()
