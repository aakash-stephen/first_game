import sys,pygame
from pygame.locals import *
import time,os.path

pygame.init
height,width = 600,1200

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("fireball_arena")
img_path = "../resources/images/"
player = pygame.image.load( img_path + 'player.png' )
#bowser = pygame.image.load( img_path + 'bowser.png' )
background = pygame.image.load( img_path + 'background1.png')
kaboom = pygame.image.load( img_path + 'kaboom.png')
fireball = pygame.image.load ( img_path + 'fireball.png' )
clock = pygame.time.Clock()
x1 = width * 0.20
y1 = height * 0.85 -80
x2 = width * 0.75
y2 = height * 0.85 -90
x1_change = 0
y1_change = 0
x2_change = 0
y2_change = 0
f = 0
game_quit = False
cur_time = 0
platform_height = 0.02* height
platform_xpos1 = width * 0.1
platform_xpos2 = width * 0.3
platform_ypos = height * 0.21
def player_motion(x1,y1,f=0,elap=1001):
    if f == 1 and elap < 1.5:
        screen.blit( player , (x1,y1))
        #y_change = 10
    else:
        screen.blit( player , (x1,y1)) 
        """for i in range(-20,21):
            pygame.time.delay(10)
            y1 += i/2 
            player_motion(x1,y1)
            screen.blit( player , (x1,y1))
            pygame.display.update()"""
        pygame.display.update()
def bowser_motion(x2,y2):
    screen.blit( bowser , (x2,y2))

while not game_quit:
    screen.fill( (255, 255, 255) ) 
    floor = pygame.draw.rect( screen , (128,0,0) , (0 , height * 0.85 , width , 0.15 * height))  
    platform1 = pygame.draw.rect( screen , (128,0,0) , (platform_xpos1 , platform_ypos * 1 , width*0.1 , platform_height))
    platform2 = pygame.draw.rect( screen , (128,0,0) , (platform_xpos2 , platform_ypos * 2 , width*0.1 , platform_height))
    platform3 = pygame.draw.rect( screen , (128,0,0) , (platform_xpos1 , platform_ypos * 3 , width*0.1 , platform_height))
    for event in pygame.event.get():
       
        #print(event)
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.KEYDOWN:
            f = 0
            if event.key == pygame.K_a: 
                x1_change = -5
            if event.key == pygame.K_d: 
                x1_change = 5
            #if event.key == pygame.K_s:
                #y1_change = 5
            #if event.key == pygame.K_w:
                #y1_change = -5
            if event.key == pygame.K_SPACE and y1 == height * 0.85 -80:
                f = 1
                cur_time = time.clock()
                y1_change = -10
            if event.key == pygame.K_LEFT: 
                x2_change = -5
            if event.key == pygame.K_RIGHT: 
                x2_change = 5
            #if event.key == pygame.K_DOWN:
                #y2_change = 5
            #if event.key == pygame.K_UP:
               # y2_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w:
                x1_change = 0
            if event.key == pygame.K_SPACE:
                y1_change = 5
            """if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x2_change = 0
                #y2_change = 0"""
        
    #print("1")
    if (x1 > 0 and x1 + 80 < width) or (x1 == 0 and x1_change > 0) or ( x1 + 80 == width and x1_change <0):
        x1 += x1_change
    if ((y1 > 0 and y1 + 80 < 0.85 * height) or (y1 == 0 and y1_change > 0) or ( y1 + 80 == 0.85*height and y1_change <0)):
        y1 += y1_change
    """if (x2 > 0 and x2 + 90 < width) or (x2 == 0 and x2_change > 0) or ( x2 + 90 == width and x2_change <0):
        x2 += x2_change
    if (y2 > 0 and y2 + 90 < 0.85*height) or (y2 == 0 and y2_change > 0) or ( y2 + 90 == 0.85*height and y2_change <0):
        y2 += y2_change
    if f == 1:
        for i in range(-20,21):
             pygame.time.delay(10)
             y1 += i/2 
             player_motion(x1,y1)
             #bowser_motion(x2,y2)
             pygame.display.update() """         
    elap = time.clock() - cur_time
    #print(elap)
    player_motion(x1,y1,f,elap)           
    #bowser_motion(x2,y2)
    pygame.display.update()
    clock.tick(60)
        
        

