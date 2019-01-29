##Solucion Dividir y Vencer
##Encontrar maxima subpalindroma diviendo el arreglo

#Variable para guardar los indices de la maxima palindroma encontrada
maxp = [0,0]

## -------------------------------------------------------------------------
##IsPalindrome: Evalua si una secuencia es palidroma
##Entradas:
##	- A: secuencia
##  - l:indice de inicio
##  - indice de fin
##Salidas:
##	- x: True si es palindroma, False si no
## -------------------------------------------------------------------------
def IsPalindrome(A, l, h):
    x= True
    aux = 0
    for i in range(l,h):
        if A[i] != A[h-aux]:
            x= False
        ##end if
        aux= aux +1
    ##end for
    return x
##end def

## -------------------------------------------------------------------------
##compSubPalindrome: Evalua cual subpalindroma es mayor
##Entradas:
##	- A: indices subsecuencia 1
##  - B: indices subsecuencia 2
##  - C: indices subsecuencia 3
##Salidas:
##	- A,B,C: subsecuencia mayor
## -------------------------------------------------------------------------
def compSubPalindrome(A,B,C):
    if A[1]-A[0] >= B[1]-B[0] and A[1]-A[0] >= C[1]-C[0]:
        return A
    ##end if
    elif B[1]-B[0] >= A[1]-A[0] and B[1]-B[0] >= C[1]-C[0]:
        return B
    ##end elif
    else:
        return C
    ##end else
##end def

## -------------------------------------------------------------------------
##FindMaxCrossPalindromeAux: encuentra una subpalindroma intermedia
##Entradas:
##	- i: indice izquierdo
##  - j: indice derecho
##  - r: indices encontrados anteriormente
##  - A: secuencia mayor
##Salidas:
##	- retorno: indices de subpalindroma maxima
## -------------------------------------------------------------------------
def FindMaxCrossPalindromeAux(i,j,r,A):
    retorno = r
    cond = True
    while i >= 0 and j <= len(A)-1 and cond:
        if A[i] == A[j]:
            retorno.clear()
            retorno.append(i)
            retorno.append(j)
        ##end if
        else:
            cond = False
        ##end else
        i = i-1
        j = j+1
    ##end while
    return retorno
##end def

## -------------------------------------------------------------------------
##FindMaxCrossPalindrome: encuentra una subpalindroma intermedia dado un caso
##Entradas:
##	- l: indice inicio
##  - m: indice intermedio
##  - h: indice fin
##  - A: secuencia mayor
##Salidas:
##	- F: indices de subpalindroma maxima
## -------------------------------------------------------------------------
def FindMaxCrossPalindrome(A, l, m, h):
    #print(l,m,h)
    B,C,D = [0,0],[0,0],[0,0]
    if m-1 >= 0 and A[m-1] == A[m+1]:##Caso 1: palindroma alrededor del pivote
        B.clear()
        B.append(m-1)
        B.append(m+1)
        B = FindMaxCrossPalindromeAux(m-2,m+2,B,A)
    ##end if
    if A[m] == A[m+1]:## Caso 2: palidroma alrededor del pivote y este +1
        C.clear()
        C.append(m)
        C.append(m+1)
        C = FindMaxCrossPalindromeAux(m-1,m+2,C,A)
    ##end if
    if m-1 >= 0 and A[m-1] == A[m]:## Caso 3: palidroma alrededor del pivote y este -1
        D.clear()
        D.append(m-1)
        D.append(m)
        D = FindMaxCrossPalindromeAux(m-2,m+1,D,A)
    ##end if
    F = compSubPalindrome(B,C,D)
    return F
##end def

## -------------------------------------------------------------------------
##FindMaxPalindrome: encuentra la subpalindroma maxima en una secuencia
##Entradas:
##	- l: indice inicio secuencia
##  - h: indice fin secuencia
##  - A: secuencia
##Salidas:
##	- retorno: indices de subpalindroma en la recurrencia dada
## -------------------------------------------------------------------------
def FindMaxPalindrome(A,l,h):
    if h <= l:##Caso base
        X = []
        X.append(l)
        X.append(h)
        return X
    ##end if
    else:
        L , R , C = [] , [] , []
        m = int((l+h)/2)
        L = FindMaxPalindrome(A,l,m)
        R = FindMaxPalindrome(A,m+1,h)
        C = FindMaxCrossPalindrome(A,l,m,h)
        LP = IsPalindrome(A, l, m)
        RP = IsPalindrome(A, m+1, h)
        FINAL = []
        if RP:
            R.clear()
            R.append(m+1)
            R.append(h)
        ##end if
        if LP:
            L.clear()
            L.append(l)
            L.append(m)
        ##end if
        FINAL = compSubPalindrome(L,R,C)

        if FINAL[1] - FINAL[0] > maxp[1] - maxp[0]:
            maxp.clear()
            maxp.append(FINAL[0])
            maxp.append(FINAL[1])
        ##end if
        return FINAL
    ##end else
