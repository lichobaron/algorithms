def ED(X, Y):
    M = Table(X,Y)
    R = ED_Aux(M, X, Y, len(X)-1, len(Y)-1)
    PrintTable(M)
    return R

def ED_Aux(M, X, Y, i, j):
    if M[i][j] == 0:
        if i == -1:
            M[0][j] = j
        elif j == -1:
            M[i][0] = i
        else:
            det = ED_Aux(M, X, Y, i-1, j) +1
            ins = ED_Aux(M, X, Y, i, j-1) +1
            chg = ED_Aux(M, X, Y, i-1, j-1) + d(X,Y,i,j)
            if det < ins and det < chg:
                M[i][j] = det
            elif ins < det and ins < chg:
                M[i][j] = ins
            else:
                M[i][j] = chg
    return M[i][j]
                   
def d(X, Y, i, j):
    if X[i] == Y[i]:
        return 0
    else:
        return 1

def Table(X,Y):
    table = []
    for i in range(0, len(X)):
        table_aux = []
        for j in range(0, len(Y)):
            table_aux.append(0)
        table.append(table_aux)
    return table

def PrintTable(table):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            print('{:6}'.format(table[i][j]), end = '')
        print()

X = "tigre"
Y = "trigo"
print(ED(X, Y))