import pygame,math,sys
from settings import*
from map import map

walltexture = pygame.image.load("wall.png")

def raycasting(sc,playerpos,playerangle):
    
    cur_angle = playerangle - HALF_FOV

    xo, yo = playerpos
    
  

    for ray in range(NUM_RAYS):

        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(MAX_DEPTH):
                x1 = xo + depth * cos_a
                y1 = yo + depth * sin_a
                x2 = xo + (depth+1) * cos_a
                y2 = yo + (depth+1) * sin_a
                hasCollided = False
                for i in map:
                    segments = i.segments
                    if i.isTrigger != True:
                        if i.checkCollide([((x1,y1),(x2,y2))]):
                        #collide
                            proj_height = PROJ_COEFF /depth
                            hasCollided = True
                            wall_slice = pygame.transform.scale(walltexture,(SCALE, int(proj_height)))
                            sc.blit(wall_slice, (ray *SCALE, 400 - proj_height //2))



                            break
                if hasCollided:
                     break
        cur_angle += DELTA_ANGLE

