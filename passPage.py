import sys

import pygame
from pygame.locals import QUIT


# 初始化
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('congradulation')  # 命名


background = pygame.image.load('achieve.png').convert_alpha()  # 背景
background = pygame.transform.scale(background, (800, 600))
screen.blit(background,(0, 0))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
