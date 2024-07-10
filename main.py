import pygame
import sys
from pantalla.pantalla import *
from boton.boton import *

pygame.init()

ancho = 500
alto = 600
ancho_boton, alto_boton = ancho//4, alto//5

#objeto pantalla:
screen = Pantalla(ancho,alto,alto_boton)

#boton:
matriz_posicion_botones = [
    [(ancho_boton*0,alto_boton*1),(ancho_boton*1,alto_boton*1),(ancho_boton*2,alto_boton*1),(ancho_boton*3,alto_boton*1)],
    [(ancho_boton*0,alto_boton*2),(ancho_boton*1,alto_boton*2),(ancho_boton*2,alto_boton*2),(ancho_boton*3,alto_boton*2)],
    [(ancho_boton*0,alto_boton*3),(ancho_boton*1,alto_boton*3),(ancho_boton*2,alto_boton*3),(ancho_boton*3,alto_boton*3)],
    [(ancho_boton*0,alto_boton*4),(ancho_boton*1,alto_boton*4),(ancho_boton*2,alto_boton*4),(ancho_boton*3,alto_boton*4)]
]
botones = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","+"],
    ["0",".","-","="]
]
color_inactivo = (144,144,144)
color_activo = (144,44,44)

for i,lista in enumerate(matriz_posicion_botones):
    for j, posicion in enumerate(lista):
        boton = Boton(posicion[0],posicion[1],ancho_boton,alto_boton,color_inactivo,color_activo,botones[i][j])
        botones[i][j] = boton

mouse = pygame.mouse

pygame.display.set_caption("Calculadora")
reloj = pygame.time.Clock()

def manejo_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = event.button
            for boton_lista in botones:
                    for boton in boton_lista:
                        boton.accion(mouse,click,screen)
        elif event.type == pygame.KEYDOWN:
            key = event.key
            screen.manejo_teclado(key)

def actualizar_pantalla():
    
    screen.dibujar(botones,mouse)
    
    pygame.display.flip()

def main():
    while True:
        
        manejo_eventos()
        
        reloj.tick(60)
        
        actualizar_pantalla()

main()