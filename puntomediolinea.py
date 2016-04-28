import pygame
import sys
import random
from pygame.locals import *

#dimensiones de la pantalla
ancho=800
alto=600

# Transform component x from cartesian coordinate to screen coordinate
def inv_xcar(px):
    return int(-ancho/2+px)

# Transform component y from cartesian coordinate to screen coordinate
def inv_ycar(py):
    return int(alto/2-py)

# Transform component x from cartesian coordinate to screen coordinate
def xcar(px):
    return int(ancho/2+px)

# Transform component y from cartesian coordinate to screen coordinate
def ycar(py):
    return int(alto/2-py)

def switchFromOctantZeroFrom(octant, x, y):
    if (octant == 0):
        return x, y
    elif (octant == 1):
        return y, x
    elif (octant == 2):
        return y, -x
    elif (octant == 3):
        return -x, y

def switchFromOctantZeroTo(octant, x, y):
    if (octant == 0):
        return x, y
    elif (octant == 1):
        return y, x
    elif (octant == 2):
        return -y, x
    elif (octant == 3):
        return -x, y

def returnOctant(p0, p1):
    dy = p1[1] - p0[1]
    dx = p1[0] - p0[0]
    if (dx == 0):
    	dx = 1
    m = dy / dx
    if (m < -1):
        return 2
    if (m < 0):
        return 3
    if (m < 1):
        return 0
    return 1
