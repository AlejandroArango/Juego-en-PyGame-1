import pygame
import sys
import random
from pygame.locals import *
from puntomediolinea import*

#dimensiones de la pantalla
ancho=800
alto=600

class Bala(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.jugador=1

		self.draw_x = 0
		self.draw_y = 0
		self.octant = 0
		self.dy = 0
		self.dx = 0
		self.d = 0
		self.velocity = 7#random.randrange(5) + 3

	def update(self):
		if self.jugador==1:
			self.rect.y-=5#bala jugador
		else:
			# MidPoint Line Algotirhm
			if self.d > 0:
				self.draw_y -= self.velocity
				self.d -= (2 * self.dx)
			self.draw_x -= self.velocity
			self.d += (2 * self.dy)

			self.rect.x, self.rect.y = switchFromOctantZeroTo(self.octant, self.draw_x, self.draw_y)
			self.rect.x = xcar(self.rect.x)
			self.rect.y = ycar(self.rect.y)
