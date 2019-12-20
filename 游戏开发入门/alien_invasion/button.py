import pygame.freetype as pf

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.msg = msg

        # 设置按钮属性
        self.font = pf.Font("C://Windows//Fonts//msyh.ttc", 48)
        self.text_color = (255, 255, 255)
        self.bg_color = (130, 130, 130)

        # 准备按钮图像
        self.prep_msg()

    def prep_msg(self):
        """创建按钮的图像对象和rect对象，并使其居中"""
        self.font_image, self.font_rect = self.font.render(
            self.msg, self.text_color, self.bg_color)
        self.font_rect.center = self.screen_rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.blit(self.font_image, self.font_rect)


