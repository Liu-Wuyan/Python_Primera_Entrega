"""El tablero de ajedrez es jugable y puede incluír nuevas herramientas como las funciones, clases,...etc"""


"""clase Pieza; el molde de una pieza es ella misma(self), color,
y el símbolo que representa y la función de movimiento que realiza
y la función de movimiento válido ( = camino libre) que servirá a 
la hora de mover una pieza de su casilla de origen a la de destino"""



class Pieza:
   
    def __init__(self, color: str, simbolo: str) -> None:
        self.color: str = color
        self.simbolo: str = simbolo


    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
       return False
    

    def camino_libre(self, origen: tuple[int,int], destino: tuple[int,int], tablero) -> bool:
        fila_origen, columna_origen = origen[0], origen[1]
        fila_destino, columna_destino = destino[0], destino[1]

        if fila_destino > fila_origen: #dependiendo de si es mayor, menor o igual entonces se ha movido x
            movimiento_fila = 1 
        elif fila_destino < fila_origen:
            movimiento_fila = -1
        else:
            movimiento_fila = 0

        if columna_destino > columna_origen:
            movimiento_columna = 1
        elif columna_destino < columna_origen:
            movimiento_columna = -1
        else:
            movimiento_columna = 0

        fila_start= fila_origen + movimiento_fila #comienza desde la casilla después del origen
        columna_start = columna_origen + movimiento_columna

        while(fila_start, columna_start) != (fila_destino, columna_destino): #recorre las casillas de la jugada desde la casilla siguiente a la original a la de ddestino
            if tablero.casillas[fila_start][columna_start] is not None: #si se topa con una pieza
                return False

            fila_start += movimiento_fila
            columna_start += movimiento_columna

        return True #si no hay obstáculos


        
#Herencias     

class Torre(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♖"
        else:
            simbolo = "♜"
        super().__init__(color, simbolo)


    def es_movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int], tablero) -> bool:
       return (((origen [0] == destino [0]) != (origen [1] == destino [1]) and (origen != destino)) and self.camino_libre(origen, destino, tablero))

    

class Alfil(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♗"  
        else:
            simbolo = "♝"
        super().__init__(color, simbolo)


    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int], tablero) -> bool:
        return ((abs(destino[0] - origen[0]) == abs(destino[1] - origen[1]) and (origen != destino)) and self.camino_libre(origen, destino, tablero))



class Caballo(Pieza):
   
    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♘"
        else:
            simbolo = "♞"  
        super().__init__(color, simbolo)


    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        return ((abs(origen[0] - destino[0]) == 2 and abs(origen[1] - destino[1]) == 1) or (abs(origen[0] - destino[0]) == 1
                and abs(origen[1] - destino[1]) == 2))



class Peon(Pieza):

    def __init__(self, color: str) -> None:
        if color == "blanco":
            simbolo = "♙"
        else:
            simbolo = "♟"
        super().__init__(color, simbolo)


    def movimiento_valido(self, origen: tuple[int,int], destino: tuple[int,int], tablero) -> bool:
        if self.color == "blanco":
            direccion = -1
            fila_inicial = 6
        else:
            direccion = 1
            fila_inicial = 1

            pieza_destino = tablero.casillas[destino[0]][destino[1]]

        return (((destino[0] - origen[0] == direccion and origen[1] == destino[1] and pieza_destino is None) #avanzar casilla a casilla
                or (origen[0] == fila_inicial and destino[0] - origen[0] == (direccion * 2) and origen[1] == destino[1] and pieza_destino is None) #avanzar dos casillas si está en posición inicial
                or (destino[0] - origen[0] == direccion and abs(origen[1] - destino[1] == 1) and pieza_destino is not None and pieza_destino.color != self.color)) #casilla en diagonal
                #para la daigonal, el peón se mueve una casilla adelante, una casilla an la columna(derecha o izquerda) y en la csilla de destino debe haver una pieza enemiga
                and self.camino_libre(origen, destino, tablero))



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
        if color == "blanco":
            simbolo = "♕"
        else:
            simbolo = "♛"
        super().__init__(color, simbolo)


    def movimento_valido(self, origen: tuple[int,int], destino: tuple[int,int], tablero) -> bool:
        return (((origen [0] == destino [0]) != (origen [1] == destino [1])
                and (origen != destino)) or (abs(destino[0] - origen[0]) == abs(destino[1] - origen[1])
                and (origen != destino)) and self.camino_libre(origen, destino, tablero)
                and self.camino_libre(origen, destino, tablero))
       



        
