##Solucion de fuerza bruta
##palindroma: crea una cadena, con una posible palabra resultado y si es palin-
##droma realiza la comparación para saber si es la más larga
##Entradas:
##	- word: Cadena de caracteres
##Salidas:
##	- Arreglo con las posiciones de inicio y fin de la subcadena
def palindroma (word):
    ##larga=""
    indices=[-1,-1]##Almacena los indices con la subacadena más larga encontrada
    for i in range(0,len(word)):
        for j in range(len(word)-1,-1,-1):
            if auxiliar(word[i:j+1]):
                if len(word[indices[0]:indices[1]+1]) < len(word[i:j+1]):
                    indices[0]=i
                    indices[1]=j
                ##end if
            ##end if
        ##end for
    ##end for
    return indices
##end def
##auxiliar: Determina si una palabra es palindroma
def auxiliar(word):
    cad=""
    for k in range(len(word)-1,-1,-1):
        cad=cad+word[k]
    ##end for
    if cad==word:
        return True
    ##end if
    return False
##end def

def Run(list):
    Exp = palindroma(list)
    print(list[Exp[0]:Exp[1]+1])

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
