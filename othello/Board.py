import math

"""Board for an othello game"""
class Board:
    BCell = 0
    WCell = 1
    ECell = 2
    VChars = [ 'O', 'X' ]

    """Creator"""
    def __init__( self, n = 8 ):
        self.m_Size = n
        self.m_Matrix = [ ]
        self.m_Turn = Board.BCell
        for i in range( self.m_Size ):
            self.m_Matrix.append( [ Board.ECell ] * self.m_Size )
        # end for
    # end def

    """Get turn and possible play positions"""
    def GetTurn( self ):
        plays = [ ]
        for i in range( self.m_Size ):
            for j in range( self.m_Size ):
                if self.m_Matrix[ i ][ j ] == Board.ECell:
                    flips = self.GetFlips( i, j )
                    if len( flips[ 1 ] ) > 0:
                        plays.append( flips )
                    # end if
                # end if
            # end for
        # end for
        return [ self.m_Turn, plays ]
    # end def

    """Configure game"""
    def Reset( self ):
        for i in range( self.m_Size ):
            for j in range( self.m_Size ):
                self.m_Matrix[ i ][ j ] = Board.ECell
            # end for
        # end for
        h = int( self.m_Size / 2 ) - 1
        self.m_Matrix[ h ][ h ] = Board.WCell
        self.m_Matrix[ h + 1 ][ h + 1 ] = Board.WCell
        self.m_Matrix[ h ][ h + 1 ] = Board.BCell
        self.m_Matrix[ h + 1 ][ h ] = Board.BCell
        self.m_Turn = Board.BCell
    # end def

    """Convert to matrix coordinates"""
    def ConvertCoordinate( self, c ):
        i = ord( c[ 0 ] ) - ord( 'a' )
        j = ord( c[ 1 ] ) - ord( '1' )
        return [ i, j ]
    # end def

    """Convert to matrix coordinates"""
    def InvertCoordinate( self, i, j ):
        return chr( ord( 'a' ) + i ) + str( j + 1 )
    # end def

    """Is valid coordinate?"""
    def IsValid( self, i, j ):
        return 0 <= i and 0 <= j and i < self.m_Size and j < self.m_Size
    # end def

    """Check"""
    def CheckCoordinate( self, c ):
        i, j = self.ConvertCoordinate( c )
        return self.IsValid( i, j )
    # end def

    """Get flips"""
    def GetFlips( self, startX, startY ):
        dirs = [
            [ 0,  1 ], [  1,  1 ], [  1, 0 ], [  1, -1 ],
            [ 0, -1 ], [ -1, -1 ], [ -1, 0 ], [ -1,  1 ]
            ]
        flips = [ ]
        if self.m_Matrix[ startX ][ startY ] == Board.ECell:
            otherTurn = ( ( self.m_Turn ) + 1 ) % 2
            for xdir, ydir in dirs:
                x, y = startX + xdir, startY + ydir
                f = [ [ x, y ] ] 
                if self.IsValid( x, y ):
                    cont = self.m_Matrix[ x ][ y ] == otherTurn
                    if cont:
                        while cont:
                            x, y = x + xdir, y + ydir
                            cont = self.IsValid( x, y )
                            if cont:
                                cont = cont and \
                                       self.m_Matrix[ x ][ y ] == otherTurn
                                if cont:
                                    f.append( [ x, y ] )
                                # end if
                            # end if
                        # end while
                        if self.IsValid( x, y ):
                            if self.m_Matrix[ x ][ y ] == self.m_Turn:
                                for flip in f:
                                    flips.append( flip )
                                # end for
                            # end if
                        # end if
                    # end if
                # end if
            # end for
        # end if
        return [ self.InvertCoordinate( startX, startY ), flips ]
    # end def

    """Play!!!"""
    def ChangePlayer( self ):
        self.m_Turn = ( self.m_Turn + 1 ) % 2
    # end def

    """Play!!!"""
    def Play( self, start, flips ):
        if len( flips ) > 0:
            sx, sy = self.ConvertCoordinate( start );
            self.m_Matrix[ sx ][ sy ] = self.m_Turn
            for f in flips:
                self.m_Matrix[ f[ 0 ] ][ f[ 1 ] ] = self.m_Turn
            # end for
            self.ChangePlayer( )
        # end if
    # end def

    """Count points"""
    def Finish( self ):
        points = [ 0, 0, 0 ]
        for i in range( self.m_Size ):
            for j in range( self.m_Size ):
                points[ self.m_Matrix[ i ][ j ] ] += 1
            # end for
        # end for
        winner = Board.ECell
        if points[ Board.BCell ] < points[ Board.WCell ]:
            winner = Board.WCell
        elif points[ Board.WCell ] < points[ Board.BCell ]:
            winner = Board.BCell
        # end if
        if winner == 2:
            return "Game was a tie."
        else:
            return "Player \"{}\" won {} to {}".format( Board.VChars[ winner ], points[ winner ], points[ ( winner + 1 ) % 2 ]  )
    # end def

    """Print into screen"""
    def Print( self ):
        hline = '  +'
        vline = '  |'
        r = '    a'
        a = ord( 'a' )
        for i in range( self.m_Size ):
            hline += '---+'
            vline += '   |'
            if i < self.m_Size - 1:
                r += '   ' + chr( a + i + 1 )
            # end if
        # end for
        r += '\n' + hline
        for y in range( self.m_Size ):
            r += '\n' + str( y + 1 ) + ' '
            for x in range( self.m_Size ):
                c = ' '
                if self.m_Matrix[ x ][ y ] != Board.ECell:
                    c = Board.VChars[ self.m_Matrix[ x ][ y ] ]
                # end if
                r += "| " + c + ' '
            # end for
            r += '|\n' + hline
        # end for
        print( r )
     # end def

    """Serialization"""
    def __str__( self ):
        r = ""
        for y in range( self.m_Size ):
            for x in range( self.m_Size ):
                r += str( self.m_Matrix[ x ][ y ] )
            # end for
        # end for
        return r
    # end def
# end class

## eof - Board.py
