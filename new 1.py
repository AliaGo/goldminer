import sys

import pygame
from pygame.locals import QUIT


# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
window_surface = pygame.display.set_mode((800, 600))
# 設置視窗標題
pygame.display.set_caption('警察抓賊')
# 清除畫面並填滿背景色
# window_surface.fill((255, 255, 255))

background = pygame.image.load('背景淡藍.jpg').convert_alpha()
background = pygame.transform.scale(background, (800,600))
window_surface.blit(background,(0,0))  #对齐的坐标

beginPolice = pygame.image.load('begin.png').convert_alpha()
beginPolice = pygame.transform.scale(beginPolice, (350,350))
window_surface.blit(beginPolice,(0,50))  #对齐的坐标

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('find criminals', True, (250, 155, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (400, 200))


pygame.mixer.init()
pygame.mixer.music.load('Giornos Theme.mp3')    # 加载背景音乐
pygame.mixer.music.set_volume(0.7)                   # 设置音量
pygame.mixer.music.play(-1)


upImageFilename = 'start.png'
downImageFilename = 'start1.png'

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
            window_surface.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            window_surface.blit(self.imageUp, (x-w/2, y-h/2))

button = Button(upImageFilename,downImageFilename, (500, 500))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()



# 事件迴圈監聽事件，進行事件處理
while True:
    button.render()
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        # get_pressed() 告訴您按下哪個鼠標按鈕
        elif event.type == pygame.MOUSEBUTTONDOWN:
            window_surface.blit(background,(0,0))
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            window_surface.blit(background,(0,0))
    pygame.display.update()