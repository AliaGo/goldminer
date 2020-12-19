import sys

import pygame
from pygame.locals import QUIT


# 初始化
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('congradulation')  # 命名


background = pygame.image.load('pass.jpg').convert_alpha()  # 背景
background = pygame.transform.scale(background, (800, 700))
screen.blit(background,(0, 0))

congrats = pygame.image.load('frame.png').convert_alpha()
congrats = pygame.transform.scale(congrats, (500, 400))
screen.blit(congrats,(150,100))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
