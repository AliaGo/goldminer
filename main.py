import sys
import pygame
import random
from pygame.locals import *
from sys import exit


# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
screen = pygame.display.set_mode((800, 600))
# 設置視窗標題
pygame.display.set_caption('警察抓犯人')
# 清除畫面並填滿背景色
screen.fill((255, 255, 255))

# 遊戲開始畫面
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

# 背景音樂
pygame.mixer.init()
pygame.mixer.music.load('Giornos Theme.mp3')    # 加载背景音乐
pygame.mixer.music.set_volume(0.7)                   # 设置音量
pygame.mixer.music.play(-1)


# 宣告按鈕
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


# start按鈕
upImageFilename = 'start.png'
downImageFilename = 'start1.png'
button1 = Button(upImageFilename,downImageFilename, (500, 500))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

# 遊戲說明頁面
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

# next按鈕
upImageFilename = 'next.png'
downImageFilename = 'next1.png'
button2 = Button(upImageFilename,downImageFilename, (400, 500))

# 本關目標業績畫面
background1 = pygame.image.load('goal.png').convert_alpha()  # 背景
background1 = pygame.transform.scale(background1, (800, 600))

# 正式遊戲畫面
background2 = pygame.image.load('background3.png').convert_alpha()
background2 = pygame.transform.scale(background2, (800,600))


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
        screen.fill((200,200,200))
        screen.blit(background1,(0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)
        screen.fill((255,255,255))
        pygame.display.update()
        break
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

# 初始化部分
fps = 40
ani = 4
clock = pygame.time.Clock()
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("警察抓犯人")
background = pygame.image.load("background3.png").convert_alpha()
background = pygame.transform.scale(background, (800,600))
# 第一關
police = pygame.image.load("police.png").convert_alpha()
police = pygame.transform.scale(police, (40,70))

# 宣告 font 文字物件
head_font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)
current_goal = 0
curr_goal_text = head_font.render('業績:     $'+str(current_goal), True, (200, 255, 255))

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
        self.image = pygame.transform.scale(self.image, (75,130))
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

counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter >= 0:
                text = str(counter).rjust(3)
            else:
                text = 'times up'
                break
        if event.type == pygame.QUIT: break
    else:
        screen.blit(font.render(text, True, (200, 255, 255)), (720, 10))
        pygame.display.flip()
        clock.tick(20)
        screen.fill((255,255,255))
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
        continue
    break

# 恭喜通關
window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('警察抓犯人')  # 命名


background = pygame.image.load('achieve.png').convert_alpha()  # 背景
background = pygame.transform.scale(background, (800, 600))
window_surface.blit(background,(0, 0))
pygame.display.flip()
pygame.time.wait(2000)

window_surface.fill((255, 255, 255))
# 商店背景
background = pygame.image.load('store2.jpg').convert_alpha()
background = pygame.transform.smoothscale(background, (800,600))

# 下注背景
de_background = pygame.image.load('gamblewithoutdetec.png').convert_alpha()
de_background = pygame.transform.smoothscale(de_background, (800,600))

# 叫字體
notoSans_40 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 40)
notoSans_20 = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 20)

# 讓字換行啦(要講的話)(開始位置)(下移級距)(大小)(顏色)
def blitText(text, position, y_move, fontsize = notoSans_20, color = (41,36,33)):
    blitlist = text.split('\n')
    x = position[0]
    y = position[1]
    for line in blitlist:
        currenttext = fontsize.render(line, True, color)
        window_surface.blit(currenttext, (x,y))
        y += y_move
    return text

class Button(object):
    def __init__(self, upimage, downimage, position , scale):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageUp = pygame.transform.scale(self.imageUp, scale)
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.imageDown = pygame.transform.scale(self.imageDown, scale)
        self.position = position

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        return in_x and in_y

    def render(self, text = None, messenger = None, text_position = None , messenger_position = None, fontsize = notoSans_20, color = (41,36,33)):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            window_surface.blit(self.imageDown, (x,y))
            if messenger != None:
                window_surface.blit(messenger, messenger_position)
            if text != None:                
                blitText(text,text_position,25,fontsize,color)
        else:
            window_surface.blit(self.imageUp, (x,y))

# 叫按鍵
bet = 'bet.png'
bet_pressed = 'bet1.png'
bet_button = Button(bet, bet_pressed, (0,525), (150, 75))

passbuttom = 'pass.png'
passbuttom_pressed = 'pass1.png'
passbuttom = Button(passbuttom, passbuttom_pressed, (0,0), (150, 75))

b2store = 'store button.png'
b2store_pressed = 'store button dark.png'
b2store_button = Button(b2store, b2store_pressed, (0,0), (150, 75))

# 叫對話框
messenger = pygame.image.load('text.png')
messenger = pygame.transform.scale(messenger, (350,350))
g_messenger = pygame.image.load('—Pngtree—certificate border_2241181.png')
g_messenger = pygame.transform.scale(g_messenger, (600,180))

# 叫道具
boom = 'boom.png'
boom_pressed = 'boom ver.dark.png'
boom_scale = (90,108)

clock = 'clock.png'
clock_pressed = 'clock ver.dark.png'
clock_scale = (100,100)

donut = 'donut.png'
donut_pressed = 'donut ver.dark.png'
donut_scale = (125,100)

remove = 'remove.png'
remove_pressed = 'remove ver.dark.png'
remove_scale = (100,100)

#叫偵探
dec1 = "detective1.png"
dec1_pressed = 'detective1 dark.png'
dec1_scale = (140,140) 
dec1_buttom = Button(dec1, dec1_pressed, (80, 150), dec1_scale)

