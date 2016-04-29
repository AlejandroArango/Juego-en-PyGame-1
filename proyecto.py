import pygame
import random
from jugador import*
from enemigo import*
from bala import*
from vida import*
from crearenemigos import*

#constantes
contador=0
puntaje=0
nivel=1
#dimensiones de la pantalla
ancho=800
alto=600
#color
blanco=(255,255,255)
negro = (0, 0, 0)

dim_pantalla = [ancho,alto]

#genera movimiento al fondo
def ini_fondo(contador):
	pantalla.blit(fondo,(0,-600+(contador%200*3)))
	pantalla.blit(fondo,(0,contador%200*3))				
#genera movimiento al fondo polvo espacial
def ini_polvo(contador,efecto):
	pantalla.blit(efecto,(0,-600+(contador%40*15)))
	pantalla.blit(efecto,(0,contador%40*15))

if __name__=='__main__':
	#inicializar pantalla
	pygame.init()
	#fuentes de texto
	fuente = pygame.font.Font("Bitsumishi.TTF", 36)
	gameover = pygame.font.Font("Abduction.TTF", 60)
	pygame.display.set_caption("Retro Invaders")
	pantalla=pygame.display.set_mode([ancho,alto])

	#fondos
	fondo = pygame.image.load('img/espacio.png').convert_alpha()
	nivel1 = pygame.image.load('img/espacio_efecto.png').convert_alpha()
	nivel2 = pygame.image.load('img/espacio_efecto2.png').convert_alpha()
	nivel3 = pygame.image.load('img/espacio_efecto3.png').convert_alpha()
	nivel4 = pygame.image.load('img/espacio_efecto4.png').convert_alpha()

	#visibilidad puntero mouse
	pygame.mouse.set_visible(False)
	#posicion inicial del puntero//ayuda a pocisionar la nave
	pygame.mouse.set_pos(400,520)
	#posicion del mouse
	dato=pygame.mouse.get_pos()
	#sonido.play() para que suene
	pygame.mixer.music.load('sound/Gradius.mp3')
	#play(loops=0, start=0.0) -1 reproduce indefinidamente
	pygame.mixer.music.play(-1)
	#lista con todos los sprites
	ls_todos    = pygame.sprite.Group()
	ls_bala     = pygame.sprite.Group()
	ls_balae    = pygame.sprite.Group()
	ls_jugador  = pygame.sprite.Group()
	ls_enemigo  = pygame.sprite.Group()
	#imagenes del juego
	jugador=Jugador('img/nave2.png')
	jugador.rect.x=dato[0]
	jugador.rect.y=dato[1]
	ls_jugador.add(jugador)
	ls_todos.add(jugador)
	#sonido disparo
	s_bala = pygame.mixer.Sound('sound/laser.wav')
	ls_enemigo, ls_todos = Crear_enemigos(5, ls_enemigo, ls_todos,nivel)
	#refrescar pantalla
	pygame.display.flip()
	#variables del juego
	num_enemigos=5
	terminar=False
	p0 = [0, 0]
	p1 = [0, 0]
	con_cuadros = 0
	tasa_cambio = 60
	tiempo_ini = 10
	seglim=0
	reloj=pygame.time.Clock()

	#tomar dos puntos con click y trazar ruta de movimiento NOTA algoritmo punto medio
	#hacer movimiento de scrolling sale de la pantalla aparece en el otro lado
	while (not terminar):
		dato=pygame.mouse.get_pos()
		for event in pygame.event.get():			
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
				terminar=True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				bala=Bala('img/balaazul.png')
				#play del sonido -> play(repeticiones=0, duracion en miliseg=0, fade_ms=0) -> Channel
				s_bala.play(0,0,0)
				bala.rect.x=dato[0]+17
				bala.rect.y=dato[1]
				ls_bala.add(bala)
				ls_todos.add(bala)
		
		#niveles
		if puntaje > 99 and puntaje < 199:
			nivel=2
		elif puntaje > 199 and puntaje < 299:
			nivel=3
		elif puntaje > 299:
			nivel=4

		#inicializacion fondos
		ini_fondo(contador)
		contador+=1
		if   nivel==1:
			ini_polvo(contador,nivel1)
		elif nivel==2:
			ini_polvo(contador,nivel2)
		elif nivel==3:
			ini_polvo(contador,nivel3)
		else:
			ini_polvo(contador,nivel4)

		fin_juego=False

		jugador.rect.x=dato[0]
		jugador.rect.y=dato[1]
		#jugador choca con enemigo
		ls_choque = pygame.sprite.spritecollide(jugador, ls_enemigo, True)

		for elemento in ls_choque:
			jugador.chocar()
   		if jugador.vida < 1:
			fin_juego = True


		if fin_juego:
			texto = gameover.render("GAME OVER", True, blanco)
			texto_rect = texto.get_rect()
			texto_x = pantalla.get_width()/2 - texto_rect.width/2
			texto_y = pantalla.get_height()/2 - texto_rect.height/2
			pantalla.blit(texto, [texto_x, texto_y])


		for b in ls_bala:
			ls_impacto=pygame.sprite.spritecollide(b, ls_enemigo, True)
			for impacto in ls_impacto:
				ls_bala.remove(b)
				ls_todos.remove(b)
				puntaje+=1
				num_enemigos-=1

		for be in ls_balae:
			impactos=ls_impacto=pygame.sprite.spritecollide(be, ls_jugador, False)
			for imp in impactos:
				jugador.menosVida(nivel)
				ls_balae.remove(be)
				ls_todos.remove(be)

		for e in ls_enemigo:
			if e.disparar==0:
				if nivel==1:
					balae=Bala('img/balaverde.png')
					balae.jugador=0
				elif nivel==2:
					balae=Bala('img/balaamarilla.png')
					balae.jugador=0
				elif nivel==3:
					balae=Bala('img/balaazul.png')
					balae.jugador=0
				else:
					balae=Bala('img/balagris.png')
					balae.jugador=0

				# Guarde la pos del jugador
				p0[0] = inv_xcar(jugador.rect.x) + 15
				p0[1] = inv_ycar(jugador.rect.y)

				# Guarde la pos de el enemigo que disparo
				p1[0] = inv_xcar(e.rect.x)
				p1[1] = inv_ycar(e.rect.y)
				
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
			ls_enemigo, ls_todos= Crear_enemigos(num_enemigos, ls_enemigo, ls_todos,nivel)

		#mostrar puntaje jugador
		txt_puntos = fuente.render("Puntaje "+ str(puntaje), True, blanco)
		pantalla.blit(txt_puntos, [5,5])

		#mostrar barra de vida jugador
	   	for nv in range(jugador.vida):
			vd = Vida(pantalla, nv)
		if jugador.vida>0:
			txt_salud = fuente.render("Salud   "+ str(jugador.vida), True, blanco)
			pantalla.blit(txt_salud, [5,27])
		else:
			txt_salud = fuente.render("Salud   0", True, blanco)
			pantalla.blit(txt_salud, [5,27])

		#tiempo del juego
		total_segundos = con_cuadros // tasa_cambio
		minutos = total_segundos // 60
		segundos = total_segundos % 60
		tiempo_final = "Tiempo {0:02}:{1:02}".format(minutos, segundos)
		texto = fuente.render(tiempo_final, True, blanco)
		pantalla.blit(texto, [500, 560])
		total_segundos = tiempo_ini - (con_cuadros // tasa_cambio)
		minutos = total_segundos // 60
		segundos = total_segundos % 60
		seglim=segundos
		con_cuadros += 1

		#para actualizar
		ls_todos.update()
		#pantalla.blit(enemigo,(200,200))
		ls_todos.draw(pantalla)
		#deben ser las ultimas instrucciones
		pygame.display.flip()
		reloj.tick(60)
		
		#pygame.time.Clock.tick(60) frames por segundo
