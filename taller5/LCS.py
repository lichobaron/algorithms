#Taller subsecuencia comun mas larga (LCS)
## -------------------------------------------------------------------------
##Solucion Programacion dinamica
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
        table.append(table_aux)
        ##end for
    ##end for
    return table
##end def

## -------------------------------------------------------------------------
##TableEnd: Crea una matriz llena de 'e' de las dimensiones de X y Y
##Entradas:
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- table: matriz de 'e' de dimensiones X y Y
## -------------------------------------------------------------------------
def TableEnd(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append("e")
        ##end for
        table.append(table_aux)
    ##end for
    return table
##end def

## -------------------------------------------------------------------------
##LCSBU: Algoritmo LCS con bottom-up
##Entradas:
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- Se guardan los datos correspondientes en la tabla M (tamaños) y B (direcciones)
## -------------------------------------------------------------------------
def LCSBU(X,Y):
    M = Table(X,Y)
    B = TableEnd(X,Y)
    LCSBU_Aux(B,M,len(X),len(Y),X,Y)
    c = LCSBT(B,M,len(X)-1,len(Y)-1,X,Y)
    print(c[::-1])
##end def

## -------------------------------------------------------------------------
##LCSBU_Aux: Algoritmo auxiliar LCS con bottom-up
##Entradas:
##	- B: tabla para almacenar las direcciones
##	- M: tabla para almacenar los tamaños
##	- m: tamaño de la secuencia X
##	- n: tamaño de la secuencia Y
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- Se guardan los datos correspondientes en la tabla M (tamaños) y B (direcciones)
##	- Ultimo valor de la tabla de tamaños
## -------------------------------------------------------------------------
def LCSBU_Aux(B,M,m,n,X,Y):
    for i in range(1,m):
        for j in range(1,n):
            if X[i] == Y[j]:
                M[i][j] =  M[i-1][j-1] + 1
                B[i][j] = "d"
            else:
                s1 = M[i][j-1]
                s2 = M[i-1][j]
                if s1 > s2:
                    M[i][j] = s1
                    B[i][j] = "l"
                else:
                    M[i][j] = s2
                    B[i][j] = "u"
                ##end if
            ##end if
        ##end for
    ##end for          
    return M[m-1][n-1]
##end def

## -------------------------------------------------------------------------
##LCSBT: Algoritmo de backtracking para encontrar la respuesta de LCS
##Entradas:
##	- B: tabla con las direcciones
##	- M: tabla con los tamaños
##	- i: ultima posicion de la secuencia X
##	- j: ultima posicion de la secuencia Y
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- cad: cadena comun mas larga
## -------------------------------------------------------------------------
def LCSBT(B,M,i,j,X,Y):
    cad = ""
    while B[i][j] != "e":
        if B[i][j] == "u":
            if X[i] == Y[j]:
                cad = cad + X[i]
            ##end if
            i -= 1 
        elif B[i][j] == "l":
            if X[i] == Y[j]:
                cad = cad + Y[j]
            ##end if
            j -= 1     
        elif B[i][j] == "d":
            if X[i] == Y[j]:
                cad = cad + X[i]
            ##end if
            i -= 1
            j -= 1
        ##end if
    ##end while
    cad = cad + X[j]
    return cad
##end def

## -------------------------------------------------------------------------
##Pruebas
## -------------------------------------------------------------------------
X = ['A','B','C','B','D','A','B']
Y = ['B','D','C','A','B','A']
print("Prueba 1", end=": ")
LCSBU(X,Y)

X = ['G','A','T','A','C','A','C','A','C','A','C','C','G','G','G','T','T','T','A','T','G','A','G','G','G']
Y = ['G','A','T','T','T','A','C','C','C','A']
print("Prueba 2", end=": ")
LCSBU(X,Y)
