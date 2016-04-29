import pygame


 
NEGRO  = (   0,   0,   0)
BLANCO = ( 255, 255, 255)
VERDE  = (   0, 255,   0)
ROJO   = ( 255,   0,   0)
ANCHO = 800
ALTO = 600


if __name__=='__main__':
	pygame.init()
	dim=[ANCHO, ALTO]
	pantalla=pygame.display.set_mode(dim)
	pygame.display.set_caption("Titulo del juego")

	#fuentes de texto
	fuente = pygame.font.Font("Bitsumishi.TTF", 36)
	fuentepuntaje = pygame.font.Font("Bitsumishi.TTF", 12)
	terminar=False
	ver_pag = True
	pag = 1
	fin_juego=False
	reloj=pygame.time.Clock()

	#CICLO PRESENTACION
	while not terminar and ver_pag:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				terminar=True
			if event.type == pygame.MOUSEBUTTONDOWN:
				pag += 1
			if pag == 3:
				ver_pag = False

		pantalla.fill(NEGRO)
 
		if pag == 1:
			# Instrucciones en pagina 1
			fondo=pygame.image.load("img/espacio.png")
			fondo=pygame.transform.scale(fondo,dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render("Instrucciones", True, BLANCO)
			pantalla.blit(texto, [10, 10]) 

			imagen=pygame.image.load('img/nave1.png')
			imagen=pygame.transform.scale(imagen,[300,300])
			pantalla.blit(imagen,[150,250])

		if pag == 2:
			# Instrucciones en pagina 1
			fondo=pygame.image.load("img/espacio.png")
			fondo=pygame.transform.scale(fondo,dim)
			pantalla.blit(fondo,[0,0])
			texto=fuente.render("Instrucciones pagina 2", True, BLANCO)
			pantalla.blit(texto, [10, 10]) 

			imagen=pygame.image.load('img/nave2.png')
			imagen=pygame.transform.scale(imagen,[400,400])
			pantalla.blit(imagen,[150,250])
 		
		reloj.tick(20)
		pygame.display.flip()

		#RELOJ CUENTA REGRESIVA, PROGRESIVA   
		con_cuadros = 0
		tasa_cambio = 60
		tiempo_ini = 10
		seglim=0

		fondo=pygame.image.load("img/espacio.png")
		fondo=pygame.transform.scale(fondo,dim)
		pantalla.blit(fondo,[0,0])

	#CICLO DEL JUEGO
	while not terminar:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminar=True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if fin_juego:
					terminar=True

		if not fin_juego:
			pantalla.fill(NEGRO)
			#CUENTA PROGRESIVA
			total_segundos = con_cuadros // tasa_cambio
			minutos = total_segundos // 60
			segundos = total_segundos % 60
			tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)

			#CUENTA REGRESIVA
			texto = fuente.render(tiempo_final, True, BLANCO)
			pantalla.blit(texto, [10, 10])
			total_segundos = tiempo_ini - (con_cuadros // tasa_cambio)
			if total_segundos < 0:
				total_segundos = 0

			minutos = total_segundos // 60
			segundos = total_segundos % 60
			seglim=segundos

			tiempo_final = "Tiempo restante: {0:02}:{1:02}".format(minutos, segundos)

			texto = fuente.render(tiempo_final, True, BLANCO)

			pantalla.blit(texto, [250, 10])

		if fin_juego:
			pantalla.fill(NEGRO)
			texto = fuente.render("Fin del juego", True, BLANCO)
			texto_rect = texto.get_rect()
			texto_x = pantalla.get_width() / 2 - texto_rect.width / 2
			texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
			pantalla.blit(fondo,[0,50])
			pantalla.blit(texto, [texto_x, texto_y])
		else:
			pantalla.blit(fondo,[0,50])

		con_cuadros += 1
		reloj.tick(tasa_cambio)

     
		pygame.display.flip()
		if seglim==0:
			fin_juego=True


