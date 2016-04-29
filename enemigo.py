import pygame
import sys
import random
from pygame.locals import *
from puntomediolinea import*

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

		self.tipo = 0
		self.radio = 0
		self.pos_x = 0
		self.pos_y = 0

		self.etapa = 0

		self.draw_x = 0
		self.draw_y = 0
		self.d = 0

	def update(self):

		if self.tipo == 1:
			if self.draw_y > self.draw_x:
				self.etapa = (self.etapa + 1) % 8

				self.memo = self.draw_x

				self.draw_x = self.radio #r = radio
				self.draw_y = 0
				self.d = 1 - self.draw_x

			if self.etapa == 0:
				self.rect.x = xcar( self.draw_x + self.pos_x)
				self.rect.y = ycar( self.draw_y + self.pos_y)
			elif self.etapa == 1:
				self.rect.x = xcar((self.memo - (self.draw_y)) + self.pos_x)
				self.rect.y = ycar((self.memo + (self.radio - self.draw_x)) + self.pos_y)
			elif self.etapa == 2:
				self.rect.x = xcar(-self.draw_y + self.pos_x)
				self.rect.y = ycar( self.draw_x + self.pos_y)
			elif self.etapa == 3:
				self.rect.x = xcar((-self.memo - (self.radio - self.draw_x)) + self.pos_x)
				self.rect.y = ycar((self.memo - (self.draw_y)) + self.pos_y)
			elif self.etapa == 4:
				self.rect.x = xcar(-self.draw_x + self.pos_x)
				self.rect.y = ycar(-self.draw_y + self.pos_y)
			elif self.etapa == 5:
				self.rect.x = xcar(-self.memo + self.draw_y + self.pos_x)
				self.rect.y = ycar(-self.memo - (self.radio - self.draw_x) + self.pos_y)
			elif self.etapa == 6:
				self.rect.x = xcar( self.draw_y + self.pos_x)
				self.rect.y = ycar(-self.draw_x + self.pos_y)
			elif self.etapa == 7:
				self.rect.x = xcar( self.memo + (self.radio - self.draw_x) + self.pos_x)
				self.rect.y = ycar(-self.memo + self.draw_y + self.pos_y)

			if self.d > 0:
				self.draw_x -= 1
				self.d -= (2 * self.draw_x)
			self.draw_y += 1
			self.d += ((2 * self.draw_y) + 1)

		else:

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
			self.disparar=random.randrange(100)
