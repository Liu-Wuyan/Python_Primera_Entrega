""" Descripción: Un tablero de ajedrez con 32 piezas (16 blancas y 16 negras); las 32 piezas se encontrarán en sus
casillas iniciales; sin posibilidad de movimiento """


#Constantes del tablero
DIMENSION_TABLERO: int = 8 #Corregido
LETRAS_VALIDAS: str = ("abcdefgh")
NUMEROS_VALIDOS: str = ("12345678")

"""Las variables/constantes de nuestra tabla, poniendo en mayúscula TABLEROS_SÍMBOLO y en forma de listas de lista,
unicodes representado lo que es cada pieza en forma de strings en cada casilla. la lista externa representando las
filas y la lista externa las columnas"""

#Posición de las piezas
TABLERO_SIMBOLOS: list[list[str]] = [ #Asignando los símbolos por listas dentro de listas
    ["\u265C","\u265E","\u265D","\u265B","\u265A","\u265D","\u265E","\u265C"], #Símbolos de la fila 8
    ["\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F","\u265F"], #Símbolos de la fila 7
    ["","","","","","","",""], #Símbolos de la fila 6
    ["","","","","","","",""], #Símbolos de la fila 5
    ["","","","","","","",""], #Símbolos de la fila 3
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

"""Cremos un encabezado vacío, creamos un bucle para las columnas, otro para las filas y uno interno para las filas. La acción será, por ejemplo
llegar a la fila 8 y llegar a la columna 0, consultar e imprimir, seguir en la fila 8 e ir a la columna 1; así hasta completarla y pasar a la 
siguiente fila (a la 7) y repetir el mismo proceso con las siguientes filas"""

encabezado: str = "  " 

for indice_columna in range(DIMENSION_TABLERO): #Bucle que recorrerá las 8 columnas
    letra_columna: str = LETRAS_VALIDAS[indice_columna] #Se busca en LETRAS_VALIDAS las letras que corresponden con las posiciones
    encabezado: str = encabezado + " " + letra_columna + " " #Lo que estaba acumulado en el encabezado, un espacio, la letra que corresponida a la posición y otro espacio
print(encabezado) #Muestra el encabezado

for indice_fila in range(DIMENSION_TABLERO): #Recorre de arriba abajo las filas
    numero_fila: int = DIMENSION_TABLERO - indice_fila #Orden del 8 al 1 restando 8-0=8,siguiente bucle 8-1=7,...etc. 
    linea: str = str(numero_fila) + " " #Al número recién calculado se le añade un espacio "8 "
    for indice_columna in range(DIMENSION_TABLERO):#Bucle interno que recorre la fila cuando el bucle externo está en una fila
        simbolo: str = TABLERO_SIMBOLOS[indice_fila][indice_columna] #Accede a la lista de listas y ver qué hay
        if simbolo == "": #Si fila vacía
            celda: str = " . "
        else:
            celda: str = " " + simbolo + " " #Poner ese símbolo entre dos espacios para alinear
        linea: str = linea + celda #A la línea con el número se le añade la celda correspondiente
    print(linea)
#instrucciones finales después de imprimir la tabla de ajedrez
print(" ") #Espacio visual
print("Introduzca una casilla (por ejemplo e2) o salir para terminar") 
print(" ")


""" Máquina de estados, la máquina de estados servirá para alternar los turnos de blancas y negras y jaque finalizar la partida """