##end def

def Run(list):
    maxp.clear()
    maxp.append(0)
    maxp.append(0)
    Exp = FindMaxPalindrome(list, 0 , len(list)-1)
    print(list[maxp[0]:maxp[1]+1])

def Pruebas():
    listT= "aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaa"
    listI= "aabbccbbaazldjtrhfiodktl69golfdgjldfkjz"
    listD= "zdfikfdolñsagvstwbocv6wsvgsyzaabbccbbaa"
    listM= "zfhskoñhydfjgemiixaabbccbbaaghsdhvtfnjds"
    list100= "dguyievbxgabjtgxetswdrjrgayanhesvscyrwaaaaaaaaaaqxnrdyujayiniuxdirbtvrjqlgamfrmtjjbsymkhlorqjruswfxvnlik"
    list500= "popjqftbujbgetxerkvslafplujtkuymecvxhfviytkhuqhoenahemmgaehphfpwmtkstreuwamqidftxhyukdgcjvaeystytjdyfbvyrqzlrvoionnqrdepwopjfgslypuazmanuouwyqmdneagmdtjfimjtqtwzoqicswrbzjujbsvfapootxwqzcgejjzifocrzfprabntvqgkpdzyhbmlxuytykxodptogqarjivismudsvymfxvodgfnxjjsszqtcoygknpjqgyxkqbplxfenzyjfppubelpnymkhpydobzvxbcjjgsqcltwslmgxoydllbcqgypetrsjojrnvpmztmsuqnapligvrxewapdvwuhcmguwjlxmcfhwdovfhrffffffffffffffffffuwuhcrwrqoxqihcntcogkfzvpyukdckwyryqjkpbrxauscuiapumawaeuwmypwjpuhqxiochwybykpgwytgzszcaxhpwjudeljltwbgvrwdxqp"
    list1000= "jsdefbzmoduxxjljcwyfwdugcyfmhkrmknjxrkebriskrlkltrarzcuwcasaxepxziysqisaqhvxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxjrfyxtyceclsjmgpccvrztnwcinsdoewhfwrarkdstvrmbdsfpyuzxflndrwpcqngymjblqqalidftjepiguorucsieectwfhhvxjqypqhjpvwnvudduaribxzvlbmseeqtspqjbzsjcdajdapudgonrvahlxhphixjcgxlrjnzribmaceizuqpeavpueqbvwmmvgforpqlgghcxklonmodtnawmoaodxaeifflcxfzhcrottwxirgmkhonwzlaqwdibofrumyvxokddampqtqvqbcyzfuxrvefcivcyaqqxzlgrsuvovpznmbfagirwbvbzlqggxsxzqohslakjcsfbmwbjxdhmpvylsmadpjfhqfukrwygjayvcagtgtrxkfbbtluysjnyjwlamgnqmcwaxxfvkjqvdnceazakjrwkqqqhjfkqbfpxqaguavpjbfnlpiipnkbgxurkuproypyfnfhjqfdpfpjeokdyorbtykzepaxvsjvrdjztrokwkfiqvpavpydlesadvwwyekhzzghuuuwbvwdgyweutpazvjehibkkosxmxwwcafduiavilcoiopdzjzzzqhkhzcujpjwpohggybdyjbdpbdudirijellymhwcewshbcriizdurlezgffkqcqxbvegthzfaoolteojkprmaptchkvquktrqnrnkrmnxabngaahwppxnbueyllgdvvhuglyvqzzdokxdisrvaqjmibuyollidkyftvqjzldqatmqjysonjkzecvyoxcagjkgoeqwrjzwmcsvqudwmecgsxciixxgqcqkhpntnxdsicbqvydonkblczmkczy"
    print("Prueba toda palindroma:")
    Run(listT)
    print("Prueba palindroma Izquierda:")
    Run(listI)
    print("Prueba palindroma Derecha:")
    Run(listD)
    print("Prueba palindroma Mitad:")
    Run(listM)
    print("Prueba palindroma 100 elementos:")
    Run(list100)
    print("Prueba palindroma 500 elementos:")
    Run(list500)
    print("Prueba palindroma 1000 elementos:")
    Run(list1000)

Pruebas()
