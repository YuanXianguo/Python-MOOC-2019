import pygame
import sys
from math import pi

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame图形绘制')
gold = 255, 251, 0
red = pygame.Color('red')
white = 255, 255, 255
green = pygame.Color('green')

e1 = pygame.draw.ellipse(screen, green, (50, 50, 500, 300), 3)
c1 = pygame.draw.circle(screen, gold, (200, 180), 30, 5)
c2 = pygame.draw.circle(screen, gold, (400, 180), 30)
r1 = pygame.draw.rect(screen, red, (170, 130, 60, 10), 3)
r2 = pygame.draw.rect(screen, red, (370, 130, 60, 10))
plist = [(295, 170), (285, 250), (260, 280), (340, 280), (315, 250), (305, 170)]
l1 = pygame.draw.lines(screen, gold, True, plist, 2)
a1 = pygame.draw.arc(screen, red, (200, 220, 200, 100), 1.4*pi, 1.9*pi, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()


