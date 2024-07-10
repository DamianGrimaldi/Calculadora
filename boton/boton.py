import pygame

class Boton():
    
    def __init__(self,posicion_x,posicion_y,ancho,alto,color_inactivo,color_activo, valor):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.ancho = ancho
        self.alto = alto
        self.color_inactivo = color_inactivo
        self.color_activo = color_activo
        self.tamaño_letra = 25
        self.myFond = pygame.font.SysFont('Times New Roman', self.tamaño_letra)
        self.valor = valor

    def renderizar_texto(self,screen):
        texto = self.myFond.render(self.valor,True,"black")
        posicion = self.posicion_x + ((self.ancho - 10 ) / 2), self.posicion_y + 5 + ((self.alto - 10 ) /2 - (self.tamaño_letra / 2))
        screen.blit(texto,posicion)
    
    def comprobacion(self,mouse):
        mouse_posicion = mouse.get_pos()
        if (self.ancho + self.posicion_x >= mouse_posicion[0] >= self.posicion_x) and (self.alto + self.posicion_y >= mouse_posicion[1] >= self.posicion_y):
            return True
        
        return False

    def accion(self,mouse,click,screen):
        if self.comprobacion(mouse):
            if click == 1:
                if self.valor in ["+","*","/","-"]:
                    if screen.input and screen.input[-1] in ["+","*","/","-"]:
                        screen.input = screen.input[:-1] + self.valor
                    elif screen.input:
                        screen.input += self.valor
                elif self.valor == "=":
                    screen.manejo_respuesta()
                else:
                    screen.input += self.valor

    def dibujar(self,screen,mouse):

        pygame.draw.rect(screen, (0,0,0), (self.posicion_x,self.posicion_y,self.ancho,self.alto))

        if self.comprobacion(mouse):
            pygame.draw.rect(screen, self.color_activo, (self.posicion_x+5,self.posicion_y+5,self.ancho - 10,self.alto - 10))

        else:
            pygame.draw.rect(screen, self.color_inactivo, (self.posicion_x+5,self.posicion_y+5,self.ancho - 10,self.alto - 10))
        
        
        self.renderizar_texto(screen)