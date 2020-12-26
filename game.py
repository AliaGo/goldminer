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
curr_goal_text = head_font.render('業績:     $'+str(current_goal), True, (200, 255, 255))

goal = [650,1350,2410,3940,6060,10100]
goal_text = head_font.render('目標業績: $'+str(goal[0]), True, (200, 255, 255))

time_text = head_font.render('時間', True, (200, 255, 255))

level = []
for i in range(0,1000):
    level.append(int(i))
level_text = head_font.render('Level '+str(level[1]), True, (200, 255, 255))

pygame.display.flip()
clock.tick(fps)
ALPHA = (0,0,0)

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
        self.image = pygame.transform.scale(self.image, (50,100))
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
        self.image = pygame.transform.scale(self.image, (70,90))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()


class Level():
    def Criminal(lvl):
        if lvl == 1:
            killer_list = pygame.sprite.Group()
            scammer_list = pygame.sprite.Group()
            stealer_list = pygame.sprite.Group()
            triangle_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [120,650]
            pos_y = [380,350]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [50,340,550]
            pos_y = [250,450,350]
            for i in range(3):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [100,250,380,650,725]
            pos_y = [200,350,230,200,250]
            for i in range(5):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [120,300,500,680]
            pos_y = [280,350,400,300]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            criminal_list.add(killer_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
        if lvl == 2:
            killer_list = pygame.sprite.Group()
            bad_list = pygame.sprite.Group()
            scammer_list = pygame.sprite.Group()
            stealer_list = pygame.sprite.Group()
            triangle_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [30]
            pos_y = [430]
            for i in range(1):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [40,750,500]
            pos_y = [250,500,350]
            for i in range(3):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [100,250,420,610,720]
            pos_y = [200,350,400,170,150]
            for i in range(5):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [30,110,110,650]
            pos_y = [380,250,460,240]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [330,700]
            pos_y = [450,240]
            for i in range(2):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
        if lvl == 3:
            killer_list = pygame.sprite.Group()
            bad_list = pygame.sprite.Group()
            scammer_list = pygame.sprite.Group()
            stealer_list = pygame.sprite.Group()
            triangle_list = pygame.sprite.Group()
            drink_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [150]
            pos_y = [430]
            for i in range(1):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [70,700]
            pos_y = [290,180]
            for i in range(2):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [130,140,190]
            pos_y = [160,225,180]
            for i in range(3):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [125,580,520,640]
            pos_y = [380,180,240,250]
            for i in range(4):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [370]
            pos_y = [260]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [73,583]
            pos_y = [200,230]
            for i in range(2):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)  
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 4:
            killer_list = pygame.sprite.Group()
            bad_list = pygame.sprite.Group()
            scammer_list = pygame.sprite.Group()
            stealer_list = pygame.sprite.Group()
            triangle_list = pygame.sprite.Group()
            drink_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [50,700]
            pos_y = [430,440]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [70]
            pos_y = [270]
            for i in range(1):
                scammer = Scammer()
                scammer.rect.x = pos_x[i]
                scammer.rect.y = pos_y[i]
                scammer_list.add(scammer)
            pos_x = [90,330]
            pos_y = [130,425]
            for i in range(2):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [130,210,650]
            pos_y = [140,390,240]
            for i in range(3):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [240,530]
            pos_y = [450,390]
            for i in range(2):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [33,370,700]
            pos_y = [320,455,290]
            for i in range(3):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)  
            criminal_list.add(killer_list)
            criminal_list.add(bad_list)
            criminal_list.add(scammer_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 5:
            killer_list = pygame.sprite.Group()
            bad_list = pygame.sprite.Group()
            scammer_list = pygame.sprite.Group()
            stealer_list = pygame.sprite.Group()
            triangle_list = pygame.sprite.Group()
            drink_list = pygame.sprite.Group()
            tnt_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [50,660]
            pos_y = [350,440]
            for i in range(2):
                killer = Killer()
                killer.rect.x = pos_x[i]
                killer.rect.y = pos_y[i]
                killer_list.add(killer)
            pos_x = [400]
            pos_y = [300]
            for i in range(1):
                stealer = Stealer()
                stealer.rect.x = pos_x[i]
                stealer.rect.y = pos_y[i]
                stealer_list.add(stealer)
            pos_x = [660]
            pos_y = [230]
            for i in range(1):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [270]
            pos_y = [450]
            for i in range(1):
                bad = Bad()
                bad.rect.x = pos_x[i]
                bad.rect.y = pos_y[i]
                bad_list.add(bad)
            pos_x = [63,180,115,190,400,600,720]
            pos_y = [110,190,485,520,480,250,280]
            for i in range(7):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            pos_x = [100,470]
            pos_y = [130,400]
            for i in range(2):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(killer_list)
            criminal_list.add(tnt_list)
            criminal_list.add(bad_list)
            criminal_list.add(stealer_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        if lvl == 6:
            triangle_list = pygame.sprite.Group()
            drink_list = pygame.sprite.Group()
            tnt_list = pygame.sprite.Group()
            criminal_list = pygame.sprite.Group()
            pos_x = [60]
            pos_y = [300]
            for i in range(1):
                triangle = Triangle()
                triangle.rect.x = pos_x[i]
                triangle.rect.y = pos_y[i]
                triangle_list.add(triangle)
            pos_x = [23,355,480,230,620,400,340,460,740]
            pos_y = [340,150,150,350,350,520,520,520,350]
            for i in range(9):
                drink = Drink()
                drink.rect.x = pos_x[i]
                drink.rect.y = pos_y[i]
                drink_list.add(drink)
            tnt_list = pygame.sprite.Group()
            pos_x = [400,310,480,210,570]
            pos_y = [150,270,270,400,400]
            for i in range(5):
                tnt = Tnt()
                tnt.rect.x = pos_x[i]
                tnt.rect.y = pos_y[i]
                tnt_list.add(tnt)
            criminal_list.add(tnt_list)
            criminal_list.add(triangle_list)
            criminal_list.add(drink_list)
        return criminal_list

criminal_list = Level.Criminal(6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    screen.blit(police,(425,20))
    screen.blit(curr_goal_text, (5, 10))
    screen.blit(goal_text, (5, 50))
    screen.blit(time_text, (650, 10))
    screen.blit(level_text, (650, 50))
    criminal_list.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

