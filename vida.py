import pygame
import sys
import random
from pygame.locals import *

#colores
verde = (0, 255, 0)
red=(255,0,0)

class Vida(pygame.sprite.Sprite):

	def __init__(self, pantalla, num):

		pygame.sprite.Sprite.__init__(self)
		self.bien = verde
		self.mal = red
		if num>50:
			pygame.draw.rect(pantalla, self.bien, [10, 570, (num*2), 20])
		else:
			pygame.draw.rect(pantalla, self.mal, [10, 570, (num*2), 20])
