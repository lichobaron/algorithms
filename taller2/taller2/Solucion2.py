##Solucion Dividir y Vencer
##Por medio de las deriavadas discretas determinar el mayor subarreglo

import math

## -------------------------------------------------------------------------
##Derivates: Calcula las derivadas discretas
##Entradas: 
##	- A: Arreglo para calcular las derivadas
##Salidas:
##	- retorno: Arreglo de las derivadas 
## -------------------------------------------------------------------------
def Derivates(A):
    retorno = []
    for i in range(1, len(A)-1):
        retorno.append(A[i]-A[i-1])
    ##end for
    return retorno
##end def

## -------------------------------------------------------------------------
##FindMaxCrossSubArray: encuentra el maximo subarreglo intermedio
##Entradas: 
##	- A: Arreglo de las derivadas discretas
##	- l: inidice posicion menor
##	- h: indice posicion mayor
##	- m: indice mitad
##Salidas:
##	- vl+vr: Suma del maximo subarreglo
##	- ml: indice izquierdo maximo subarreglo
##	- lr: indice derecho maximo subarreglo
## -------------------------------------------------------------------------
def FindMaxCrossSubArray(A, l, m, h):
    retorno = []
    vl = -math.inf #variable mayor suma por la izquierda
    s = 0 ##variable suma deriavadas
    ml=   -1 ##indice izquierdo
    for i in range(m,l-1,-1):
        s= s+ A[i]
        if s > vl: ##Evaluacion suma mayor
            vl = s
            ml = i
	#end if
    ##end for
    vr = -math.inf #variable mayor suma por la derecha
    s = 0
    mr =  -1 ##indice derecho
    for i in range(m+1,h+1):
        s= s+ A[i]
        if s > vr: ##Evaluacion suma mayor
            vr = s
            mr = i+1
	##end if
    ##end for
    retorno.append(vl+vr)
    retorno.append(ml)
    retorno.append(mr)
    return retorno
##end def

##FindMaxSubArray: encuentra el maximo subarreglo
##Entradas: 
##	- A: Arreglo de las derivadas discretas
##	- l: inidice posicion menor
##	- h: indice posicion mayor
##Salidas:
## Cada subarreglo cuenta con la suma de sus elementos, su inicio y su fin
##	- X: subarreglo caso base
##	- L: maximo subarreglo izquierdo 
##	- R: maximo subarreglo derecho 
##	- C: maximo subarreglo intermedio 
## -------------------------------------------------------------------------
def FindMaxSubArray(A,l,h):
    X, L, R, C = [], [], [], []
    if h <= l: #Caso base
        if len(A) >0:
            X.append(A[l])
            X.append(l)
            X.append(h)
        else:
            X.append(-1)
            X.append(-1)
            X.append(-1)
        del(L)
        del(R)
        del(C)
        return X
	##end if
    ##end if
    else:
        m = int((l+h)/2) ##Particion del arreglo, dividir
	##Llamados recurrentes
        L = FindMaxSubArray(A,l,m) ##izquierda
        R = FindMaxSubArray(A,m+1,h) ##derecha
	##Funcion para arreglo intermedio
        C = FindMaxCrossSubArray(A, l, m, h)
        if L[0] >= R[0] and L[0] >= C[0]:
            del(X)
            del(R)
            del(C)
            return L
	##end if
        elif R[0] >= L[0] and R[0] >= C[0]:
            del(X)
            del(L)
            del(C)
            return R
	##end elif
        else:
            del(X)
            del(L)
            del(R)
            return C
	#end else
##end def

##Solucion2: solucion dividir y vencer
##Entradas: 
##	- A: Arreglo de precios por dia
##Salidas:
##	- inicio del subarreglo
##	- fin del arreglo
##	- suma del subarreglo
## -------------------------------------------------------------------------
def Solucion2(A):
    der = Derivates(A)
    return FindMaxSubArray(der,0, len(der)-1)
##end def
