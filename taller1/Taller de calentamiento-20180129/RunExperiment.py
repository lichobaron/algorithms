#!/usr/bin/python3

import sys, time
from CreateRandomArray import *
#from BubbleSort import *
#from InsertionSort import *
#from QuickSort import *
#from MergeSort import *

## -------------------------------------------------------------------------
def IsOrdered( S ):
    r = 1
    for i in range( len( S ) - 1 ):
        if S[ i + 1 ] < S[ i ]:
            r = 0
        ## end if
    ## end for
    return r
## end def

## -------------------------------------------------------------------------
def MeasureTime( alg, S ):
    sT = time.process_time( )
    alg( S )
    eT = time.process_time( )
    return float( eT - sT )
## end def
    
## -------------------------------------------------------------------------
## Main code
## -------------------------------------------------------------------------

## Check arguments
if len( sys.argv ) != 3:
    print( "Usage: ", sys.argv[ 0 ], "algorithm max_time" )
    exit( 1 )
## end if
algName = sys.argv[ 1 ]
m = float( sys.argv[ 2 ] )

## Load algorithm
alg = getattr( __import__( algName ), algName )

sT = time.process_time( )
d = float( 0 )
n = 0
while d < m:
    ## Update execution time
    d = float( time.process_time( ) - sT )

    ## Create an array
    S = CreateRandomArray( n )
    n = n + 100

    ## Execute algorithm
    t = MeasureTime( alg, S )
    print( len( S ), IsOrdered( S ), "%.5f"% ( t ) )
## end while

## eof - MeasureTime.py
