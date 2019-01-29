#Taller Subsecuencia creciente más larga (LIS)
## -------------------------------------------------------------------------
##Solucion Programacion dinamica
## -------------------------------------------------------------------------
##LIS: Subsecuencia creciente más larga
##Entradas:
##	- S: secuencia de números
##Salidas:
##	- Output: Subsecuencia creciente más larga.
## -------------------------------------------------------------------------
def LIS(S):
    M = Table(S,S)
    for i in range(0,len(S)-1):
        for j in range(0,i+1):    
            if S[i] < S[i+1]:
                M[i][j] += 1
            M[i+1][j] = M[i][j]
            ##end if
        ##end for
    ##end for
        ##----------------Bactracking----------------##
    R = []
    j = 0
    while j != len(S)-1:
        if M[len(S)-1][j] > M[len(S)-1][j+1] :
            R.append(S[j])
        j+=1
        ##end if
    ##end while
    if S[len(S)-1] < S[j-1]:
        R.append(S[j-1])
    else:
        R.append(S[j])
    ##end if
    return R
##end def

## -------------------------------------------------------------------------
##Table: Crea una matriz llena de 1 de las dimensiones de X y Y
##Entradas:
##	- X: secuencia 1
##	- Y: secuencia 2
##Salidas:
##	- table: matriz de 1 de dimensiones X y Y
## -------------------------------------------------------------------------
def Table(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append(1)
        table.append(table_aux)
        ##end for
    ##end for
    return table
#end def

##Pruebas
S=[5,2,8,6,3,6,9,7]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)
S=[1,2,3,4,5]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)
S=[10,2,3,4]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)
S=[5,2,8,6,3,6,9,7,18,19,40]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)
S =[5,4,3,2,1]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)
S =[1,1,1,1,1]
R = LIS(S)
print("--------------------------------------------------------------------")
print("Secuencia original: ",S)
print("El tamaño de la mayor secuencia es de ",len(R))
print("La secuencia es: ",R)