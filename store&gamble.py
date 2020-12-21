import pygame, random, sys

pygame.init()

window_surface = pygame.display.set_mode((800, 600))

pygame.display.set_caption('警察抓賊-商店')
window_surface.fill((255, 255, 255))

# 商店背景
background = pygame.image.load('store1.png').convert_alpha()
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
    k1 = random.randint(30,500)
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

    