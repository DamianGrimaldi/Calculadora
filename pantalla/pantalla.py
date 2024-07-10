import pygame

class Pantalla():
    def __init__(self,ancho,alto, tamaño_y) -> None:
        self.ancho = ancho
        self.alto = alto
        self.tamaño_y = tamaño_y
        self.tamaño_letra = 25
        self.input = "0"
        self.myFond = pygame.font.SysFont('Times New Roman', self.tamaño_letra)
        self.respuesta = "0"
        self.teclas_validas = [
            "[0]", "0", "[1]", "1", "[2]", "2", "[3]", "3", "[4]", "4",
            "[5]", "5", "[6]", "6", "[7]", "7", "[8]", "8", "[9]", "9","[+]", "[*]", "[-]", "[.]", "[/]"
        ]
        self.reemplazo = {
            "[0]": "0", "[1]": "1", "[2]": "2", "[3]": "3", "[4]": "4",
            "[5]": "5", "[6]": "6", "[7]": "7", "[8]": "8", "[9]": "9",
            "[+]": "+", "[*]" : "*", "[-]" : "-" , "[.]" : ".", "[/]" : "/"
        }
        self.screen = pygame.display.set_mode((self.ancho,self.alto))

    def mostrar(self):
        texto = self.myFond.render(self.input,True,"black")
        posicion = (10,(self.tamaño_y - self.tamaño_letra))
        self.screen.blit(texto,posicion)
        
        #respuesta en pantalla
        
        texto = self.myFond.render ("Respuestas: ",True, "black")
        posicion = (10, 10)
        self.screen.blit(texto,posicion)
        
        texto = self.myFond.render (self.respuesta,True, "black")
        posicion = (10, 10+self.tamaño_letra)
        self.screen.blit(texto,posicion)

    def manejo_respuesta(self):
        try:
            self.respuesta = str(eval(self.input))
            self.input = self.respuesta
        except Exception as e:
            self.respuesta = "Syntax error"
            self.input = "0"

    def manejo_teclado(self,key):
        
        key_name = pygame.key.name(key)
        
        if key == pygame.K_RETURN or key == pygame.K_KP_ENTER:
            self.manejo_respuesta()
        elif key == pygame.K_BACKSPACE:
            self.input = self.input[:-1]
        elif key == pygame.K_ESCAPE:
            self.input = "0"
        elif key_name in self.teclas_validas:
            if key_name in  ["[+]","[*]","[/]","[-]"]:
                if self.input and self.input[-1] in ["+","*","/","-"]:
                        self.input = self.input[:-1] + self.reemplazo[key_name]
                elif self.input:
                    self.input += self.reemplazo[key_name]
            elif key_name == "[.]":
                if self.input and self.input[-1] != ".":
                        self.input += self.reemplazo[key_name]
            elif key_name in self.reemplazo:
                self.input += self.reemplazo[key_name]
            else:
                self.input +=  key_name

    def dibujar(self,botones,mouse):
        
        self.screen.fill((144,44,100))
        
        for boton_lista in botones:
            for boton in boton_lista:
                boton.dibujar(self.screen,mouse)
        
        self.mostrar()