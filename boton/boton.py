import pygame

class Boton():
    
    def __init__(self,posicion_x,posicion_y,ancho,alto,color_inactivo,color_activo, valor):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.ancho = ancho
        self.alto = alto
        self.color_inactivo = color_inactivo
        self.color_activo = color_activo
        self.myFond = pygame.font.SysFont('Times New Roman', 25)
        self.valor = valor

    def renderizar_texto(self,screen):
        texto = self.myFond.render(self.valor,True,"black")
        posicion = (((self.posicion_x * 2) + self.ancho) / 2, ((self.posicion_y * 2) + self.alto) /2)
        screen.blit(texto,posicion)
    
    def comprobacion(self,mouse):
        mouse_posicion = mouse.get_pos()
        if (self.ancho + self.posicion_x >= mouse_posicion[0] >= self.posicion_x) and (self.alto + self.posicion_y >= mouse_posicion[1] >= self.posicion_y):
            return True
        
        return False

    def accion(self,mouse,click,screen):
        if self.comprobacion(mouse):
            if click == 1:
                if self.valor == "X":
                    screen.input += "*"
                else:
                    screen.input += self.valor

    def dibujar(self,screen,mouse):

        pygame.draw.rect(screen, (255,255,255), (self.posicion_x,self.posicion_y,self.ancho,self.alto))

        if self.comprobacion(mouse):
            pygame.draw.rect(screen, self.color_activo, (self.posicion_x+5,self.posicion_y+5,self.ancho-5,self.alto-5))

        else:
            pygame.draw.rect(screen, self.color_inactivo, (self.posicion_x+5,self.posicion_y+5,self.ancho-5,self.alto-5))
        
        
        self.renderizar_texto(screen)