
if __name__ == "__main__":
    import Board

    # Create board
    b = Board.Board( 8 )
    b.Reset( )

    validGame = True
    while validGame:
        print( b )
        t, plays = b.GetTurn( )
        if len( plays ) > 0:
            print( "Player \"{}\", it\'s your turn".format( t ) )
            msg = plays[ 0 ][ 0 ]
            for i in range( 1, len( plays ) ):
                msg += ", " + plays[ i ][ 0 ]
            # end for
            c = input( "Choose a play ({}): ".format( msg ) )
            while not b.CheckCoordinate( c ):
                c = input( "Really, choose a VALID play ({}): ".format( msg ) )
            # end while
            r = None
            for p in plays:
                if p[ 0 ] == c:
                    r = p
                # end if
            # end for
            if r != None:
                b.Play( r[ 0 ], r[ 1 ] )
            else:
                print( "Really, choose a VALID play ({})".format( msg ) )
            # end if
        else:
            print( "No valid moves, changing player" )
            b.ChangePlayer( )
            t, plays = b.GetTurn( )
            if len( plays ) == 0:
                b.Finish( )
                validGame = False
            # end if
        # end if
    # end while
# end if


## eof - LocalGame.py
