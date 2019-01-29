#Taller dar vueltas (DV)
## -------------------------------------------------------------------------
##Solucion Programacion dinamica
## -------------------------------------------------------------------------
##DV_BU: Encuentra el menor numero de monedas para dar vueltas de un valor
##Entradas:
##	- D: secuencia de denominaciones de monedas
##	- v: valor a devolver
##Salidas:
##	- R: Tupla que posee el minimo numero de monedas y una secuencia con las mismas.
## -------------------------------------------------------------------------
def DV_BU(D,v):
    M = Table(D,v)
    B = Table(D,v)
    R = []
    r = DV_BU_Aux(B,M,D,v,len(D)-1) ##Bottom-up
    s = DV_BT(B,D,v,r) ##Backtracking
    R.append(r)
    R.append(s)
    return R
##end def

## -------------------------------------------------------------------------
##DV_BU_Aux: Encuentra el menor numero de monedas para dar vueltas de un valor
##Entradas:
##	- B: tabla de backtracking
##	- M: tabla para guardar los numeros minimos de monedas
##	- D: secuencia de denominaciones de monedas
##	- v: valor a devolver
##	- n: tamaño de la secuencia de denominaciones
##Salidas:
##	- M[n][v]: numero minimo de denominaciones para un valor dado
## -------------------------------------------------------------------------
def DV_BU_Aux(B,M,D,v,n):
    for i in range(0,len(D)):
        M[i][0] = 0
    ##end for
    for i in range(0,v+1):
        M[0][i] = i
    ##end for
    for i in range(1,len(D)):
        for j in range(1,v+1):
            if D[i] == j:
                M[i][j] = 1
                B[i][j]  = D[i]
            elif D[i] < j:
                x = M[i][j-D[i]] + 1 
                y = M[i-1][j]
                if x < y:
                    M[i][j] = x
                    B[i][j]  = D[i]
                else:
                    M[i][j] = y
                ##end if
            else:
                M[i][j] = M[i-1][j]
            ##end if
        ##end for
    ##end for
    return  M[n][v]
##end def

## -------------------------------------------------------------------------
##DV_BT: Indica cuales monedas hacen parte de la solución
##Entradas:
##	- B: tabla de backtracking, posee la denominacion si es solucion, 0 de lo contrario
##	- D: secuencia de denominaciones de monedas
##	- v: valor a devolver
##	- c: tamaño de monedas a devolver
##Salidas:
##	- sol: Secuencia de las monedas que hacen parte de la solucion
## -------------------------------------------------------------------------
def DV_BT(B,D,v,c):
    sol = []
    coins = 0
    t = v
    n = len(D)-1 
    while coins < c:
        if n == 0:
            sol.append(1)
            coins+=1
            t -= B[n][t]
        elif B[n][t] == 0:
            n-=1
        else:
            sol.append(B[n][t])
            coins+=1
            t -= B[n][t]
        ##end if
    ##end while
    return sol
##end def

## -------------------------------------------------------------------------
##Table: Crea una matriz llena de 0 de las dimensiones de D el valor de v
##Entradas:
##	- D: secuencia 1
##	- v: valor
##Salidas:
##	- T: matriz de 0 de dimensiones |D| y v
## -------------------------------------------------------------------------
def Table(D,v):
    T = []
    for i in range(0, len(D)):
        T_Aux = []
        for j in range(0, v+1):
            T_Aux.append(0)
        ##end for
        T.append(T_Aux)
    ##end for
    return T
##end def

## -------------------------------------------------------------------------
##Run: funcion para ejecutar prueba
##Entradas:
##	- D: secuencia de demoninaciones
##	- v: valor para buscar vueltas
##Salidas:
##	- muestra por pantalla el tamaño de la solución y la solución
## -------------------------------------------------------------------------
def Run(D,v):
    R = DV_BU(D, v)
    print("-------------------------------------------------------------------")
    print("La solución minima para ", v, " es de tamaño ", R[0], "y es:")
    print(R[1])
    print("-------------------------------------------------------------------")
##end def

##Pruebas
D = [1, 3, 6 ,10]
Run(D,3)
Run(D,12)
Run(D,57)
Run(D,500)
Run(D,767)
