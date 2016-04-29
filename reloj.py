import pygame

#dimensiones de la pantalla
ancho=800
alto=600
#color
blanco=(255,255,255)
negro = (0, 0, 0)

dim_pantalla = [ancho,alto]
pantalla=pygame.display.set_mode(dim_pantalla)
fin_juego=False
reloj=pygame.time.Clock()

def reloj:

	reloj.tick(20)
	con_cuadros = 0
	tasa_cambio = 60
	tiempo_ini = 10
	seglim=0

	if not fin_juego:
		total_segundos = con_cuadros // tasa_cambio
		minutos = total_segundos // 60
		segundos = total_segundos % 60
		tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)

		if total_segundos < 0:
			total_segundos = 0

		texto = fuente.render(tiempo_final, True, blanco)

		pantalla.blit(texto, [250, 10])
