#Taller distacias de edicion (ED)
## -------------------------------------------------------------------------
##Solucion Programacion dinamica
## -------------------------------------------------------------------------
##ED: Encuentra la menor edicion para convertir una cadena en otra
##Entradas:
##	- X: secuencia de caracteres 1
##	- Y: secuencia de caracteres 2
##Salidas:
##	- Output: lista de pasos para convertir la secuencia 1 en la secuencia 2
## -------------------------------------------------------------------------
def ED(X, Y):
    M = Table(X,Y)
    B = Table(X,Y)
    Output = []
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            if i == 0:
                M[i][j] = j
                B[i][j] = [0,-1]
            elif j == 0:
                M[i][j] = i
                B[i][j] = [-1,0]
            else:
                det = M[i-1][j] + 1
                ins = M[i][j-1] + 1
                chg = M[i-1][j-1] + d(X,Y,i,j)
                if det < ins and det < chg:
                    M[i][j] = det
                    B[i][j] = [-1,0]
                elif ins < det and ins < chg:
                    M[i][j] = ins
                    B[i][j] = [0,-1]
                else:
                    M[i][j] = chg
                    B[i][j] = [-1,-1]
                ##end if
            ##end if
        ##end for
    ##end for
    ##----------------Bactracking----------------##
    i , j = len(X)-1, len(Y)-1
    while i >= 0 and j >= 0:
        C = B[i][j]
        if X[i] != Y[j]:
            if C[0] == -1 and C[1] == 0:
                if i == j:
                    Output.append("Cambiar " + str(X[i]) + " por " + str(Y[j]) + " en la posicion " + str(i))
                else:
                    Output.append("Eliminar " + str(X[i]) + "en la posicion " + str(i))
                ##end if
            elif C[0] == 0 and C[1] == -1:
                if i == j:
                    Output.append("Cambiar " + str(X[i]) + " por " + str(Y[j]) + " en la posicion " + str(i))
                else:
                    Output.append("Insertar " + str(Y[j]) + " en la posicion " + str(i))
                ##end if
            elif C[0] == -1 and C[1] == -1:
                Output.append("Cambiar " + str(X[i]) + " por " + str(Y[j]) + " en la posicion " + str(i))  
            ##end if  
        i += C[0]
        j += C[1]
    ##end while
    return Output
##end def

## -------------------------------------------------------------------------
##d: Funcion para incremento del comando "Cambio"
##Entradas:
##	- X: secuencia de caracteres 1
##	- Y: secuencia de caracteres 2
##	- i: indice actual en X
##	- j: indice actual en Y
##Salidas:
##	- 0, si los caracteres son iguales
##	- 1, si los caracteres son diferentes
## -------------------------------------------------------------------------                   
def d(X, Y, i, j):
    if X[i] == Y[j]:
        return 0
    else:
        return 1
    ##end if
##end def

## -------------------------------------------------------------------------
##Table: Crea una matriz llena de 0 de las dimensiones de X y Y
##Entradas:
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- table: matriz de 0 de dimensiones X y Y
## -------------------------------------------------------------------------
def Table(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append(0)
        ##end for
        table.append(table_aux)
    ##end for
    return table
##end def

## -------------------------------------------------------------------------
##printOutput: imprime con formato la salida de ED
##Entradas:
##	- L: lista con los pasos de la solucion
##Salidas:
##	- ninguna
## -------------------------------------------------------------------------
def printOutput(L):
    print("--------------------------------------")
    for i in range(0,len(L)):
        print(i+1,".",L[i])
    ##end for
    print("--------------------------------------")
##end def

##Pruebas
print("--------------------------------------")
X = "tigre"
Y = "trigo"
print("Convertir", X, " a ", Y)
printOutput(ED(X, Y))

X = "comunismo"
Y = "petro"
print("Convertir", X, " a ", Y)
printOutput(ED(X, Y))

X = "petro"
Y = "comunismo"
print("Convertir", X, " a ", Y)
printOutput(ED(X, Y))

X = "sunday"
Y = "saturday"
print("Convertir", X, " a ", Y)
printOutput(ED(X, Y))