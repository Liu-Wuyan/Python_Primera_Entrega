"""El tablero de ajedrez es jugable y puede incluír nuevas herramientas como las funciones, clases,...etc"""
#Las cuatro funciones necesarias:
#Función de validación
#Función de conversión
#Función de consulta
#Función de impresión


"""clase Pieza, el molde de una pieza es ella misma(self), color,
y el símbolo que representa y la función de movimiento válido"""



class Pieza:
   
    def __init__(self, color: str, simbolo: str) -> None:
        self.color: str = color
        self.simbolo: str = simbolo

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
       return False
       

class Torre(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo = "♖"
        else:
            simbolo = "♜"
        super().__init__(color, simbolo)

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
       return ((origen [0] == destino [0]) != (origen [1] == destino [1]) and (origen != destino))
    

class Alfil(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♗"  
        else:
            simbolo = "♝"
        super().__init__(color, simbolo)

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        return (abs(destino[0] - origen[0]) == abs(destino[1] - origen[1]) and (origen != destino))


class Caballo(Pieza):
   
    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♘"
        else:
            simbolo = "♞"  
        super().__init__(color, simbolo)

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        return ((abs(origen[0] - destino[0]) == 2 and abs(origen[1] - destino[1]) == 1) or (abs(origen[0] - destino[0]) == 1 and abs(origen[1] - destino[1]) == 2))



class Peon(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♙"
        else:
            simbolo = "♟"
        super().__init__(color, simbolo)

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        if self.color == "blanco":
            direccion = -1
            fila_inicial = 6
        else:
            direccion == 1
            fila_inicial = 1

        return ((destino[0] - origen[0] == direccion and origen[1] == (direccion * 2) and origen[1] == destino[1]) or origen[0] == fila_inicial and destino[0] - origen[0] == (direccion * 2) and origen[1] == destino[1]) or (destino[0] - origen[0] == direccion and abs(origen[1] - destino[1] == 1))



class Rey(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♔"
        else:
            simbolo = "♚"
        super().__init__(color, simbolo)

    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        return (abs(destino[0] - origen[0]) <= 1 and abs(destino[1] - origen[1]) <= 1) and (origen != destino) 


class Dama(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanca":
            simbolo = "♕"
        else:
            simbolo = "♛"
        super().__init__(color, simbolo)

    def movimento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        return ((origen [0] == destino [0]) != (origen [1] == destino [1]) and (origen != destino)) or (abs(destino[0] - origen[0]) == abs(destino[1] - origen[1]) and (origen != destino))
       



        
   

#clase tablero
class Tablero:

    def __init__(self) -> None:
        self.casillas: list[list[Pieza | None]] = []
        for fila in range(8):
            fila_vacia: list[Pieza | None] = [None] * 8
            self.casillas.append(fila_vacia)

    def colocar(self, pieza: Pieza, fila: int, columna: int) -> None:
        self.casillas[fila][columna] = pieza

    def obtener(self, fila: int, columna: int) -> Pieza | None:
        return self.casillas[fila][columna]

    def imprimir(self) -> None:
        for fila in range(7, -1):
            linea: str = str(fila + 1)
            for columna in range(8):
                pieza: Pieza | None = self.casillas[fila][columna]
                if pieza is None:
                    linea: str = linea + "  "
                else:
                    linea: str = linea + " " + pieza.simbolo
            print(linea)

    def mover(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        pieza = self.obtener(origen[0], origen[1])
        if pieza is None:
            return False
        if pieza.movimiento_valido(origen, destino):
            self.casillas[destino[0]][destino[1]] = pieza
            self.casillas[origen[0]][origen[1]] = None
            return True

        return False 


#coloco las piezas
tablero = Tablero()
#Piezas negras
tablero.colocar(Torre("negra"), 0, 0)
tablero.colocar(Caballo("negro"), 0, 1)
tablero.colocar(Alfil("negro"), 0, 2)
tablero.colocar(Rey("negro"), 0, 3)
tablero.colocar(Dama("negra"),0 ,4)
tablero.colocar(Alfil("negro"),0 ,5)
tablero.colocar(Caballo("negro"),0 ,6)
tablero.colocar(Torre("negra"),0 ,7)
tablero.colocar(Peon("negro"),1 ,0)
tablero.colocar(Peon("negro"),1 ,1)
tablero.colocar(Peon("negro"),1 ,2)
tablero.colocar(Peon("negro"),1 ,3)
tablero.colocar(Peon("negro"),1 ,4)
tablero.colocar(Peon("negro"),1 ,5)
tablero.colocar(Peon("negro"),1 ,6)
tablero.colocar(Peon("negro"),1 ,7)

#Piezas blancas
tablero.colocar(Torre("blanca"), 7, 0)
tablero.colocar(Caballo("blanco"), 7, 1)
tablero.colocar(Alfil("blanco"), 7, 2)
tablero.colocar(Rey("blanco"), 7, 3)
tablero.colocar(Dama("blanca"),7 ,4)
tablero.colocar(Alfil("blanco"),7 ,5)
tablero.colocar(Caballo("blanco"),7 ,6)
tablero.colocar(Torre("blanco"),7 ,7)
tablero.colocar(Peon("blanco"),6 ,0)
tablero.colocar(Peon("blanco"),6 ,1)
tablero.colocar(Peon("blanco"),6 ,2)
tablero.colocar(Peon("blanco"),6 ,3)
tablero.colocar(Peon("blanco"),6 ,4)
tablero.colocar(Peon("blanco"),6 ,5)
tablero.colocar(Peon("blanco"),6 ,6)
tablero.colocar(Peon("blanco"),6 ,7)
tablero.imprimir()







    




   

