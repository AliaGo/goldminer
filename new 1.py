import sys

import pygame
from pygame.locals import QUIT


# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
screen = pygame.display.set_mode((800, 600))
# 設置視窗標題
pygame.display.set_caption('警察抓賊')
# 清除畫面並填滿背景色
screen.fill((255, 255, 255))

background = pygame.image.load('background1.png').convert_alpha()
background = pygame.transform.scale(background, (800,600))
screen.blit(background,(0,0))  #对齐的坐标

beginPolice = pygame.image.load('begin.png').convert_alpha()
beginPolice = pygame.transform.scale(beginPolice, (350,350))
screen.blit(beginPolice,(0,50))  #对齐的坐标

# 宣告 font 文字物件
word = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 60)
# 渲染方法會回傳 surface 物件
text_surface = word.render('警察抓犯人', True, (250, 155, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
screen.blit(text_surface, (400, 200))


pygame.mixer.init()
pygame.mixer.music.load('Giornos Theme.mp3')    # 加载背景音乐
pygame.mixer.music.set_volume(0.7)                   # 设置音量
pygame.mixer.music.play(-1)


class Button(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageUp = pygame.transform.scale(self.imageUp, (300,100))
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.imageDown = pygame.transform.scale(self.imageDown, (300,100))
        self.position = position

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))


upImageFilename = 'start.png'
downImageFilename = 'start1.png'
button1 = Button(upImageFilename,downImageFilename, (500, 500))


def Instruction():
    word = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf" ,50)
    text = word.render("遊戲說明:", True, (0,0,70))
    screen.blit(text,(20,10))
    word1 = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf" ,30)
    text1 = word1.render("以鍵盤↓鍵控制手銬去抓犯人，↑鍵控制丟炸彈，", True, (0,0,70))
    screen.blit(text1,(20,90))
    text2 = word1.render("抓到不同的犯人可以得到不同的業績，", True, (0,0,70))
    screen.blit(text2,(20,135))
    text3 = word1.render("若沒在時間限制內超過目標業績則失敗。", True, (0,0,70))
    screen.blit(text3,(20,180))
    text4 = word1.render("每次通關後可在商店購買道具，使下一關更順利，", True, (0,0,70))
    screen.blit(text4,(20,225))
    text5 = word1.render("也可以在賭場進行下注，有一定機率可以直接通關。", True, (0,0,70))
    screen.blit(text5,(20,270))

upImageFilename = 'next.png'
downImageFilename = 'next1.png'
button2 = Button(upImageFilename,downImageFilename, (400, 500))

background1 = pygame.image.load('background3.png').convert_alpha()
background1 = pygame.transform.scale(background1, (800,600))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

stop = ''
# 事件迴圈監聽事件，進行事件處理
while True:
    if '10' not in stop:
        button1.render()
    else:
        screen.fill((255,255,255))
        screen.blit(background, (0, 0))
        Instruction()
        break
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        # get_pressed() 告訴您按下哪個鼠標按鈕
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isOver() is True:
                stop += '1'
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            if button1.isOver() is True:
                stop += '0'
    pygame.display.update()

stop = ''
# 事件迴圈監聽事件，進行事件處理
while True:
    if '10' not in stop:
        button2.render()
    else:
        screen.fill((255,255,255))
        screen.blit(background1, (0, 0))
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        # get_pressed() 告訴您按下哪個鼠標按鈕
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button2.isOver() is True:
                stop += '1'
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            if button2.isOver() is True:
                stop += '0'
    pygame.display.update()