import pygame.freetype as pf
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.font = pf.Font("C://Windows//Fonts//msyh.ttc", 48)
        self.text_color = (30, 30, 30)

        # 准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转化为一副渲染的图片"""
        score = round(self.stats.score, -1)
        score_str = 'Score:{:,}'.format(score)
        self.score_image , self.score_rect = self.font.render(
            score_str, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高分转换为渲染的图片"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = 'HighScore:{:,}'.format(high_score)
        self.high_score_image, self.high_score_rect = self.font.render(
            high_score_str, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        level_str = 'Level:' + str(self.stats.level)
        self.level_image, self.level_rect = self.font.render(
            level_str, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示当前得分、最高得分和等级，并绘制剩余飞船"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制剩余飞船
        self.ships.draw(self.screen)
