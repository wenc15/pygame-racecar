import pygame
import sys



pygame.init()

pygame.display.set_caption("赛车游戏")
screen = pygame.display.set_mode((700, 700)) #设置当前窗口的高宽

#颜色

white = pygame.color.Color(255,255,255) # 定义颜色
black = pygame.color.Color(0,0,0, a =255) #alpha 代表不透明
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = (0,0,255)
screen.fill(black)
#设置图像的帧速率
FPS = 30 
clock= pygame.time.Clock()
background =pygame.image.load("780.jpg")
player = pygame.image.load("rotated_player.jpg")


x, y =330, 604


while True:#为了保留窗口需要while loop一直进行循环
    screen.blit(background, (0,0))
    screen.blit(player, (x,y))
    y -= 1
    for event in pygame.event.get():
        #用if来判断当前的event是否为quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #为确保其他程序正常运行，需要先退出pygame再退出系统
    pygame.display.update()
    clock.tick(FPS)
      #通过display update 来确保窗口的显示，但是为了避免窗口陷入死循环我们需要设置条件
    #来确保只有当event发生的时候才显示窗口