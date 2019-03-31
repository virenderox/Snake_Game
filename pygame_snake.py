import pygame
import time
import random
pygame.init()
apple_eat =  pygame.mixer.Sound("apple_eat.Wav")
pygame.mixer.music.load("apple_music.mp3")
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0 , 225 ,0)
display_width = 800
display_height = 600
Applethickness = 30
block_size = 20
direction = "right"
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("snake")
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)
imp   = pygame.image.load('snake_img.png')
appleimg = pygame.image.load('apple.png')
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

def pause():
    paused =  True 

def score(score):
    text = smallfont.render("Score: " + str(score) , True  ,black)
    gamedisplay.blit(text , [0,0])

def game_intro():
    intro = True
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gamedisplay.fill(white)
        message_to_screen("Welcome to Slither", green, -100 ,"large")
        message_to_screen("The objective of this game is to eat apple", black, -30 )
        message_to_screen("More apple you eat , the longer  you get", black, 10 )
        message_to_screen("If you run into yourself , or the edges, you die!", black, 50 )
        message_to_screen("press C to play and Q to Quit", black, 180 )
        pygame.display.update()
        clock.tick(15)
    
def snake(block_size,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(imp,270)
    if direction == "left":
        head = pygame.transform.rotate(imp,90)
    if direction == "up":
        head = imp
    if direction == "down":
        head = pygame.transform.rotate(imp,180)
    gamedisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    for i in snakelist[:-1]:
        pygame.draw.rect(gamedisplay,black,[i[0],i[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface=  smallfont.render(text,True,color)
    if size == "medium":
        textSurface=  medfont.render(text,True,color)
    if size == "large":
        textSurface=  largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace = 0 ,size = "small"):
    textSurf , textrect = text_objects(msg , color, size)
    textrect.center = (display_width / 2), (display_height / 2) + y_displace
    gamedisplay.blit(textSurf , textrect)
    
  #  screen_text = font.render(msg,True,color)
   
def game_loop():
    global direction
    pygame.mixer.music.play(-1)
    driection = "right"
    randapplex = round(random.randint(0,display_width-Applethickness ))#/10.0)*10.0
    randappley = round(random.randint(0,display_height-Applethickness ))#/10.0)*10.0
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakelist = []
    snakelength = 1
    while not gameExit:

        while gameOver == True:
            gamedisplay.fill(white)
            message_to_screen("Game over",red, -50, size = "large")
            message_to_screen("Press c to play and Q to Quit",black, 50,size = "medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()
                    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = 10
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = 10
                    lead_x_change = 0

        if lead_x >= display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gamedisplay.fill(white)
        
        #pygame.draw.rect(gamedisplay,red,[randapplex,randappley,Applethickness,Applethickness])
        gamedisplay.blit(appleimg , (randapplex,randappley))
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del snakelist[0]

        for eachsegement in snakelist[:-1]:
            if eachsegement == snakehead:
                gameOver = True
                
        snake(block_size,snakelist)

        score(snakelength -1)
        pygame.display.update()
        if lead_x > randapplex and lead_x < randapplex + Applethickness  or lead_x +block_size > randapplex and lead_x + block_size <  randapplex + Applethickness  :
             if lead_y >  randappley and lead_y < randappley + Applethickness or lead_y +block_size > randappley and lead_y + block_size <  randappley + Applethickness  :
                #pygame.mixer.music.stop()
                pygame.mixer.Sound.play(apple_eat)
                randapplex = round(random.randint(0,display_width-Applethickness ))#/10.0)*10.0
                randappley = round(random.randint(0,display_height-Applethickness ))#/10.0)*10.0
                snakelength+=1
            
        clock.tick(20)

##    message_to_screen("You Lose",red)
##    pygame.display.update()
##    time.sleep(2)

    pygame.quit()
    quit()
game_intro()
game_loop()               
