import pygame
import random


contador=0

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

#clase balas
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
		self.velocity = random.randrange(5) + 3

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

def Crear_enemigos(num, l_e, l_t):
    for i in range(num):
       enemigo=Enemigo('img/enemigo3.png')
       enemigo.rect.x=random.randrange(ancho - 100)
       enemigo.rect.y=random.randrange(alto - 300)
       l_e.add(enemigo)
       l_t.add(enemigo)
    return l_e, l_t

#genera movimiento al fondo
def ini_fondo(contador):
	pantalla.blit(fondoa,(0,-600+(contador%200*3)))
	pantalla.blit(fondoa,(0,contador%200*3))				
#genera movimiento al fondo polvo espacial
def ini_polvo(contador):
	pantalla.blit(fondob,(0,-600+(contador%40*15)))
	pantalla.blit(fondob,(0,contador%40*15))

if __name__=='__main__':
	#inicializar pantalla
	pygame.init()
	pygame.display.set_caption("Retro Invaders")
	pantalla=pygame.display.set_mode([ancho,alto])

	#fondos
	fondoa = pygame.image.load('img/espacio.png').convert_alpha()
	fondob = pygame.image.load('img/espacio_efecto.png').convert_alpha()

	#visibilidad puntero mouse
	pygame.mouse.set_visible(False)
	#posicion del mouse
	dato=pygame.mouse.get_pos()
	#sonido.play() para que suene
	pygame.mixer.music.load('sound/music1.ogg')
	#play(loops=0, start=0.0) -1 reproduce indefinidamente
	pygame.mixer.music.play(-1)
	#lista con todos los sprites
	ls_todos    = pygame.sprite.Group()
	ls_bala     = pygame.sprite.Group()
	ls_balae    = pygame.sprite.Group()
	ls_jugador  = pygame.sprite.Group()
	ls_enemigo  = pygame.sprite.Group()
	#imagenes del juego
	jugador=Jugador('img/nave.png')
	jugador.rect.x=dato[0]
	jugador.rect.y=dato[1]
	ls_jugador.add(jugador)
	ls_todos.add(jugador)
	#sonido disparo
	s_bala = pygame.mixer.Sound('sound/laser.wav')
	ls_enemigo, ls_todos = Crear_enemigos(5, ls_enemigo, ls_todos)
	#refrescar pantalla
	pygame.display.flip()
	#variables del juego
	puntos = 0
	num_enemigos=5
	terminar=False
	p0 = [0, 0]
	p1 = [0, 0]
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
				bala=Bala('img/laser.png')
				#play del sonido -> play(repeticiones=0, duracion en miliseg=0, fade_ms=0) -> Channel
				s_bala.play(0,0,0)
				bala.rect.x=dato[0]+17
				bala.rect.y=dato[1]
				ls_bala.add(bala)
				ls_todos.add(bala)
				#print (dato)

		ini_fondo(contador)
		ini_polvo(contador)
		contador+=1

		jugador.rect.x=dato[0]
		jugador.rect.y=dato[1]

		ls_choque = pygame.sprite.spritecollide(jugador, ls_enemigo, True)

		for elemento in ls_choque:
			#print ('choque')
			jugador.chocar()
			#print (jugador.vida)


		for b in ls_bala:
			ls_impacto=pygame.sprite.spritecollide(b, ls_enemigo, True)
			for impacto in ls_impacto:
				ls_bala.remove(b)
				ls_todos.remove(b)
				puntos+=1
				num_enemigos-=1
				#print (puntos)

		for be in ls_balae:
			impactos=ls_impacto=pygame.sprite.spritecollide(be, ls_jugador, False)
			for imp in impactos:
				jugador.chocar()
				#print jugador.vida, ' ', puntos
				ls_balae.remove(be)
				ls_todos.remove(be)

		for e in ls_enemigo:
			if e.disparar==0:
				balae=Bala('img/balaenemigo.png')
				balae.jugador=0

				# Guarde la pos del jugador
				p0[0] = inv_xcar(jugador.rect.x) + 15
				p0[1] = inv_ycar(jugador.rect.y)

				# Guarde la pos de el enemigo que disparo
				p1[0] = inv_xcar(e.rect.x)
				p1[1] = inv_ycar(e.rect.y)
				#print (p0, p1)
				
				# Decide a que octante pertenece la pendiente
				balae.octant = returnOctant(p0, p1)

				# Transforma con respecto al octante
				p0[0], p0[1] = switchFromOctantZeroFrom(balae.octant, p0[0], p0[1])
				p1[0], p1[1] = switchFromOctantZeroFrom(balae.octant, p1[0], p1[1])

				# Inicializa las variables de decision
				balae.dy = p1[1] - p0[1]
				balae.dx = p1[0] - p0[0]
				balae.d = 2 * balae.dy - balae.dx
				
				# Inicializa la pos de la bala
				balae.draw_x = p1[0]
				balae.draw_y = p1[1]

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
