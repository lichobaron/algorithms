def ED(X, Y):
    return ED_Aux(X, Y, len(X)-1, len(Y)-1)

def ED_Aux(X,Y,i,j):
    if i == -1:
        return j
    elif j == -1:
        return i
    else:
        det = ED_Aux(X, Y, i-1, j) +1
        ins = ED_Aux(X, Y, i, j-1) +1
        chg = ED_Aux(X, Y, i-1, j-1) + d(X,Y,i,j)
        if det < ins and det < chg:
            return det
        elif ins < det and ins < chg:
            return ins
        else:
            return chg
                          
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

X = "tigre"
Y = "trigo"
print(ED(X, Y))