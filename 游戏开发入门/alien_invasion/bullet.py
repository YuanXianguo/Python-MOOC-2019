import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship

        # 在（0，0）出创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width, self.ai_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        # 子弹颜色设置
        self.color = self.ai_settings.bullet_color

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.ai_settings.bullet_speed_factor

        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在指定位置绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
