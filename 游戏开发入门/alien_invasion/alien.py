import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load(".\images\\alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储用小数表示的外星人位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """移动外星人"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction

        # 更新表示外星人的rect的位置
        self.rect.x = self.x

    #def blitme(self):
        """在指定位置绘制外星人"""
        #self.screen.blit(self.image, self.rect)
