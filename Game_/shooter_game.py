from pygame import *#импорт библиотеки
from random import *

class GameSprite(sprite.Sprite):#класс
    def __init__(self, image_sprite, img_x, img_y, speed, hight, width):#ввод значений 
        super().__init__()##указывает на себя всё из класса родителя
        self.image = transform.scale(image.load(image_sprite), (65,65))#указывает на себя картинку
        self.speed = speed#указывает на себя скорость
        self.rect = self.image.get_rect()#указывает на себя
        self.rect.x = img_x#указывает на себя х
        self.rect.y = img_y#указывает на себя у

    def show_s(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>5:
            self.rect.x -=self.speed
        if keys[K_d] and self.rect.x<win_width-80:
            self.rect.x +=self.speed
    def fire(self):
            pulya=Bullet(img_bullet, self.rect.centerx, self.rect.top, 15,20,15)
            bulets.add(pulya)

class Enemy(GameSprite):
    def update(self):
        global prop
        self.rect.y+=self.speed
        if self.rect.y>win_width:
            self.rect.y=0
            self.rect.x=randint(50,win_hight-50)

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<0:
            self.kill()




win_width = 700
win_hight = 500




window = display.set_mode((win_width, win_hight))
display.set_caption("ConterStiric")

background = transform.scale(image.load("galaxy.jpg"), (win_width,win_hight))
corable = Player('rocket.png',300,400,7,100,100)
img_bullet = 'bullet.png'

monsters = sprite.Group()
bulets = sprite.Group()

for i in range(6):
    en1 = Enemy("ufo.png", randint(50, win_width-50), -50, randint(1,3),80,50)
    monsters.add(en1)


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

run = True
finish = False

clock = time.Clock()

score=0

font.init()
font=font.Font(None,36)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

while run:

    keys = key.get_pressed()

    for i in event.get():
            if i.type == QUIT:
                run = False
            if i.type == KEYDOWN:
                if i.key==K_SPACE:
                    corable.fire()

    if finish!=True:
        window.blit(background,(0,0))

        corable.show_s()
        corable.update()

        monsters.update()
        monsters.draw(window)

        bulets.update()
        bulets.draw(window)

        collides=sprite.groupcollide(monsters, bulets, True, True)

        for i in collides:
            score+=1
            en1 = Enemy("ufo.png", randint(50, win_width-50), -50, randint(1,3),80,50)
            monsters.add(en1)

        if sprite.spritecollide(corable, monsters,  False):
            finish=True

        text_score=font.render("Счёт: "+str(score), 1, (255,255,255))
        window.blit(text_score,(10,20))

        display.update()
    else:
        finish=False
        score=0
        for b in bulets:
            b.kill()
        for m in monsters:
            m.kill()

        time.delay(50)

        
        for i in range(6):
            en1 = Enemy("ufo.png", randint(50, win_width-50), -50, randint(1,3),80,50)
            monsters.add(en1)

    clock.tick(60)