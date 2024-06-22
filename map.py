from settings import*
from collider import*
import pygame,math,sys


map = []
lapProgression = []


playerimage = pygame.image.load("collider.png")
#(x,y)(w,h)angle
    
#top wall
map.append(BoxCollider(800,15,1400,50,0,False))

#bottom wall
map.append(BoxCollider(800,775,1400,50,0,False))

#right wall
map.append(BoxCollider(1600,375,800,200,90,False))

#left wall
map.append(BoxCollider(0,375,800,325,90,False))

#inside wall
map.append(BoxCollider(675,175,725,75,0,False)) #left          #new colliders match 2D background 
map.append(BoxCollider(1025,400,350,200,90,False)) #right
map.append(BoxCollider(675,600,725,75,0,False)) #middle
map.append(BoxCollider(1200,475,300,300,0,False))
map.append(BoxCollider(375,400,700,75,0,False))
map.append(BoxCollider(1300,175,125,75,0,False))


#lap progression
lapProgression.append(BoxCollider(600,600,450,100,135,True)) #bottom left
lapProgression.append(BoxCollider(1000,600,450,100,45,True)) #bottom right
lapProgression.append(BoxCollider(1000,200,450,100,45,True))#top right
lapProgression.append(BoxCollider(500,200,450,100,135,True)) #top left
lapProgression.append(BoxCollider(250,375,450,100,0,True)) #finish

