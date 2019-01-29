##Solucion de fuerza bruta
##Solucion1: compara cada elemento del arreglo con los demas para encontrar mayor diferencia
##Entradas: 
##	- precios: Arreglo de precios por dia
##Salidas:
##	- indice de inicio de la mayor difrencia
##	- indice de fin de la mayor difrencia
##	- diferencia mayou
def Solucion1(precios):
    mejor = float('-inf') ##Variable para almacenar la mejor ganacia
    retorno= [-1,-1,-1]
    for i in range(0, len(precios)-1):
        for j in range(i+1, len(precios)-1): 
            dif = precios[j]-precios[i]  ##Calculo de la diferencia de precio en cada dia
            if  dif > mejor: ##Evaluar que se consiga una diferencia mejor
                mejor = dif
                retorno.clear()
                retorno.append(mejor)
                retorno.append(i)
                retorno.append(j)
	    ##end if
	##end for
    ##end for
    return retorno
##end def

