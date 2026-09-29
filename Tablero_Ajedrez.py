""" Descripción: Un tablero de ajedrez con 32 piezas (16 blancas y 16 negras); las 32 piezas se encuentran en sus casillas iniciales """


#Constantes del tablero
TAMAÑO_TABLERO: int = 8
LETRAS_VALIDAS: str = ("abcdefgh")
NUMEROS_VALIDOS: str = ("12345678")

#A continuación procederemos a crear las variables de nuestra tabla, poniendo en mayúscula TABLEROS_SÍMBOLO y metiendo una lista dentro de
#de otra lista metiendo unicodes en forma de strings estamos detallando de fila en fila y de columna y columna qué pieza está en cada casilla
#

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

#Ahora, con el mismo proceso de lsitas dentro de listas vamos a convertir esas unicodes en palabras, para que a la hora de consultar
#nos enseñe qué es esa pieza.


 