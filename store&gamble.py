import pygame
import random

pygame.init()

window_surface = pygame.display.set_mode((800, 600))

pygame.display.set_caption('警察抓賊-商店')
window_surface.fill((255, 255, 255))

# 商店背景
background = pygame.image.load('store1.png').convert_alpha()
background = pygame.transform.smoothscale(background, (800,600))
window_surface.blit(background,(0,0))

# 下注背景
de_background = pygame.image.load('gamblewithoutdetec.png').convert_alpha()
de_background = pygame.transform.smoothscale(de_background, (800,600))

#叫按鍵
bet = 'bet.png'
bet_pressed = 'bet1.png'
passbuttom = 'pass.png'
passbuttom_pressed = 'pass1.png'
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

    def render(self, text = ''):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            window_surface.blit(self.imageDown, (x,y))
            if text != '':
                window_surface.blit(text, (500,100))
        else:
            window_surface.blit(self.imageUp, (x,y))

bet_button = Button(bet, bet_pressed, (0,525), (150, 75))
passbuttom = Button(passbuttom, passbuttom_pressed, (0,0), (150, 75))

# 叫對話框
messenger = pygame.image.load('text.png')
messenger = pygame.transform.scale(messenger, (300,300))
window_surface.blit(messenger, (450,80))

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
dec1_pressed = 'price1.png'
dec1_scale = (140,140) 
dec1_buttom = Button(dec1, dec1_pressed, (80, 150), dec1_scale)

dec2 = "detective5.png"
dec2_pressed = 'price2.png'
dec2_scale = (150,150) 
dec2_buttom = Button(dec2, dec2_pressed, (235, 145), dec2_scale)

dec3 = "detective3.png"
dec3_pressed = 'price3.png'
dec3_scale = (160,160) 
dec3_buttom = Button(dec3, dec3_pressed, (400, 135), dec3_scale)


dec4 = "detective4.png"
dec4_pressed = 'price4.png'
dec4_scale = (140,140)
dec4_buttom = Button(dec4, dec4_pressed, (560, 150), dec4_scale)
 
# 叫價錢版
pricetag = pygame.image.load('price2.png')
pricetag =  pygame.transform.smoothscale(pricetag, (130,65))
g_pricetag = pygame.image.load('price4.png')
g_pricetag = pygame.transform.smoothscale(g_pricetag, (130,65))

# 叫字體
notoSans = pygame.font.Font('NotoSansMonoCJKtc-Bold.otf', 40)

# 產生隨機價錢
def randomprice():
    k1 = random.randint(1,500)
    randomprice = '$' + str(k1)
    price = notoSans.render(randomprice, True, (255,245,238))
    return price

# 產生隨機道具
k = random.randint(2,3)

items = [(boom, boom_pressed , boom_scale), (clock, clock_pressed, clock_scale), (donut,donut_pressed, donut_scale), (remove,remove_pressed, remove_scale)]
currentitems = random.sample(items, k)

for i, item in enumerate(currentitems):
    if i == 0:
        item1 = item[0]
        item_buttom1 = Button(item[0], item[1], (200,100), item[2] )
        window_surface.blit(pricetag, (320,100))
        price = randomprice()
        window_surface.blit(price, (345, 105))
        currentitems[0] = (item1, item_buttom1)        
    elif i == 1:
        item2 = item[0]
        item_buttom2 = Button(item[0], item[1], (200,230), item[2] )
        window_surface.blit(pricetag, (320,230))
        price = randomprice()
        window_surface.blit(price, (345, 235))
        currentitems[1] = (item2, item_buttom2)
    elif i == 2:
        item3 = item[0]
        item_buttom3 = Button(item[0], item[1], (200,380), item[2] )
        window_surface.blit(pricetag, (320,360))
        price = randomprice()
        window_surface.blit(price, (345, 365))
        currentitems[2] = (item3, item_buttom3)
pygame.display.update()

# 博士要說的話
def whichitem(item):
    if item == boom:
        text = notoSans.render('炸掉手銬上不想通緝的人物或物品，可節省時間抓其他犯人。', True, (255,245,238))
    elif item == clock:
        text = notoSans.render('時間暫停。', True, (255,245,238))
    elif item == donut:
        text = notoSans.render('加快抓到犯人的速度。', True, (255,245,238))
    elif item == remove:
        text = notoSans.render('拆除地圖上的TNT。', True, (255,245,238))
    return text

stop = ''
# 事件迴圈監聽事件，進行事件處理
while True:
    if '10' not in stop:
        bet_button.render()
        passbuttom.render()
        for item_tuple in currentitems:
            text = whichitem(item_tuple[0])
            item_tuple[1].render(text)        
    else:
        window_surface.blit(de_background, (0, 0))
        dec1_buttom.render()
        dec2_buttom.render()
        dec3_buttom.render()
        dec4_buttom.render()
        window_surface.blit(g_pricetag, (85,350))
        window_surface.blit(g_pricetag, (250,350))
        window_surface.blit(g_pricetag, (400,350))
        window_surface.blit(g_pricetag, (550,350))
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            sys.exit()
        # get_pressed() 告訴您按下哪個鼠標按鈕
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bet_button.isOver() is True:
                stop += '1'
        # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            if bet_button.isOver() is True:
                stop += '0'
    pygame.display.update()
    