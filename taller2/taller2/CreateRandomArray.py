#!/usr/bin/python3

import random, sys

## -------------------------------------------------------------------------
## CreateRandomArray: creates a random integer array of size n
## @inputs: n, desired size
## @outputs: S, a random integer array
## -------------------------------------------------------------------------
def CreateRandomArray( n ):
    m = random.randint( n / 2, 2 * n )
    S = [ 0 for i in range( n ) ]
    for i in range( n ):
        S[ i ] = random.randint( 1, m )
    ## end for
    return S
## end def

## eof - CreateRandomArray.py
