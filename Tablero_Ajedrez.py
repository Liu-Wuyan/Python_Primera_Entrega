""" Descripción: Un tablero de ajedrez con 32 piezas (16 blancas y 16 negras); las 32 piezas se encontrarán en sus
 casillas iniciales; sin
posibilidad de moverse """


#Constantes del tablero
TAMAÑO_TABLERO: int = 8
LETRAS_VALIDAS: str = ("abcdefgh")
NUMEROS_VALIDOS: str = ("12345678")

"""Las variables/constantes de nuestra tabla, poniendo en mayúscula TABLEROS_SÍMBOLO y en forma de listas de lista,
unicodes representado lo que es cada pieza en forma de strings en cada casilla. la lista externa representando las
filas y la lista expterna las columnas"""

#Posición de las piezas
TABLERO_SIMBOLOS: list[list[str]] = [ #Asignando los símbolos por listas dentro de listas
    ["\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"], #Símbolos de la fila 8
    ["\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F"], #Símbolos de la fila 7
    [" . "," . "," . "," . "," . "," . "," . "," . "], #Símbolos de la fila 6
    [" . "," . "," . "," . "," . "," . "," . "," . "], #Símbolos de la fila 5
    [" . "," . "," . "," . "," . "," . "," . "," . "], #Símbolos de la fila 4
    [" . "," . "," . "," . "," . "," . "," . "," . "], #Símbolos de la fila 3
    ["\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659","\u2659"], #Símbolos de la fila 2
    ["\u2656","\u2658","\u2657","\u2655","\u2654","\u2657","\u2658","\u2656"] #Símbolos de la fila 1
 ] 

"""Ahora,con otra lista de listas para determinar qué pieza correspone"""

TABLERO_NOMBRES: list[list[str]] = [
    ["Torre_negra","Caballo_negro","Alfil_negro","Dama_negra","Rey_negro","Alfil_negro","Caballo_negro","Torre_negra"],
    ["Peón_negro","Peón_negro","Peón_negro","Peón_negro","Peón_negro","Peón_negro","Peón_negro","Peón_negro"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["Peón_Blaco","Peón_Blaco","Peón_Blaco","Peón_Blaco","Peón_Blaco","Peón_Blaco","Peón_Blaco","Peón_Blaco"],
    ["Torre_blanca","Caballo_blanco","Alfil_blanco","Dama_blanca","Rey_blanco","Alfil_blanco","Caballo_blanco","Torre_blanca"]
]
 
encabezado: str = " " #creamos 