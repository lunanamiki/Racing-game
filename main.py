import pygame, sys, math, keyboard, time
from player import*
from pygame.locals import QUIT
from map import map
from settings import*
from ray_casting import raycasting

mapProgress = 0
laps = 0
playerimage = pygame.image.load("Car.png")
backgroundimage = pygame.image.load('racetrack.jpg')
clock = pygame.time.Clock()
player = Player()

totaltime = 0
lastlapendtime = 0
currentlaptime = 0
bestlaptime = 0

#denug variable
debug = 0

pygame.init()
sc = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Racing Game!')


def clockText(milliseconds):
    m = int(totaltime%1000)
    s = int((totaltime/1000)%60)
    min = int((totaltime/1000)/60)
    if(min<9):
        if(s<9):
            return "0"+str(min)+":0"+str(s)+"."+str(m)
        else:
            return "0"+str(min)+":"+str(s)+"."+str(m)
    else:
        if(s<9):
            return str(min)+":0"+str(s)+"."+str(m)
        else:
            return "0"+str(min)+":"+str(s)+"."+str(m)



while True:#gameloop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    sc.fill(BLACK)
    currenttime = pygame.time.get_ticks()
    totaltime = currenttime
    currentlaptime = currenttime-lastlapendtime

    player.movePlayer()
    if player.col.checkCollide(lapProgression[mapProgress].segments):
        mapProgress += 1
        if mapProgress >= len(lapProgression):
            laps += 1
            if currentlaptime<bestlaptime or bestlaptime == 0:
                bestlaptime = currentlaptime
            lastlaptime = totaltime
            mapProgress = 0
        
    #pygame.draw.circle(sc,GREEN,player.getPosition(),12)
    sc.blit(backgroundimage,(0,0))
    rotatedimage = pygame.transform.rotate(playerimage,-math.degrees(player.angle)-90)#player image faces up by default
    playerimagex, playerimagey = player.getPosition()
    playerImagePosition = (playerimagex - rotatedimage.get_width()//2,playerimagey - rotatedimage.get_height()//2)
    sc.blit(rotatedimage, playerImagePosition)
    pygame.draw.line(sc,GREEN,player.getPosition(),(player.x+(100*math.cos(player.angle)),
                                                         player.y+(100*math.sin(player.angle))))
    
#debug menu
    for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
           debug+=1
#-----keypress suggestion----
           

    # a = keyboard.read_event()     #Reading the key
    # if a.name == "esc":break      #Loop will break on pressing esc, you can remove that
    # elif a.event_type == "down":  #If any button is pressed (Not talking about released) then wait for it to be released
    #     t = time.time()           #Getting time in sec
    #     b = keyboard.read_event() 
    #     while not b.event_type == "up" and b.name == a.name:  #Loop till the key event doesn't matches the old one
    #         b = keyboard.read_event()
    #     debug+=1
           
#handle keypress with pygame issue with frame line ups, solution adding buffers
     
       
    if debug % 2 == 1:   
        
        player.col.renderCollider(sc)
        player.col.debugVertices(sc)
        for i in map:
                i.renderCollider(sc)
                i.debugVertices(sc)

        lapProgression[mapProgress].renderCollider(sc)
        lapProgression[mapProgress].debugVertices(sc)    

    
    

#caption
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Laps "+ str(laps), True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (190,100)
    sc.blit(text, textRect)

    #total time
    milliseconds = int(totaltime%1000)
    seconds = int((totaltime/1000)%60)
    minutes = int((totaltime/1000)/60)

    text = font.render("Total: "+clockText(totaltime), True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (190,200)
    sc.blit(text, textRect)
    
    clock.tick(FPS)
    pygame.display.update()


