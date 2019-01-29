## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys
if __name__ != '__main__':
    sys.exit( 1 )
# end if

import argparse, random, socket
import ProPlayer

## -------------------------------------------------------------------------
def PlayOthello( options, board, myTurn ):
  opts = options.split( ' ' )
  print("Your options are: ", opts)
  print("My turn: ", myTurn)
  return ProPlayer.simulatePlay(board, int(myTurn))
# end def

## -------------------------------------------------------------------------
# Some global variables
type_PLAY = 0
type_WAIT = 1
type_END  = 2

# Some configuration from command line
parser = argparse.ArgumentParser( )
parser.add_argument( '--host', help = 'host address' )
parser.add_argument( '--port', help = 'port in host' )
args = parser.parse_args( )
print( args.host, args.port )

# Create a TCP/IP socket and bind it to the port
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
try:
    # Ok, start
    print( 'Connecting to {}'.format( args.host ) )
    sock.connect( ( args.host, int( args.port ) ) )

    # Handshake
    sock.sendall( bytearray( 'pujOthello', 'ascii' ) )

    # Get turn
    myTurn = int.from_bytes( sock.recv( 2 ), byteorder = 'little' )
    print( 'Your turn is {}'.format( myTurn ) )

    # Play!
    validGame = True
    while validGame:
        play = int.from_bytes( sock.recv( 2 ), byteorder = 'little' )
        if play == type_PLAY:
            msg_size = int.from_bytes( sock.recv( 4 ), byteorder = 'little' )
            msg = sock.recv( msg_size ).decode( 'ascii' )
            b_size = int.from_bytes( sock.recv( 4 ), byteorder = 'little' )
            b = sock.recv( b_size ).decode( 'ascii' )
            c = PlayOthello( msg, b, myTurn )
            print( "I send {}".format( c ) )
            sock.sendall( bytearray( c, 'ascii' ) )
        elif play == type_END:
            msg_size = int.from_bytes( sock.recv( 4 ), byteorder = 'little' )
            msg = sock.recv( msg_size ).decode( 'ascii' )
            print( msg )
            validGame = False
        elif play == type_WAIT:
            print( "I wait" )
        # end if
    # end while
except:
    print( "Error caught: {}".format( sys.exc_info( )[ 0 ] ) )
# end try

# Finish session
print( 'Closing session...', end = '' )
sock.close( )
print( ' done!' )

## eof - RandomPlayer.py
