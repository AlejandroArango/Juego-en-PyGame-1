import pygame
import sys
import random
from pygame.locals import *

class Jugador(pygame.sprite.Sprite):

	def __init__(self,imagen):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.vida=100

	def chocar(self):
		self.vida -=10

	def menosVida(self,nivel):
		if nivel==1:
			self.vida = self.vida - 1
		elif nivel==2:
			self.vida = self.vida - 2
		elif nivel==3:
			self.vida = self.vida - 3
		else:
			self.vida = self.vida - 4

	def masVida(self):
		self.vida = self.vida + 1
