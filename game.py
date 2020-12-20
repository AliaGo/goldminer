# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import sys

# 初始化部分
fps = 40
ani = 4
clock = pygame.time.Clock()
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("criminal")
background = pygame.image.load("background3.png").convert_alpha()
background = pygame.transform.scale(background, (800,600))

police = pygame.image.load("police.png").convert_alpha()
police = pygame.transform.scale(police, (40,70))

# 宣告 font 文字物件
head_font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
# 渲染方法會回傳 surface 物件
current_goal = 0
curr_goal_text = head_font.render('業績:   $'+str(current_goal), True, (200, 255, 255))

goal = 650
goal_text = head_font.render('目標業績: $'+str(goal), True, (200, 255, 255))

time_text = head_font.render('時間', True, (200, 255, 255))

level = []
for i in range(1,1000):
    level.append(int(i))
level_text = head_font.render('Level '+str(level[0]), True, (200, 255, 255))

pygame.display.flip()
clock.tick(fps)


class Killer(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('killer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,130))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Bad(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bad.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,130))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Scammer(pygame.sprite.Sprite):  
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('scammer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Stealer(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('stealer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25,35))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Triangle(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('triangle.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,38))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Drink(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('drink.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,38))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Reporter(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('reporter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,130))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Tnt(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tnt.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,130))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


ALPHA = (0,0,0)

killer_list = pygame.sprite.Group()
pos_x = [120,650]
pos_y = [380,350]
for i in range(2):
    killer = Killer()
    killer.rect.x = pos_x[i]
    killer.rect.y = pos_y[i]
    killer_list.add(killer)


scammer_list = pygame.sprite.Group()
pos_x = [50,340,550]
pos_y = [250,450,350]
for i in range(3):
    scammer = Scammer()
    scammer.rect.x = pos_x[i]
    scammer.rect.y = pos_y[i]
    scammer_list.add(scammer)


stealer_list = pygame.sprite.Group()
pos_x = [100,250,380,650,725]
pos_y = [200,350,230,200,250]
for i in range(5):
    stealer = Stealer()
    stealer.rect.x = pos_x[i]
    stealer.rect.y = pos_y[i]
    stealer_list.add(stealer)

triangle_list = pygame.sprite.Group()
pos_x = [120,300,500,680]
pos_y = [280,350,400,300]
for i in range(4):
    triangle = Triangle()
    triangle.rect.x = pos_x[i]
    triangle.rect.y = pos_y[i]
    triangle_list.add(triangle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background,(0,0))
    screen.blit(police,(425,20))
    screen.blit(curr_goal_text, (5, 10))
    screen.blit(goal_text, (5, 50))
    screen.blit(time_text, (650, 10))
    screen.blit(level_text, (650, 50))
    killer_list.draw(screen)
    scammer_list.draw(screen)
    stealer_list.draw(screen)
    triangle_list.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
