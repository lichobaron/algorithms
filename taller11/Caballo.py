## -------------------------------------------------------------------------
##CalcularPosiciones: Calcula las posiciones a las que la ficha del caballo puede avanzar.
##Entradas:
##	- x: posición fila actual del caballo.
##	- y: posición columna actual del caballo.
##  - n: Tamaño del lado del tablero.
##Salidas:
##	- P: Posibles posiciones que puede avanzar el caballo.
## -------------------------------------------------------------------------
def CalcularPosiciones (x,y,n):
    P = []
    V = [-2,-1,1,2]
    for i in range(0,len(V)):
        k = x + V[i]
        for j in range(0,len(V)):
            if abs(V[i]) != abs(V[j]):
                l = y +V[j]
                if k>=0 and k<n and l>=0 and l<n:
                    p = [k,l]
                    P.append(p)
                #end if
            #end if
        #end for
    #end for
    return P
#end def

## -------------------------------------------------------------------------
##TodoVisitado: Retornar un valor booleano si el tablero está visitado o no.
##Entradas:
##	- T: Tablero actual.
##  - n: Tamaño del lado del tablero.
##Salidas:
##	- v: True si el tablero está visitado completamente o False de lo contrario.
## -------------------------------------------------------------------------
def TodoVisitado (T,n):
    v = True
    for i in range(0,n):
        for j in range(0,n):
            if T[i][j] == 0:
                v = False
            #end if
        #end for
    #end for
    return v
#end def


## -------------------------------------------------------------------------
##Caballo: Retornar un valor booleano si existe un camino que recorra todo el tablero.
##Entradas:
##	- T: Tablero actual.
##	- x: posición fila actual del caballo.
##	- y: posición columna actual del caballo.
##  - n: Tamaño del lado del tablero.
##  - S: Secuencia que contiene los saltos del caballo.
##Salidas:
##	- sol: True si el todo tablero está visitado o False de lo contrario.
## -------------------------------------------------------------------------
def Caballo(T,x,y,n,S):
    T[x][y] = 1
    P = CalcularPosiciones(x,y,n)
    sol = TodoVisitado(T,n)
    i = 0
    while sol == False and i< len(P) :
        act = P[i]
        if T[act[0]][act[1]] != 1:
            T[act[0]][act[1]] = 1
            sol = Caballo (T,act[0],act[1],n,S)
            if sol == True:
                p = [act[0]+1,act[1]+1]
                S.append(p)
            else:
                S.clear()
                T[act[0]][act[1]] = 0
            #end if
        i += 1
        #end if
    #end while
    return sol
#end def

## -------------------------------------------------------------------------
##Matrix: Crea una matriz de tamaño nxn.
##Entradas:
##  - n: Tamaño del lado del tablero.
##Salidas:
##	- M: Matriz construida y llenada de ceros.
## -------------------------------------------------------------------------
def Matrix (n):
    M =[]
    for i in range(0,n):
        M_Aux = []
        for j in range (0,n):
            M_Aux.append(0)
        #end for
        M.append(M_Aux)
    #end for
    return M
#end def

## -------------------------------------------------------------------------
##FindPath: Encuentra un camino que debe seguir la ficha del caballo para recorrer
#           todas las celdas del tablero..
##Entradas:
##  - n: Tamaño del lado del tablero.
## -------------------------------------------------------------------------
def FindPath(n):
    T = Matrix(n)
    S = []
    path = False
    i, j = 0, 0
    while path == False and i < n :
        while path == False and j < n :
            path = Caballo(T,i,j,n,S)
            j+=1
        #end while
        i+=1
    #end while
    print("Existe camino: ")
    print (path)
    print("El camino inverso es: ")
    print (S)
#end def

##PRUEBAS
# Tablero 2x2 (4 celdas)
print ("Tablero 2x2")
FindPath(2)
# Tablero 3x3 (9 celdas)
print ("Tablero 3x3")
FindPath(3)
# Tablero 5x5 (25 celdas)
print ("Tablero 5x5")
FindPath(5)

