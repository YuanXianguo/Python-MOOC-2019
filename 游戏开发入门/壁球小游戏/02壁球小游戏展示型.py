import sys, pygame

# 初始化
pygame.init()
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame壁球')
# pygame.image.load(filename),将filename路径下的图像载入游戏，支持JPG、PNG、GIF(非动画)等13种常用图片格式
ball = pygame.image.load('PYG02-ball.gif')
# Pygame使用内部定义的Surface对象表示所有载入的图像，.get_rect()方法返回一个覆盖图像的矩形Rect对象
# Rect对象有一些重要属性，例如：top,bottom,left,right表示上下左右；width,height表示宽度、高度
ball_rect = ball.get_rect()
while True:  # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # .move(x,y),矩形移动一个偏移量(x,y)，即在横轴方向移动x像素，纵轴方向移动y像素，x,y均为整数
    ball_rect = ball_rect.move(speed[0], speed[1])
    # 矩形的反弹运动，遇到上下左右边界速度取反
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = - speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = - speed[1]
    # 窗口刷新
    # screen.fill(color),显示窗口背景填充为color颜色，采用RGB色彩体系
    # 由于壁球不断运动，运动后原有位置将默认填充白色，因此需要不断刷新背景色
    screen.fill(BLACK)
    # screen.blit(src,dest),将一个图像绘制在另一个图像上，即将src绘制到dest位置上；
    # 通过Rect对象引导对壁球的绘制
    screen.blit(ball, ball_rect)
    pygame.display.update()
