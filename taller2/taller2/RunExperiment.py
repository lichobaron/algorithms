#!/usr/bin/python3

import sys, time
from CreateRandomArray import *
from Solucion2 import *
from Solucion1 import *

## -------------------------------------------------------------------------
def WriteFile(algName, S, Outs):
    file = open(algName + ".res", "a")
    file.write(str(len( S )) +  str(" %.5f"% ( Outs[0] )) + " " + str(Output( Outs[1] )) + "\n")
    file.close()

## -------------------------------------------------------------------------
def Output( R ):
    return ("G: %d C: %d V: %d" %(R[2], R[0], R[1]) )
## end def

## -------------------------------------------------------------------------
def MeasureTime( alg, S ):
    X = []
    sT = time.process_time( )
    R = alg( S )
    eT = time.process_time( )
    X.append(float( eT - sT ))
    X.append(R)
    return X
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
    Outs = MeasureTime( alg, S )

    ##Write Output
    WriteFile(algName,S,Outs)
## end while

## eof - MeasureTime.py
