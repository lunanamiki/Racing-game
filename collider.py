from settings import*
import pygame,math,sys

boxColliderImage = pygame.image.load("collider.png")
class BoxCollider:
    def __init__(self,x,y,w,h,a,t):
        #self.image = i
        #self.texturesize = t
        self.x,self.y = (x,y)
        self.angle = a #in degrees
        self.width,self.height = (w,h)
        self.isTrigger = t
        self.verticies = []
        self.segment = []
        self.updateVerticies()


    def rePos(self, xpos,ypos):
        self.x = xpos
        self.y = ypos
        self.updateVerticies()
    def reScale(self, width, height):
        self.width = width
        self.height = height
        self.updateVerticies()
    def setRotation(self, setAngle): #in degrees
        self.angle = setAngle
        self.updateVerticies()
    def renderCollider(self,sc): #render from center
        for p1,p2 in self.segments:
            if self.isTrigger:
                pygame.draw.line(sc,RED,p1,p2)
            else:
             pygame.draw.line(sc,GREEN,p1,p2)



        #Render = pygame.transform.scale(boxColliderImage,(self.width, self.height))
        #Render = pygame.transform.rotate(Render, self.angle)#COUNTERCLOCKWISE 
        #posx, posy = (self.x-Render.get_width()//2, self.y-Render.get_height()//2)
        #sc.blit(Render, (posx,posy))

    def updateVerticies(self):
        self.verticies = [] #clear current verticies
        self.segments = []
        finalx,finaly = (self.x,self.y)
        radianAngle = math.radians(self.angle) #angle of rotation in rads
        rectAngle = math. atan((self.height/2)/(self.width/2))# angle of internal face at 0 rotation 
        finalAngle = radianAngle + rectAngle #combined angles
        finalAltAngle = radianAngle - rectAngle
        a = (self.width/2)*(self.width/2)
        b = (self.height/2)*(self.height/2)
        hypLength = math.sqrt(a+b)
        xmot = hypLength*(math.cos(finalAngle))
        ymot = hypLength*(math.sin(finalAngle))
        xmotalt = hypLength*(math.cos(finalAltAngle))
        ymotalt = hypLength*(math.sin(finalAltAngle))

        self.verticies.append((self.x+xmot,self.y-ymot))
        self.verticies.append((self.x-xmot,self.y+ymot))
        self.verticies.append((self.x+xmotalt,self.y-ymotalt))
        self.verticies.append((self.x-xmotalt,self.y+ymotalt))

        #create 4 segments
        self.segments.append((self.verticies[0],self.verticies[2]))# 0-2
        self.segments.append((self.verticies[2],self.verticies[1]))# 2-1
        self.segments.append((self.verticies[1],self.verticies[3]))# 1-3
        self.segments.append((self.verticies[3],self.verticies[0]))# 3-0

    def maptexture(self):
        image = pygame.Surface(self.texturesize)
        for i in range (math.ceil(self.width/self.texturesize[0])):
            print (i) 
            print ((i*self.texturesize[0]+self.texturesize[0]/2)*math.sin(self.angle-90)+self.verticies[0][0])
            for j in range (math.ceil(self.height/self.texturesize[1])):
                image.blit(self.image,((i*self.texturesize[0]+self.texturesize[0]/2)*math.sin(self.angle-90)+self.verticies[2][0],self.verticies[2][1]))
    def debugVertices(self,sc):
        

        #draw each vertex
        pygame.draw.circle(sc,GREEN,(self.x,self.y),5)
        for x,y in self.verticies:
            pygame.draw.circle(sc,GREEN,(x,y),5)

       # if self.image != None:
          #  self.maptexture()

    

    #dynamic colliders checking other colliders 
    def checkCollide(self, otherSegments):
        if self.isTrigger :
            return False #checkVerticies is for incoming collider
        #check the area with patting
        
        for A,B in self.segments: #separate each segment into their points
            for C,D in otherSegments:
                if intersect(A,B,C,D):
                    return True #placeholder to prevent error
            #get the slope of each face of the collider
            #determine if a face is vertical or horizontal
            #get the point along the slope of collider
            #use inequalities to check collision

        

        return False
    

def ccw(A,B,C):
    Ax,Ay = A
    Bx,By = B
    Cx,Cy = C
    return (Cy-Ay)*(Bx-Ax) > (By-Ay)*(Cx-Ax)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D)and ccw(A,B,C)!= ccw(A,B,D)

