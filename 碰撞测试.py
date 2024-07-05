import pygame
import sys
from pygame.locals import *
from pygame.sprite import Sprite
import time
import random
pygame.init()

pygame.display.set_caption("逆行飙车")
screen = pygame.display.set_mode((700, 700)) #设置当前窗口的高宽

#1. 角色不能超出边界
#2. 碰撞画面不真实
#3 难度随着时间流逝而增加

screen_width = screen.get_width()
screen_height = screen.get_height()
#类的定义
SCORE = 0
SPEED = 5    #敌人的运动速度
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        x, y =screen_width//2, screen_height//2
        self.image = pygame.image.load("rotated_player.jpg")
        self.surf = pygame.Surface((40,50))
        self.rect = self.surf.get_rect(left = 178, bottom= screen_height - 50)  #默认是(0, 0 )
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= screen_height - 21:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right <= screen_width - 4:
            self.rect.move_ip(5,0)
        if pressed_keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-5,0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #调用父类的函数
        super(Enemy,self).__init__()
        #随机生成敌人的X坐标
        x, y =(random.randint(100, 378), 0)
        #生成图片
        self.image = pygame.image.load("rotated_enemy.jpg")
        #生成一个矩形区域
        self.surf = pygame.Surface((40,50))
        #返回pygame react对象
        self.rect = self.surf.get_rect(center = (x,y))  #默认是(0, 0 )
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.top > screen_height:
            SCORE += 1
            self.rect.top = 0
            self.rect.left = random.randint(22,378)

#颜色

white = pygame.color.Color(255,255,255) # 定义颜色
black = (0,0,0)
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = (0,0,255)

#设置图像的帧速率
FPS = 30 
clock= pygame.time.Clock()


#定义用户事件
SPEED_UP = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED_UP, 1000)   #每隔1000毫秒就将事件编码放到事件队列中1次
#设置字体和文字
print(black)
font_big = pygame.font.SysFont("微软雅黑", 60)
font_small = pygame.font.SysFont("Verdana", 80)
game_over = font_small.render("GAMEOVER", True, black)
print(game_over)


#1. 角色类型继承Sprite 
#2. 应用父类__init__方法初始化对象
#3. 定义精灵组
#4. 碰撞检测以及处理
background =pygame.image.load("780.jpg")
player = Player()
enemy = Enemy()
enemy2 = Enemy()

#定义精灵组
enemies = pygame.sprite.Group()
enemies.add(enemy)
enemies.add(enemy2)

#将所有的精灵放到一个组中
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(enemy2)
while True:#为了保留窗口需要while loop一直进行循环
    screen.blit(background, (0,0))
    scores = font_small.render(str(SCORE),True, black)
    screen.blit(scores, (10,10))
    #统一对所有的精灵进行图像绘制， 角色移动的方法调用
    for sprites in all_sprites:
        screen.blit(sprites.image, sprites.rect)
        sprites.move()
    # screen.blit(player.image, player.rect)
    # screen.blit(enemy.image, enemy.rect)
    # #放在while loop 里面是因为可以不断检测按键的状态
    # player.move()
    # enemy.move()
    for event in pygame.event.get():

        if event.type == SPEED_UP:
            SPEED += 0.5
        #用if来判断当前的event是否为quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #为确保其他程序正常运行，需要先退出pygame再退出系统
    #1.敌人和玩家都存在
    # if pygame.sprite.spritecollide(player, enemies,False):
    #     print("meiyou")
    # 2.敌人消失
    # if pygame.sprite.spritecollide(player, enemies,True):
    #     print("撞车了")
    # 3.敌人和玩家都消失
    # if pygame.sprite.spritecollide(player,enemies,True):
    #     player.kill()
    #     print("撞车啦")
    # 4. 玩家消失
    # if pygame.sprite.spritecollideany(player, enemies):
    #     player.kill()
    #     print("两车相撞")
    # 从每个组中删除精灵, 不影响精灵的状态, 还可以重新添加到Group中.
    if pygame.sprite.spritecollideany(player, enemies):
        time.sleep(1.5)
        screen.fill(RED)
        screen.blit(game_over,(150, 200))

        time.sleep(1.5)
        pygame.display.update()
        
        pygame.quit()
        sys.exit()
    if player not in all_sprites:
        all_sprites.add(player)

    pygame.display.update()
    clock.tick(FPS)
      #通过display update 来确保窗口的显示，但是为了避免窗口陷入死循环我们需要设置条件
    #来确保只有当event发生的时候才显示窗口