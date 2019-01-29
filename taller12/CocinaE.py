from random import *
from time import time

## -------------------------------------------------------------------------
##Potencia: Retorna todas las combinaciones posibles dada una lista de elementos.
##Entradas:
##  - L: Lista de elementos que se quieren combinar.
##Salidas:
##	- R: Lista de elementos con las combinaciones.
## -------------------------------------------------------------------------
def Potencia(L):
    if len(L) == 0:
        return [[]]
    R = Potencia(L[:-1])
    r = len(R)
    for i in range(0, r):
        S = []
        S = R[i][0:len(R[i])]
        S.append(L[-1])
        R.append(S)
    return R

## -------------------------------------------------------------------------
##Recipe: Encuentra una receta que cumpla con la condición.
##Entradas:
##  - T: Matriz de discordancia.
##  - p: Discordancia máxima permitida.
##  - n: Cantidad de ingredientes.
##Salidas:
##	- S: Combinación de ingredientes que cumple con la condición.
## -------------------------------------------------------------------------
def Recipe(T, p, n):
    D = []
    for i in range(0, n):
        for j in range(i+1, n):
            D.append([i, j])
        # end for
    # end for
    P = Potencia(D)
    P.pop(0)
    i = 0
    while i < len(P):
        c = P[i]
        e = False
        for j in range(0, len(c)):
            f1 = c[j][0]
            c1 = c[j][1]
            for k in range(j+1, len(c)):
                if f1 == c[k][0] or c1 == c[k][1] or f1 == c[k][1] or c1 == c[k][0]:
                    e = True
                #end if
            #end for
        #end for
        if e:
            P.remove(c)
            i = 0
        else:
            i += 1
        #end if
    #end while
    max = float("-inf")
    min = float("inf")
    S = []
    suma = 0
    for i in range(0, len(P)):
        c = P[i]
        x = 0
        for j in range(0, len(c)):
            x += T[c[j][0]][c[j][1]]
        # end for
        if x <= p and len(c) >= max:
            if x <= min:
                min = x
                suma = x
            max = len(c)
            S = c
        # end if
    # end for
    print("Suma: ", suma)
    return S
# end def
## -------------------------------------------------------------------------
##Matrix: Crea una matriz de tamaño nxn.
##Entradas:
##  - n: Cantidad de ingredientes.
##Salidas:
##	- M: Matriz construida y llenada de ceros.
## -------------------------------------------------------------------------
def Matrix (n):
    M =[]
    for i in range(0,n):
        M_Aux = []
        for j in range (0,n):
            M_Aux.append(0.0)
        #end for
        M.append(M_Aux)
    #end for
    return M
#end def

## -------------------------------------------------------------------------
##FillMatrix: Llena una matriz de tamaño nxn 
##Entradas:
##  - M: Matriz que se llenará.
##  - n: Cantidad de ingredientes.
## -------------------------------------------------------------------------
def FillMatrix (M,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if i != j:
                M[i][j] = round(uniform(0, 1),1)
                M[j][i] = M[i][j]
            #end if
        #end for
    #end for
#end def

## -------------------------------------------------------------------------
##RecipeE: algoritmo heuristico para encontrar 
##Entradas:
##  - T: Matriz de discordancia.
##  - p: Discordancia máxima permitida.
##  - n: Cantidad de ingredientes.
##Salidas:
##	- R: Combinación de ingredientes que cumple con la condición.
## -------------------------------------------------------------------------
def RecipeE(T,p,n):
    U = InitIng(n)
    R = []
    pAcum = 0
    while pAcum <= p:
        minD = float('inf')
        coorMin = [0,0]
        i = 0
        while i < n:
            #print("i: ",i)
            j = i
            while j < n:
                #print("  j: ",j)
                if U[i] != 1 and U[j] != 1:
                    if i != j and T[i][j] < minD:
                        minD = T[i][j]
                        coorMin[0], coorMin[1] = i , j
                    ##end if
                ##end if
                j += 1
            ##end while
            i += 1
        ##end while
        pAcum += minD
        U[coorMin[0]] , U[coorMin[1]] = 1 , 1
        R.append(coorMin)
    #end while
    R.pop()
    suma = 0
    for i in range(0,len(R)):
        coor = R[i]
        suma += T[coor[0]][coor[1]]
    ##end for
    print("Suma: ", suma)
    return R

##end def

## -------------------------------------------------------------------------
##InitIng: inicializa la lista auxiliar de ingredientes usados
##Entradas:
##  - n: Cantidad de ingredientes.
##Salidas:
##	- U: lista que indica que ingrredientes estan usados
## -------------------------------------------------------------------------
def InitIng(n):
    U = []
    for i in range(0,n):
        U.append(0)
    ##end for
    return U 
##end def

## -------------------------------------------------------------------------
##RunTest: Codigo que ejecuta 10 pruebas con T y p aletorios
## -------------------------------------------------------------------------
def RunTest():
    for i in range(0,10): 
        print("--------------------Prueba ", i+1,"--------------------")      
        n = randint(5, 6)
        d = uniform(0.5, 1)
        round(n,1)
        M = Matrix(n)
        FillMatrix(M,n)
        print("----Algoritmo Combinatorio----")
        start_time = time()
        print("Resultado: ", Recipe(M, d, n))
        elapsed_time = time() - start_time
        print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
        print("----Algoritmo Euristico-------")
        start_time = time()
        print("Resultado: ", RecipeE(M, d, n))
        elapsed_time = time() - start_time
        print("Tiempo transcurrido: %0.10f seconds." % elapsed_time)
        print("--------------------------------------------------")
    ##end for
##end def

RunTest()