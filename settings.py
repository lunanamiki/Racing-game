import math

#raycasting settings
FOV = math.pi /2.75
HALF_FOV= FOV/2
NUM_RAYS = 10
MAX_DEPTH = 70
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2*math.tan(HALF_FOV))
PROJ_COEFF = 15* DIST *100
SCALE = 800 // NUM_RAYS

#runtime settings
FPS= 60

#gameplay settings
GROUNDFRICTION = .05
ROTATIONALDRAG = math.pi/960


#colors
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)