"""La clase Tablero; es una matriz 8*8 (de 8 a 1 y de 'a' a 'h') que contendrá las piezas.
Sus funciones son la de colocar, para colocar las piezas; obtener,
para saber qué pieza se encuentra en qué casilla; imprimir, que nos
imprime el tablero; convertir, para la conversión del imput a la hora de 
jugar en cooredenadas; mover, para mover una pieza desde el origen hasta
el destino. Pero también están las fucniones para coronar al peón,jaque
y jaque mate que se llaman en la función mover. Y por último, colocar
piezas iniciales, con la función colocar. """

#Clase tablero
class Tablero:

    def __init__(self) -> None:
        self.fin_por_jaque_mate: bool = False
        self.casillas: list[list[Pieza | None]] = []
        for fila in range(8):
            fila_vacia: list[Pieza | None] = [None] * 8
            self.casillas.append(fila_vacia)
        

    def colocar(self, pieza: Pieza, fila: int, columna: int) -> None:
        self.casillas[fila][columna] = pieza


    def obtener(self, fila: int, columna: int) -> Pieza | None:
        return self.casillas[fila][columna]
    

    def imprimir(self) -> None:
        letras = "abcdefgh" #columnas
    
        letras_columna: str = "  "
        for columna in range(8):
            letras_columna += f"{letras[columna]}"
        print(letras_columna)

        for fila in range(8): #filas
            linea: str = str(8 - fila)
            for columna in range(8):
                pieza: Pieza | None = self.casillas[fila][columna]
                if pieza is None:
                    linea: str = linea + "  "
                else:
                    linea: str = linea + " " + pieza.simbolo
            print(linea)


    def coronar_peon(self, destino: tuple[int,int]) -> None:
        pieza_actual = self.casillas(destino)
        color_peon = pieza_actual.color

        convertir = input("Converitir en (opciones : torre, alfil, caballo o dama):").strip().lower() #siguiendo el input, se convierte el peon
        if convertir in ["dama", "reina"]:
            self.casillas[destino[0]][destino[1]] = Dama(color_peon)
        elif convertir == "torre":
            self.casillas[destino[0]][destino[1]] = Torre(color_peon)
        elif convertir == "alfil":
            self.casillas[destino[0]][destino[1]] = Alfil(color_peon)
        elif convertir == "caballo":
            self.casillas[destino[0]][destino[1]]
        else:
            print("⚠ LA OPCIÓN NO SE HA RECONOCIDA, POR FAVOR INTRODUZCA UNA OPCIÓN VÁLIDA ⚠")  

        print(f"---Coronación exitosa en {convertir}---") 


    def convertir_letra(self, coordenada: str) -> tuple[int,int]:
        try:
            coordenada = coordenada.strip().lower() #separa y conviente en minúscula
            if len(coordenada) != 2:
                return None
            
            letra_columna = coordenada[0].lower()
            numero_fila = int(coordenada[1])

            columna = ord(letra_columna) - ord("a")
            fila = 8 - numero_fila

            if not (0 <= fila < 8 and 0 <= columna < 8): #deben estar las coordenadas entre 0 y 7
                return None

            return (fila, columna)
        except(ValueError,IndexError,TypeError):  #para evitar fallos 
            return None

    
    def jaque(self, color_rey: str) -> bool:
        posicion_rey = None #creamos la variable inicial
        if color_rey == "blanco":
            color_enemigo = "negro"
        else:
            color_enemigo = "blanco"

        for fila in range(8): #recorremos el tablero en busca del rey
            for columna in range(8):
                pieza = self.casillas
                if pieza is not None and type(pieza).__name__.lower() == "rey" and pieza.color == color_rey: #si la casilla no está vacía y es el rey
                    posicion_rey = (fila, columna) #guarda la coordenada en posicion_rey
                    break #terminamos el recorrido interno una vez encontrado el rey
                if posicion_rey: #nos salimos del bucle interno
                    break
                if not posicion_rey: #en el caso de que n se encuentre
                    return False

        for fila in range(8): #recorre el tablero por piezas enemigas
            for columna in range(8):
                pieza = self.casillas[fila][columna]
                if pieza is not None and pieza.color == color_enemigo:
                    if pieza.movimiento_valido((fila,columna), posicion_rey, self): #si el movimiento de la pieza enemiga puede llegar al rey
                        print("⚠ EL REY ESTÁ EN JAQUE ★")
                        return True

        return False


    def jaque_mate(self, color_rey: str) -> bool:
        if not self.jaque(color_rey): #primero compreobamos si está en jaque
            return False

        for fila_pieza in range(8): #recorremos el tablero en busca de una pieza cuyo movimiento salvara al rey
            for columna_pieza in range(8):
                pieza = self.casillas[fila_pieza][columna_pieza]
                if pieza is not None and pieza.color == color_rey: #es uan pieza del mismo bando que el rey
                    for fila_pieza_movimiento in range(8): #comprobamos el moviemnto de esta pieza que lo salva 
                        for columna_pieza_movimiento in range(8): 
                            origen = (fila_pieza, columna_pieza)
                            destino = (fila_pieza_movimiento, columna_pieza_movimiento)

                            if pieza.movimiento_valido(origen, destino, self): #verifivamos si la pieza piiede relizar ese movimiento
                                pieza_destino = self.casillas[fila_pieza_movimiento][columna_pieza_movimiento] #simulamos el destino que haría la pieza,teniendo en cuenta la que podrá estar en la casilla de destino
                                if pieza_destino is None or pieza_destino.color != color_rey: #comprobamos que no sea una pieza del mismo bando que el rey
                                    self.casillas[fila_pieza_movimiento][columna_pieza_movimiento] = pieza
                                    self.casillas[fila_pieza][columna_pieza] = None

                                    sigue_jaque = self.jaque(color_rey) #comprobamos si el rey aún estaría en jaque
                                    self.casillas[fila_pieza][columna_pieza] = pieza #deshacemos el movimiento
                                    self.casillas[fila_pieza_movimiento][columna_pieza_movimiento] = pieza_destino #devolvemos si había, la pieza que estaba originalmente
                                
                                    if not sigue_jaque: #si no está en jaque
                                        return False

        return True
    

    def mover(self, origen: tuple[int,int], destino: tuple[int,int]) -> bool:
        pieza = self.obtener(origen[0], origen[1]) #mira el origen
        if pieza is None:
            print("⚠ LA CASILLA ESTÁ VACÍA, POR FAVOR SELECCIONE UNA CASILLA NO VACÍA DE TU COLOR ⚠")
            return False
        
        pieza_destino = self.casillas[destino[0], destino[1]] #para que la casilla de destino no sea una no nemiga
        if pieza_destino is not None and pieza_destino.color == pieza.color:
            print("⚠ LA CASILLA DE DESTINO ESTÁ OCUPADA POR UNA PIEZA DE TU PROPIO COLOR, NO ES POSIBLE LA JUGADA ⚠")
            return False
    
        if not pieza.movimiento_valido(origen,destino,self): #llama a la pieza y mira su movimiento válido
            print("⚠ LA PIEZA SELECCIONADA NO REALIZA ESTE TIPO DE MOVIMIENTO O HAY UNA PIEZA QUE OBSTACULIZA LA JUGADA, POR FAVOR INTRODUZCA UNA JUGADA VÁLIDA ⚠")
            return False

        if pieza_destino is not None:
            print("★ CAPTURA VICTORIOSA ★")

        self.casillas[destino[0]],[destino[1]] = pieza
        self.casillas[origen[0]],[origen[1]] = None
        
        #después de colocarse la pieza, si es peón y llega al borde contario, se realiza la coronación
        if type(pieza).__name__ == "Peon":
            if (pieza.color == "blanco" and destino[0] == 0) or (pieza.color == "negro" and destino[0] == 7):
                print(" FELICIDADES, EL PEÓN SE CORONARÁ")
                self.coronar_peon(destino)

        if pieza.color == "blanco": #mira el color de las piezas del turno
            color_contrario = "negro"  
        else:
            color_contrario = "blanco"

        if self.jaque(color_contrario):
            print("★ JAQUE ★")
        elif self.jaque_mate(color_contrario):
            print("★ JAQUE MATE, FIN DE LA PARTIDA ★")
            self.fin_por_jaque_mate = True #se activa el atributo
            return True 


        return True
                


