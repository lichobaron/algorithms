import math

## -------------------------------------------------------------------------
## Merge: Merge two subsequences of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          q, pivot between both subsequences
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def Merge( S, p, q, r ):
    n1 = q - p + 1
    n2 = r - q
    L = [ math.inf for i in range( n1 + 1 ) ]
    R = [ math.inf for j in range( n2 + 1 ) ]
    for i in range( n1 ):
        L[ i ] = S[ p + i ]
    ## end for
    for j in range( n2 ):
        R[ j ] = S[ q + j + 1 ]
    ## end for
    i = 0
    j = 0
    for k in range( p, r + 1 ):
        if L[ i ] < R[ j ]:
            S[ k ] = L[ i ]
            i = i + 1
        else:
            S[ k ] = R[ j ]
            j = j + 1
        ## end if
    ## end for
## end def

## -------------------------------------------------------------------------
## MergeSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def MergeSortAux( S, p, r ):
    if p < r:
        q = int( ( p + r ) / 2 )
        MergeSortAux( S, p, q )
        MergeSortAux( S, q + 1, r )
        Merge( S, p, q, r )
    ## end if
## end def

## -------------------------------------------------------------------------
## MergeSort: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
def MergeSort( S ):
    MergeSortAux( S, 0, len( S ) - 1 )
## end def

## eof - MergeSort.py
