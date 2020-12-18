import sys

import pygame
from pygame.locals import QUIT


# 初始化
pygame.init()

screen = pygame.display.set_mode((400, 300))  # 打字框
pygame.display.set_caption('Keybroad Example')  # 命名
pygame.display.update()


clock= pygame.time.Clock()
font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 60)  # 字體設置
background = pygame.image.load('background.jpg').convert_alpha()  # 背景
background = pygame.transform.scale(background, (400, 300))
screen.blit(background,(0, 0))

pygame.display.update()



def objectText(object_str):  # 目標文字
    # 渲染方法會回傳 surface 物件
    text = font.render(object_str, True, (250, 155, 0))
    # blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
    screen.blit(text, (0, 0))

    pygame.display.update()

def drawText(command):  # 使用者打字(印)
    text = font.render(command,True,(255,255,255))
    screen.blit(background,(0, 0))
    screen.blit(text,
                (100, 200-text.get_height() // 2))
    objectText(object_str)
    
    pygame.display.update()

object_str = 'find'  # 目標字
str = ''
while True:
    objectText(object_str)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:  # 沒打完不能走
            pass
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # ENTER鍵輸入(正確才離開)
                if str == object_str:
                    sys.exit()
                    pygame.quit()
                else:
                    pass
            elif event.key == pygame.K_BACKSPACE:  # 刪除鍵
                str = str[:-1]
                drawText(str)
            else:  # 其他
                str += chr(event.key)
                drawText(str)


