# 导入模块
import pygame
from pygame.locals import *
from sys import exit

# 初始化部分
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My moving handcuff")
background = pygame.image.load("background2.png").convert()

# 坦克精灵类
tank_image = pygame.image.load('handcuff.png').convert_alpha()

class HeroTank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tank_image = tank_image
        self.tank_rect = self.tank_image.get_rect()
        self.speed = 8

    def moveLeft(self):
        if self.tank_rect.left > 0:
            self.tank_rect.x -= self.speed
        self.rotate(270)

    def moveRight(self):
        if self.tank_rect.right < 640:
            self.tank_rect.x += self.speed
        self.rotate(90)

    def moveUp(self):
        if self.tank_rect.top > 0:
            self.tank_rect.y -= self.speed
        self.rotate(180)

    def moveDown(self):
        if self.tank_rect.bottom < 480:
            self.tank_rect.y += self.speed
        self.rotate(0)

    def rotate(self, angle):
        # 选择机身
        self.tank_image = pygame.transform.rotate(tank_image, angle)
        self.tank_rect = self.tank_image.get_rect(center=self.tank_rect.center)

    def display(self, screen):
        screen.blit(self.tank_image, self.tank_rect)

my_tank = HeroTank()
framerate = pygame.time.Clock()
angel = 0

while True:
    framerate .tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    key_press = pygame.key.get_pressed()
    if key_press[K_w]:
        my_tank.moveUp()
    elif key_press[K_s]:
        my_tank.moveDown()
    elif key_press[K_a]:
        my_tank.moveLeft()
    elif key_press[K_d]:
        my_tank.moveRight()
    screen.blit(background, (0, 0))
    my_tank.rotate(angel)
    angel += 1
    my_tank.display(screen)
    pygame.display.update()
