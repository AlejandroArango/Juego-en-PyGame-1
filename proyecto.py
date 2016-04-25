import pygame
import random

#dimensiones de la pantalla
ancho=1000
alto=600

#clase jugador
class Jugador(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.vida=100
	def chocar(self):
		self.vida -=10

#clase enemigo
class Enemigo(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.direccion=0
		self.disparar=random.randrange(100)
	def update(self):
		if self.rect.y >= (alto-20):
			self.direccion=1
		if self.rect.y <= 10:
			self.direccion=0

		if self.direccion==0:
			self.rect.y+=5
		else:
			self.rect.y-=5

		self.disparar-=1
		if self.disparar<0:
			self.disparar=random.randrange(100)

#clase balas
class Bala(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagen).convert_alpha()
		self.rect = self.image.get_rect()
		self.jugador=1
	def update(self):
		if self.jugador==1:
			self.rect.x+=5#bala jugador
		else:
			self.rect.x-=5#bala enemigo

def Crear_enemigos(num, l_e, l_t):
    for i in range(num):
       enemigo=Enemigo('enemigo3.png')
       enemigo.rect.x=random.randrange(100, ancho-20)
       enemigo.rect.y=random.randrange(alto-20)
       l_e.add(enemigo)
       l_t.add(enemigo)
    return l_e, l_t


if __name__=='__main__':
	#inicializar pantalla
	pygame.init()
	pygame.display.set_caption("Retro Invaders")
	pantalla=pygame.display.set_mode([ancho,alto])
	#fondo juego
	fondo = pygame.image.load('fondo.jpg').convert_alpha()
	pantalla.blit(fondo,(0,0))
	#visibilidad puntero mouse
	pygame.mouse.set_visible(False)
	#posicion del mouse
	dato=pygame.mouse.get_pos()
	#sonido.play() para que suene
	#sonido fondo
	pygame.mixer.music.load('music1.ogg')
	#play(loops=0, start=0.0) -1 reproduce indefinidamente
	pygame.mixer.music.play(-1)
	#lista con todos los sprites
	ls_todos    = pygame.sprite.Group()
	ls_bala     = pygame.sprite.Group()
	ls_balae    = pygame.sprite.Group()
	ls_jugador  = pygame.sprite.Group()
	ls_enemigo  = pygame.sprite.Group()
	#imagenes del juego
	jugador=Jugador('nave.png')
	jugador.rect.x=dato[0]
	jugador.rect.y=dato[1]
	ls_jugador.add(jugador)
	ls_todos.add(jugador)
	#sonido disparo
	s_bala= pygame.mixer.Sound('laser.wav')
	ls_enemigo, ls_todos = Crear_enemigos(5, ls_enemigo, ls_todos)
	#refrescar pantalla
	pygame.display.flip()
	#puntuacion
	puntos = 0
	num_enemigos=5
	terminar=False
	reloj=pygame.time.Clock()


	#tomar dos puntos con click y trazar ruta de movimiento NOTA algoritmo punto medio
	#hacer movimiento de scrolling sale de la pantalla aparece en el otro lado
	while (not terminar):
		dato=pygame.mouse.get_pos()
		for event in pygame.event.get():
			#if event.type == pygame.KEYDOWN:
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
				terminar=True


			elif event.type == pygame.MOUSEBUTTONDOWN:
				bala=Bala('laser.png')
				sonido_bala = pygame.mixer.Sound('laser.wav')#no funciona
				bala.rect.x=dato[0]
				bala.rect.y=dato[1]+17
				ls_bala.add(bala)
				ls_todos.add(bala)
				print (dato)

		#pantalla.fill(blanco)
		pantalla.blit(fondo,(0,0))
		jugador.rect.x=dato[0]
		jugador.rect.y=dato[1]

		ls_choque = pygame.sprite.spritecollide(jugador, ls_enemigo, True)

		for elemento in ls_choque:
			print ('choque')
			jugador.chocar()
			print (jugador.vida)


		for b in ls_bala:
			ls_impacto=pygame.sprite.spritecollide(b, ls_enemigo, True)
			for impacto in ls_impacto:
				ls_bala.remove(b)
				ls_todos.remove(b)
				puntos+=1
				num_enemigos-=1
				print (puntos)

		for be in ls_balae:
			impactos=ls_impacto=pygame.sprite.spritecollide(be, ls_jugador, False)
			for imp in impactos:
				jugador.chocar()
				print jugador.vida, ' ', puntos
				ls_balae.remove(be)
				ls_todos.remove(be)

		for e in ls_enemigo:
			if e.disparar==0:
				balae=Bala('balaenemigo.png')
				balae.jugador=0
				balae.rect.x=e.rect.x
				balae.rect.y=e.rect.y
				ls_todos.add(balae)
				ls_balae.add(balae)

		if num_enemigos<2:
			num_enemigos=random.randrange(5)
			ls_enemigo, ls_todos= Crear_enemigos(num_enemigos, ls_enemigo, ls_todos)
		#para actualizar
		ls_todos.update()
		#pantalla.blit(enemigo,(200,200))
		ls_todos.draw(pantalla)
		#deben ser las ultimas instrucciones
		pygame.display.flip()
		reloj.tick(50)
		#pygame.time.Clock.tick(60) frames por segundo
