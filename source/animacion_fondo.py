import random

class Fondo():
	
	
	def __init__(self, imagen):
		self.imagen=imagen
		self.contador=0
		
	def updatecontador(self):
		self.contador=self.contador+1
		
	def ini_fondo(self):
		pantalla.blit(self.imagen['espacio.png'],(0,-600+(self.contador%200*3)))
		pantalla.blit(self.imagen['espacio.png'],(0,self.contador%200*3))				
		
	def ini_polvo(self):
		pantalla.blit(self.imagen['espacio_efecto.png'],(0,-600+(self.contador%40*15)))
		pantalla.blit(self.imagen['espacio_efecto.png'],(0,self.contador%40*15))
	