#Se colocan las piezas
    def colocar_piezas_iniciales(self) -> None:
        self.colocar(Torre("negra"), 0, 0)
        self.colocar(Caballo("negro"), 0, 1)
        self.colocar(Alfil("negro"), 0, 2)
        self.colocar(Rey("negro"), 0, 3)
        self.colocar(Dama("negra"),0 ,4)
        self.colocar(Alfil("negro"),0 ,5)
        self.colocar(Caballo("negro"),0 ,6)
        self.colocar(Torre("negra"),0 ,7)
        self.colocar(Peon("negro"),1 ,0)
        self.colocar(Peon("negro"),1 ,1)
        self.colocar(Peon("negro"),1 ,2)
        self.colocar(Peon("negro"),1 ,3)
        self.colocar(Peon("negro"),1 ,4)
        self.colocar(Peon("negro"),1 ,5)
        self.colocar(Peon("negro"),1 ,6)
        self.colocar(Peon("negro"),1 ,7)

#Piezas blancas
        self.colocar(Torre("blanca"), 7, 0)
        self.colocar(Caballo("blanco"), 7, 1)
        self.colocar(Alfil("blanco"), 7, 2)
        self.colocar(Rey("blanco"), 7, 3)
        self.colocar(Dama("blanca"),7 ,4)
        self.colocar(Alfil("blanco"),7 ,5)
        self.colocar(Caballo("blanco"),7 ,6)
        self.colocar(Torre("blanca"),7 ,7)
        self.colocar(Peon("blanco"),6 ,0)
        self.colocar(Peon("blanco"),6 ,1)
        self.colocar(Peon("blanco"),6 ,2)
        self.colocar(Peon("blanco"),6 ,3)
        self.colocar(Peon("blanco"),6 ,4)
        self.colocar(Peon("blanco"),6 ,5)
        self.colocar(Peon("blanco"),6 ,6)
        self.colocar(Peon("blanco"),6 ,7)
        self.imprimir()


 

    
