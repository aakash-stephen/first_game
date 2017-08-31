import sys,pygame
from pygame.locals import *
import time,os.path

pygame.init
height,width = 600,1200

screen = pygame.display.set_mode((width,height))
img_path = "C:/python/project/first_game/resources/images/"
player = pygame.image.load( img_path + 'player.png' )
bowser = pygame.image.load( img_path + 'bowser.png' )
background = pygame.image.load( img_path + 'background1.png')
kaboom = pygame.image.load( img_path + 'kaboom.png')
fireball = pygame.image.load ( img_path + 'fireball.png' )
clock = pygame.time.Clock()
game_quit = False
def player_motion(x1,y1):
    screen.blit( player , (x1,y1))
def bowser_motion(x2,y2):
    screen.blit( bowser , (x2,y2))
x1 = width * 0.20
y1 = height * 0.85 -80
x2 = width * 0.75
y2 = height * 0.85 -90
x1_change = 0
y1_change = 0
x2_change = 0
y2_change = 0
while not game_quit:
    screen.fill( (255, 255, 255) ) 
    floor = pygame.draw.rect( screen , (128,0,0) , (0 , height * 0.85 , width , 0.2 * height))  
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                x1_change = -5
            if event.key == pygame.K_d: 
                x1_change = 5
            #if event.key == pygame.K_s:
                #y1_change = 5
            #if event.key == pygame.K_w:
                #y1_change = -5
            if event.key == pygame.K_SPACE:
                for i in range(-20,21):
                    pygame.time.delay(10)
                    y1 += i/2 
                    player_motion(x1,y1)
                    bowser_motion(x2,y2)
                    pygame.display.update()
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
                #y1_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x2_change = 0
                #y2_change = 0
        
    
    if (x1 > 0 and x1 + 80 < width) or (x1 == 0 and x1_change > 0) or ( x1 + 80 == width and x1_change <0):
        x1 += x1_change
    #if (y1 > 0 and y1 + 80 < 0.85*height) or (y1 == 0 and y1_change > 0) or ( y1 + 80 == 0.85*height and y1_change <0):
        #y1 += y1_change
    if (x2 > 0 and x2 + 90 < width) or (x2 == 0 and x2_change > 0) or ( x2 + 90 == width and x2_change <0):
        x2 += x2_change
    #if (y2 > 0 and y2 + 90 < 0.85*height) or (y2 == 0 and y2_change > 0) or ( y2 + 90 == 0.85*height and y2_change <0):
        #y2 += y2_change
    
    player_motion(x1,y1)           
    bowser_motion(x2,y2)
    pygame.display.update()
    clock.tick(60)
        
        

