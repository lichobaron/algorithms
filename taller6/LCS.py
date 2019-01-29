def LCS_Aux(i,j,X,Y):
        if i < 0 or j < 0:
            return 0
        elif X[i-1] == Y[j-1]:
            return LCS_Aux(i-1, j-1, X, Y) + 1
        else:
            s1 = LCS_Aux(i, j-1, X, Y)
            s2 = LCS_Aux(i-1, j, X, Y)
            if s1 > s2:
                return  s1
            else:
                return s2
##end def

def LCS(X,Y):
    return LCS_Aux(len(X)-1, len(Y)-1, X, Y)

def LCSM(X,Y):
    M = TableZero(X,Y)
    R = LCSM_Aux(M,len(X)-1,len(Y)-1,X,Y)
    PrintTable(M)
    return R

def LCSM_Aux(M,i,j,X,Y):
    if M[i][j] == 0:
        if i == 0 or j == 0:
            #M[i][j] = 0
            pass
        elif X[i] == Y[j]:
            M[i][j] = LCSM_Aux(M, i-1, j-1, X, Y) + 1
        else:
            s1 = LCSM_Aux(M, i, j-1, X, Y)
            s2 = LCSM_Aux(M, i-1, j, X, Y)
            if s1 > s2:
                M[i][j] = s1
            else:
                M[i][j] = s2
    ##end if
    return M[i][j]
##end def

def Table(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append(float("-inf"))
        table.append(table_aux)
    return table

def TableEnd(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append("e")
        table.append(table_aux)
    return table

def PrintTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            print('{:6}'.format(table[i][j]), end = '')
        print()

def LCSBU(X,Y):
    M = Table(X,Y)
    B = TableEnd(X,Y)
    R = LCSBU_Aux(B,M,len(X),len(Y),X,Y)
    PrintTable(M)
    PrintTable(B)
    c = LCSBT(B,M,len(X)-1,len(Y)-1,X,Y)
    print(c[::-1])
    #c = LCSBTR(M, X, Y, len(X)-1,len(Y)-1)
    #print(c)
    return R

def LCSBU_Aux(B,M,m,n,X,Y):
    for i in range(0,m):
        M[i][0]= 0
    for i in range(0,n):
        M[0][i]= 0
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
    return M[m-1][n-1]
##end def

def LCSBT(B,M,i,j,X,Y):
    cad = ""
    while B[i][j] != "e":
        if B[i][j] == "u":
            if X[i] == Y[j]:
                cad = cad + X[i]
            i -= 1
            
        elif B[i][j] == "l":
            if X[i] == Y[j]:
                cad = cad + Y[j]
            j -= 1
            
        elif B[i][j] == "d":
            if X[i] == Y[j]:
                cad = cad + X[i]
            i -= 1
            j -= 1
    cad = cad + Y[i]
    return cad

def LCSBTR(M, X, Y, i, j):
    if i == 0 or j == 0:
        return Y[j]
    elif  X[i] == Y[j]:
        return LCSBTR(M, X, Y, i-1, j-1) + X[i]
    else:
        if M[i][j-1] > M[i-1][j]:
            return LCSBTR(M, X, Y, i, j-1)
        else:
            return LCSBTR(M, X, Y, i-1, j)

def TableZero(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append(0)
        table.append(table_aux)
    return table

X = ['A','B','C','B','D','A','B']
Y = ['B','D','C','A','B','A']
#X = [1,0,0,1,0,1,0,1]
#Y = [0,1,0,1,1,0,1,1,0]
#X = ['G','A','T','A','C','A','C','A','C','A','C','C','G','G','G','T','T','T','A','T','G','A','G','G','G']
#Y = ['G','A','T','T','T','A','C','C','C','A']
#print(LCS(X,Y))
#print(LCSM(X,Y))
print(LCSBU(X,Y))
