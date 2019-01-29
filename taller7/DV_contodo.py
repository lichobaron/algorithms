def DV(D,v):
    return DV_Aux(D,v,len(D)-1)

def DV_Aux(D,v,n):
    if v == 0:
        return 0
    elif n == 0:
        return DV_Aux(D,v-D[0],n) + 1
    else:
        if D[n] <= v:
            x = DV_Aux(D,v-D[n],n) + 1
            y = DV_Aux(D,v,n-1)
            if x > y:
                return y
            else:
                return x
        else:
            return DV_Aux(D,v,n-1)

def DV_Mem(D,v):
    M = Table(D,v)
    return DV_Mem_Aux(M,D,v,len(D)-1)

def DV_Mem_Aux(M,D,v,n):
    if M[n][v] == float('inf'):
        if v == 0:
            M[n][v] = 0
        elif n == 0:
            M[n][v] = DV_Mem_Aux(M,D,v-D[0],n) + 1
        else:
            if D[n] <= v:
                x = DV_Mem_Aux(M,D,v-D[n],n) + 1
                y = DV_Mem_Aux(M,D,v,n-1)
                if x > y:
                    M[n][v] = y
                else:
                    M[n][v] = x
            else:
                M[n][v] = DV_Mem_Aux(M,D,v,n-1)
    return  M[n][v]

def DV_BU(D,v):
    M = Table(D,v)
    B = Table(D,v)
    r = DV_BU_Aux(B,M,D,v,len(D)-1)
    print(DV_BT(B,D,v,r))
    return r

def DV_BU_Aux(B,M,D,v,n):
    for i in range(0,len(D)):
        M[i][0] = 0
    for i in range(0,v+1):
        M[0][i] = i
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
            else:
                M[i][j] = M[i-1][j]
    return  M[n][v]

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
    return sol

def Table(D,v):
    T = []
    for i in range(0, len(D)):
        T_Aux = []
        for j in range(0, v+1):
            T_Aux.append(0)
        T.append(T_Aux)
    return T

def PrintTable(M):
    for i in range(0, len(M)):
        M_Aux = M[i]
        for j in range(0, len(M_Aux)):
            print(M[i][j], end = " ")
        print()

D = [1, 3, 6 ,10]
v = int(input())
print(DV_BU(D, v))