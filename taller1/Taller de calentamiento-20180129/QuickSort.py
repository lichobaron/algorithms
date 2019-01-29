## -------------------------------------------------------------------------
## QuickSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def QuickSortPartition( S, p, r ):
    pval = S[ p ]
    lm = p + 1
    rm = r
    done = False
    while not done:
        while lm <= rm and S[ lm ] <= pval:
            lm = lm + 1
        ## end while
        while S[ rm ] >= pval and rm >= lm:
            rm = rm - 1
        ## end while
        if rm < lm:
            done = True
        else:
            aux = S[ lm ]
            S[ lm ] = S[ rm ]
            S[ rm ] = aux
        ## end if
    ## end while
    aux = S[ p ]
    S[ p ] = S[ rm ]
    S[ rm ] = aux
    return rm
## end def

## -------------------------------------------------------------------------
## QuickSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def QuickSortAux( S, p, r ):
    if p < r:
        q = QuickSortPartition( S, p, r )
        QuickSortAux( S, p, q - 1 )
        QuickSortAux( S, q + 1, r )
    ## end if
## end def

## -------------------------------------------------------------------------
## QuickSort: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
def QuickSort( S ):
    QuickSortAux( S, 0, len( S ) - 1 )
## end def

## eof - QuickSort.py
