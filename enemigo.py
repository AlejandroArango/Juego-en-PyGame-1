import pygame
import sys
import random
from pygame.locals import *

#dimensiones de la pantalla
ancho=800
alto=600

class Enemigo(pygame.sprite.Sprite):

	def __init__(self,imagen):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.direccion=0
		self.disparar=random.randrange(100) + 100 

	def update(self):

		#ancho pantalla - ancho imagen
		if self.rect.x >= (ancho-62):
			self.direccion=1
		if self.rect.x <= 0:
			self.direccion=0

		if self.direccion==0:
			self.rect.x+=5
		else:
			self.rect.x-=5

		self.disparar-=1
		if self.disparar<0:
			self.disparar=random.randrange(100) + 100
