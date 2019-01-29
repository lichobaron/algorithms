## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sys
if __name__ != '__main__':
    sys.exit( 1 )
# end if

import argparse, random, socket, subprocess
import Board

# Some global variables
type_PLAY = 0
type_WAIT = 1
type_END  = 2

# Guess current IP address
myIP = subprocess.check_output(
    [ 'hostname', '--all-ip-addresses' ]
    ).decode( 'ascii' ).split( ' \n' )[ 0 ]

# Some configuration from command line
parser = argparse.ArgumentParser( )
parser.add_argument( '--size', default = 8, help = 'Board size', type = int )
parser.add_argument( '--ip1', help = 'Allowed first connection' )
parser.add_argument( '--ip2', help = 'Allowed second connection' )
args = parser.parse_args( )

# Create a TCP/IP socket and bind it to the port
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
conns = [ ]
clients = [ ]
allowed_clients = [ ]
if args.ip1 != None: allowed_clients.append( args.ip1 )
if args.ip2 != None: allowed_clients.append( args.ip2 )

try:
    sock.bind( ( myIP, 0 ) )
    print( 'Starting up on {} port {}'.format( *sock.getsockname( ) ) )

    # Listen for incoming connections
    sock.listen( 1 )

    # Choose turns
    turns = [ random.randint( 0, 1 ) ]
    turns.append( ( turns[ 0 ] + 1 ) % 2 )

    # Create game
    board = Board.Board( args.size )
    board.Reset( )

    # Wait for players
    while len( conns ) < 2:
        print( 'Waiting for {} connection(s)'.format( 2 - len( conns ) ) )
        co, cl = sock.accept( )
        data = co.recv( 10 ).decode( 'ascii' )
        if data == 'pujOthello':
            conns.append( co )
            clients.append( cl[ 0 ] )
            co.setblocking( True )
            t = turns[ len( conns ) - 1 ]
            print( 'Player from {} has turn {}'.format( cl[ 0 ], t ) )
            co.sendall( t.to_bytes( 2, byteorder = 'little' ) )
        # end if
    # end while

    # Play!
    validGame = True
    while validGame:
        board.Print( )
        t, plays = board.GetTurn( )
        o = ( t + 1 ) % 2
        conns[ t ].sendall( type_PLAY.to_bytes( 2, byteorder = 'little' ) )
        conns[ o ].sendall( type_WAIT.to_bytes( 2, byteorder = 'little' ) )
        if len( plays ) > 0:
            print( "Player \"{}\", it\'s your turn".format( t ) )
            msg = plays[ 0 ][ 0 ]
            for i in range( 1, len( plays ) ):
                msg += " " + plays[ i ][ 0 ]
            # end for
            b = str( board )
            conns[ t ].sendall( len( msg ).to_bytes( 4, byteorder = 'little' ) )
            conns[ t ].sendall( bytearray( msg, 'ascii' ) )
            conns[ t ].sendall( len( b ).to_bytes( 4, byteorder = 'little' ) )
            conns[ t ].sendall( bytearray( b, 'ascii' ) )
            print( 'Waiting for player {} to play... '.format( t ), end = '' )
            c = conns[ t ].recv( 2 ).decode( 'ascii' )
            print( c )
            if board.CheckCoordinate( c ):
                r = None
                for p in plays:
                    if p[ 0 ] == c:
                        r = p
                    # end if
                # end for
                if r != None:
                    board.Play( r[ 0 ], r[ 1 ] )
                # end if
            # end if
        else:
            print( "No valid moves, changing player" )
            board.ChangePlayer( )
            t, plays = board.GetTurn( )
            if len( plays ) == 0:
                msg = board.Finish( )
                for co in conns:
                    co.sendall( type_END.to_bytes( 2, byteorder = 'little' ) )
                    co.sendall( len( msg ).to_bytes( 4, byteorder = 'little' ) )
                    co.sendall( bytearray( msg, 'ascii' ) )
                # end for
                print( msg )
                validGame = False
            # end if
        # end if
    # end while
except BaseException as error:
    print(
        "\n********\nError caught: {}.\n********\n".format( error.__doc__ )
        )
# end try

# Finish session
print( 'Closing session...', end = '' )
for c in conns:
    c.close( )
# end for
sock.close( )
print( ' done!' )

## eof - Server.py