print("    ¡¡BIENVENI@!!    ")





"""Para poder guardar las jugadas, la partida y poder retomarla,
creamos la función guardar_historial que se usará para guardar cada movimiento.
Cargar_historial, para retomar partidas. Y exportar_historial,
para visualizar las jugadas realizadas"""

import os

def guardar_historial(jugadas: list[str], ruta: str) -> None:
    with open(ruta, "w", encoding = "utf-8") as fichero: #se abre el fichero
        for jugada in jugadas:
            fichero.write(f"{jugada}\n") # se guarda cada jugada en lineas con salto de línea
   

import csv

def exportar_historial_csv(jugadas: list[str], ruta: str) -> None:
    with open(ruta, "w", newline = "", encoding = "utf-8") as fichero: #abre el fichero en modo escritura
        escritor = csv.writer(fichero) #se abre el escritor  csv
        escritor.writerow(["numero", "turno", "origen", "destino"]) #la cabecera de las líneas
        for numero, mov in enumerate(jugadas, start = 1): #enumera el número de juagadas y las jugadas que se realizan
            if numero % 2 == 1: #como simpre empiezan las blancas, son las jugadas impares
                turno_str = "blancas" 
            else:
                turno_str = "negras"
            origen_str, destino_str = jugada.split() #separa origen y movimiento

            escritor.writerow([numero, turno_str, origen_str, destino_str]) #con los datos recogidos, se escriben


def cargar_historial(ruta: str) -> list[str]: #recibe una ruta, por ejemplor partida.txt
    jugadas: list[str] = [] #preparamos la lista vacía
    with open(ruta, "r", encoding = "utf-8") as fichero: #abre el fichero en modo lectura
            for linea in fichero: #recorre el fichero linea a linea
                depurado = linea.strip() #elimina saltos de linea (\n) para la variable depurado
                if depurado: #si al eliminar el salto de línea, no es una jugada vacía
                    jugadas.append(depurado) #las jugadas del fichero se añaden a juagadas
            return jugadas #devulve las jugadas ya limpias









#--Bucle principal del juego--

"""En el bucle principal, se chequea si hay partidas guardadas,
se pregunta si se quiere retomar o no. Si no hay partidas guardadas o no se retoma,
se le pide al jugador del turno ingresar una jugada. Mientras que el estado no sea
guardar o fin de partida se alterna entre blancas y negras. Se ha creado una función (turno)
que recoge todo el proceso de un turno para no duplicar el código para cada turno (blancas y negras)"""

estado: str = "blancas"

