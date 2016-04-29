import pygame
import sys
import random
from enemigo import*
def Crear_enemigos(num, l_e, l_t,nivel):
	for i in range(num):
		if nivel==1:
			enemigo=Enemigo('img/enemigoverde.png')
			enemigo.tipo = random.randrange(3)
		elif nivel==2:
			enemigo=Enemigo('img/enemigoamarillo.png')
			enemigo.tipo = random.randrange(3)
		elif nivel==3:
			enemigo=Enemigo('img/enemigoazul.png')
			enemigo.tipo = random.randrange(3)
		else:
			enemigo=Enemigo('img/enemigogris.png')
			enemigo.tipo = random.randrange(3)

		if enemigo.tipo == 1:

			enemigo.pos_x=inv_xcar(random.randrange(ancho - 200) + 100)
			enemigo.pos_y=inv_ycar(random.randrange(alto - 350) + 100)

			enemigo.radio = random.randrange(90) + 10
			enemigo.draw_x = enemigo.radio
			enemigo.draw_y = 0
			enemigo.d = 1 - enemigo.draw_x
		else:
			enemigo.rect.x=random.randrange(ancho - 100)
			enemigo.rect.y=random.randrange(alto - 300)
      
		l_e.add(enemigo)
		l_t.add(enemigo)
	return l_e, l_t
