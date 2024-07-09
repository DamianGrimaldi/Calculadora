import pygame

class Pantalla():
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.screen = pygame.display.set_mode((self.ancho,self.alto))
    
    def dibujar(self):
        
        self.screen.fill((144,44,100))
