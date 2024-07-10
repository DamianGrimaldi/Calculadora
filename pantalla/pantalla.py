import pygame

class Pantalla():
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.input = ""
        self.myFond = pygame.font.SysFont('Times New Roman', 25)
        self.respuesta = "0"
        self.reemplazo = {
            "[0]": "0", "[1]": "1", "[2]": "2", "[3]": "3", "[4]": "4",
            "[5]": "5", "[6]": "6", "[7]": "7", "[8]": "8", "[9]": "9",
            "[+]": "+", "[*]" : "*", "[-]" : "-" , "[.]" : ".", "[/]" : "/"
        }
        self.screen = pygame.display.set_mode((self.ancho,self.alto))

    def mostrar(self):
        texto = self.myFond.render(self.input,True,"black")
        posicion = ((10,95))
        self.screen.blit(texto,posicion)

    def manejo_respuesta(self):
        pass

    def manejo_teclado(self,key):
        if key == pygame.K_RETURN or key == pygame.K_KP_ENTER:
            self.manejo_respuesta()
        elif key == pygame.K_BACKSPACE:
            self.input = self.input[:-1]

    def dibujar(self,botones,mouse):
        
        self.screen.fill((144,44,100))
        
        for boton_lista in botones:
            for boton in boton_lista:
                boton.dibujar(self.screen,mouse)
        
        self.mostrar()