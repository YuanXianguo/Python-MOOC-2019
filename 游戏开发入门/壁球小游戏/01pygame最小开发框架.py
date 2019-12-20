import pygame
import sys  # sys是Python的标准库，提供Python运行时环境变量的操控

pygame.init()  # 对Pygame内部各功能模块进行初始化创建及变量设置，默认调用
# 初始化显示窗口，第一个参数size是一个二值元组，分别表示窗口的宽度和高度
screen = pygame.display.set_mode((600, 400))
# 设置显示窗口的标题内容，参数title是一个字符串类型
pygame.display.set_caption('Pygame游戏之旅')

while True:
    # 从Pygame的事件队列中取出事件，并从队列中删除该事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()  # 对显示窗口进行刷新，默认窗口全部重绘


