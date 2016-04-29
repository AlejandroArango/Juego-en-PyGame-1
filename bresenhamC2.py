import pygame
import sys

AZUL = (0,0,255)


# ancho y alto de la pantalla
ANCHO=800
ALTO=600

CentroX = int(ANCHO/2)
CentroY = int(ALTO/2)

def transformada(punto):
  nx=CentroX+punto[0]
  ny=CentroY-punto[1]
  return (int(nx),int(ny))


def CircleMidPoint(r):
  x = 0
  y = r
  p = 1 - r

  Lista_1 = []
  Lista_2 = []
  Lista_3 = []
  Lista_4 = []
  Lista_5 = []
  Lista_6 = []
  Lista_7 = []
  Lista_8 = []
  
  Lista_1.append(transformada([x,y]))

  while (x < y):
    x = x + 1
    if p < 0:
      p = p + 2*x + 1
    else :
      y = y - 1
      p = p + 2*(x - y) + 1
    x1 = x
    y1 = y
  
    Lista_1.append(transformada([x1,y1]))
    Lista_8.append(transformada([-x1,y1]))
    Lista_4.append(transformada([x1,-y1]))
    Lista_5.append(transformada([-x1,-y1]))
    Lista_2.append(transformada([y1,x1]))
    Lista_7.append(transformada([-y1,x1]))
    Lista_3.append(transformada([y1,-x1]))
    Lista_6.append(transformada([-y1,-x1]))
  Lista_1.extend(Lista_2[::-1])
  Lista_1.extend(Lista_3)
  Lista_1.extend(Lista_4[::-1])
  Lista_1.extend(Lista_5)
  Lista_1.extend(Lista_6[::-1])
  Lista_1.extend(Lista_7)
  Lista_1.extend(Lista_8[::-1])

  return Lista_1
