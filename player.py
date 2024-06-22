import math, pygame
from settings import*
from collider import*
from map import *

class Player:
    def __init__(self):
        self.w,self.h =(70,45)
        self.x, self.y = (200,300)
        self.angle = 0
        self.speed = 0
        self.rotationalVelocity = 0
        self.rotationalAcceleration = math.pi/(500)
        self.rotationalVelocityMax = math.pi/50
        self.acceleration = .1
        self.maxSpeed = 6
        self.minSpeed = -2
        self.col = BoxCollider(self.x, self.y, self.w, self.h, self.angle,False)

       

    def getPosition(self):
        return (self.x, self.y)
    
    def getAngle(self):
        return (self.angle)
    
    def movePlayer(self):
        #rotational control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rotationalVelocity += self.rotationalAcceleration
        elif keys[pygame.K_a]:
            self.rotationalVelocity -= self.rotationalAcceleration
        elif self.rotationalVelocity > 0:
            self.rotationalVelocity -= ROTATIONALDRAG
            if self.rotationalVelocity < 0:
                self.rotationalVelocity = 0
        elif self.rotationalVelocity < 0:
            self.rotationalVelocity += ROTATIONALDRAG
            if self.rotationalVelocity > 0:
                self.rotationalVelocity = 0
        if self.rotationalVelocity > self.rotationalVelocityMax:
            self.rotationalVelocity = self.rotationalVelocityMax
        if self.rotationalVelocity < -self.rotationalVelocityMax:
            self.rotationalVelocity = -self.rotationalVelocityMax
        #end rotational control ---
            
        #speed control
        if keys[pygame.K_w]:
            self.speed += self.acceleration
        elif keys[pygame.K_s]:
            self.speed -= self.acceleration
        elif self.speed > 0:
            self.speed -= GROUNDFRICTION
            if self.speed < 0:
                self.speed = 0
        elif self.speed < 0:
            self.speed += GROUNDFRICTION
            if self.speed > 0:
                self.speed = 0

        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        if self.speed < self.minSpeed:
            self.speed = self.minSpeed
        #end speed control ---
            
        

        nextPosX, nextPosY = (self.x,self.y)
        nextPosX += self.speed*math.cos(self.angle)
        nextPosY += self.speed*math.sin(self.angle)

        lastx, lasty = self.x, self.y

        #check if necpos is not in wall
        self.x, self.y = nextPosX, nextPosY
        self.col.rePos(self.x, self.y)
        #update collider
        if self.CollideCheckMap():
            #bounce backwards & undo movements
            self.speed = -self.speed
            self.x, self.y = lastx, lasty
            self.col.rePos(self.x, self.y)
            
        #angle
        lastangle = self.angle
        self.angle += self.rotationalVelocity
        self.col.setRotation(-math.degrees(self.angle))

        if self.CollideCheckMap():
            self.rotationalVelocity = -self.rotationalVelocity
            self.angle = lastangle
            self.col.setRotation(-math.degrees(self.angle))

        


    def CollideCheckMap(self):
        for i in map:
            segments = i.segments
            if i.isTrigger != True:
             if self.col.checkCollide(segments):
                return True
        return False