dec2 = "detective5.png"
dec2_pressed = 'detective5 dark.png'
dec2_scale = (150,150) 
dec2_buttom = Button(dec2, dec2_pressed, (235, 145), dec2_scale)

dec3 = "detective3.png"
dec3_pressed = 'detective3 dark.png'
dec3_scale = (160,160) 
dec3_buttom = Button(dec3, dec3_pressed, (400, 135), dec3_scale)


dec4 = "detective4.png"
dec4_pressed = 'detective4 dark.png'
dec4_scale = (140,140)
dec4_buttom = Button(dec4, dec4_pressed, (560, 150), dec4_scale)

#建偵探字
d1_text = '成功機率巴'
d2_text = '成功機率巴拉'
d3_text = '成功機率巴拉拉'
d4_text = '成功機率巴拉拉拉'

#建偵探字tuple
decs_text_tuple = [(dec1_buttom, d1_text), (dec2_buttom, d2_text), (dec3_buttom, d3_text), (dec4_buttom, d4_text)]
  
# 叫價錢版
pricetag = pygame.image.load('price2.png')
pricetag =  pygame.transform.smoothscale(pricetag, (130,65))
g_pricetag = pygame.image.load('price4.png')
g_pricetag = pygame.transform.smoothscale(g_pricetag, (130,65))

# 產生隨機價錢
def randomprice():
    k1 = random.randint(1,500)
    randomprice = '$' + str(k1)
    price = notoSans_40.render(randomprice, True, (255,245,238))
    return price
    
#建現在資金
money = notoSans_40.render('$現在金額', True, (255,250,250))

#建偵探價格
d1_price =  notoSans_20.render('$500', True, (255,250,250))
d2_price =  notoSans_20.render('$700', True, (255,250,250))
d3_price =  notoSans_20.render('$900', True, (255,250,250))
d4_price =  notoSans_20.render('$1100', True, (255,250,250))



# 產生隨機道具
k = random.randint(2,3)

items = [(boom, boom_pressed , boom_scale), (clock, clock_pressed, clock_scale), (donut,donut_pressed, donut_scale), (remove,remove_pressed, remove_scale)]
currentitems = random.sample(items, k)

for i, item in enumerate(currentitems):
    if i == 0:
        item1 = item[0]
        item_buttom1 = Button(item[0], item[1], (200,100), item[2] )
        price1 = randomprice()
        currentitems[0] = (item1, item_buttom1)         
    elif i == 1:
        item2 = item[0]
        item_buttom2 = Button(item[0], item[1], (200,230), item[2] )
        price2 = randomprice()
        currentitems[1] = (item2, item_buttom2)
        item_num = 2
    elif i == 2:
        item3 = item[0]
        item_buttom3 = Button(item[0], item[1], (200,380), item[2] )
        price3 = randomprice()
        currentitems[2] = (item3, item_buttom3)
        item_num = 3

# 博士要說的話
def whichitem(item):
    if item == boom:
        text = '炸掉手銬上不想通\n緝的人物或物品，\n可節省時間抓其他\n犯人。'
    elif item == clock:
        text = '時間暫停。'
    elif item == donut:
        text = '加快抓到犯人的速\n度。'
    elif item == remove:
        text = '拆除地圖上的TNT。'
    return text

stop = []
# 事件迴圈監聽事件，進行事件處理
while True:
    if '1' not in stop and '0' not in stop:
        window_surface.blit(background,(0,0))
        bet_button.render()
        passbuttom.render()
        window_surface.blit(money, (550,0))
        if item_num == 2:
            window_surface.blit(pricetag, (320,100))
            window_surface.blit(price1, (345, 105))
            window_surface.blit(pricetag, (320,230))
            window_surface.blit(price2, (345, 235))
        elif item_num == 3:
            window_surface.blit(pricetag, (320,100))
            window_surface.blit(price1, (345, 105))
            window_surface.blit(pricetag, (320,230))
            window_surface.blit(price2, (345, 235))
            window_surface.blit(pricetag, (320,360))
            window_surface.blit(price3, (345, 365))
        for item_tuple in currentitems:
            text = whichitem(item_tuple[0])
            item_tuple[1].render(text,messenger, (525,150), (430,50),notoSans_20,(41,36,33))        
    else:
        window_surface.blit(de_background, (0, 0))
        window_surface.blit(money, (550,0))
        b2store_button.render()
        dec1_buttom.render()
        dec2_buttom.render()
        dec3_buttom.render()
        dec4_buttom.render()
        window_surface.blit(g_pricetag, (85,350))
        window_surface.blit(g_pricetag, (250,350))
        window_surface.blit(g_pricetag, (400,350))
        window_surface.blit(g_pricetag, (550,350))
        window_surface.blit(g_messenger, (100,400))
        window_surface.blit(d1_price, (100,350))
        window_surface.blit(d2_price, (265,350))
        window_surface.blit(d3_price, (410,350))
        window_surface.blit(d4_price, (565,350))
        for currentdec in decs_text_tuple:
            currentdec[0].render(text = currentdec[1], text_position = (130, 430),fontsize = notoSans_40,color = (255,250,250))
        
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        # get_pressed() 告訴您按下哪個鼠標按鈕
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bet_button.isOver() is True:
                stop.append('1')
            elif b2store_button.isOver() is True:
                stop.remove('1')
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            if bet_button.isOver() is True:
                stop.append('0')
            elif b2store_button.isOver() is True:
                stop.remove('0')
    pygame.display.update()