def turno(tablero: "Tablero", jugadas: list[str], color_turno: str, estado: str, siguiente_turno: str) -> str: # en vez de duplicar el código, creamos una función que lo lleve
    tablero.imprimir()
    print(f"Turno de las {estado}")
    print("---Puede introducir 'salir', 'guardar' o una jugada (origen destino) ej: 'a2 a3---")

    eleccion = input ("→ ").strip().strip("'\"") #recibe con input

    if eleccion.lower() == "salir": #si la opción es salir
        print("---Se ha seleccionado salir---")
        return "fin_partida"

    if eleccion.lower() == "guardar": #si la opción es guardar, se llama a la función para gaurdar el historial
        guardar_historial(jugadas, "partida.txt")
        print("---Se ha seleccionado guardar---")
        return estado

    troceado = eleccion.split() #si se introduce una jugada convierte por ejmplo de a2 a3 a "a2" "a3"
    if len(troceado) != 2: #verificar si no es de 2
        print("⚠ INTRODUZCA EL ORIGEN Y DESTINO CON UN ESPACIO , EJ: 'a2 a3' ⚠")
        if color_turno == "blanco":
            return "blancas"
        else:
            return "negras"
        
    origen = tablero.convertir_letra(troceado[0]) #correspondría por ejmplo a "a2"
    destino = tablero.convertir_letra(troceado[1]) #correspondría por ejmplo a "a3"
    if origen is None or destino is None:
        print("⚠ LA COORDENADA NO ES VÁLIDA , POR FAVOR INTRODUZCA UNA COORDENADA VÁLIDA ⚠")
        return estado #seguimos en el mismo estado 
    
    pieza = tablero.obtener(origen[0], origen[1])
    if pieza is not None and pieza.color != color_turno: #mira que no se seleccione una pieza del enemigo
       print("⚠ NO PUEDE MOVER UNA PIEZA ENEMIGA, POR FAVOR SELECCIONE UNA PIEZA DE SU TURNO ⚠")

    if tablero.mover(origen, destino):
        jugadas.append(f"{troceado[0]} {troceado[1]}")
        guardar_historial(jugadas, "partida.txt")
        tablero.imprimir()
        if tablero.fin_por_jaque_mate:
                return "fin_partida"
        return siguiente_turno
    
        
    return estado




 #En este punto comenzaría la partida, se imrpime el tablero y comienza la partida




tablero = Tablero() #se crea el tablero, se colocan las piezas iniciales, se deja comenzaso la lista donde se guardarán las jugadsa y comienzan las blancas
tablero.colocar_piezas_iniciales
jugadas: list[str] = []
estado = "blancas"

if os.path.exists("partida.txt"): #si existe un fichero anterior, se pregunta si se quiere retomar
    respuesta = input("---Existe una partida anterior, ¿Se desea exportarla? (introduzca s ,para retomarla)---")
    if respuesta == "s": 
        historial_cargado = cargar_historial("partida.txt") #si se respone que se quiere retomar, se carga la partida
        tablero_prueba = Tablero() # se simula una tablero, se ponen las piezas iniciales
        tablero_prueba.colocar_piezas_iniciales()
        valido = True
        for jugada in historial_cargado: #recorre cada jugada 
            troceado = jugada.split()
            if len(troceado) != 2: #si no está compuesto de dos partes
                valido = False
                break
            origen = tablero_prueba.convertir_letra(troceado[0]) #del caso contrario, las concierte en coordenadas
            destino = tablero_prueba.convertir_letra(troceado[1])
            if origen is None or destino is None or not tablero_prueba.mover(origen, destino): #si no hay origen, destino y al aplicar las jugadas en el tablero de prueba ocurre un error
                valido = False
                break

        if not valido: #si no devuelve True
            print("⚠ EL ARCHIVO NO ES VALIDO ⚠")
        elif tablero_prueba.fin_por_jaque_mate:
            print("---La partida gaurdada ya había termiando. Se empieza una partida nueva---")
        else: #
            tablero = tablero_prueba
            jugadas = historial_cargado
            if len(jugadas) % 2 == 1: #para retomar el turno, si hay por ejemplor 3 (impar) jugadas = blnacas, negras, blancas. Le correspondrían a las negras 
                estado = "negras"
            else:
                estado = "blancas"



while estado  != "fin_partida":
    if estado == "blancas":
        estado = turno(tablero, jugadas, "blanco", "blancas", "negras") #aquí están los cuatro atributos que definimos para la función 
    elif estado == "negras":
        estaddo = turno(tablero, jugadas, "negro", "negras", "blancas")

