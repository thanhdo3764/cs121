class Connect4():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = []
        
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]
        
    def __repr__(self):
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|' # add the separator character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        #print out the horizontal separator
        for i in range(2 * self.width + 1):
            s += '-'
        s += '\n'
        # print out indices of each column
        for i in range(self.width):
            s += ' ' + str(i % 10)
        return s # return string
    
    def addMove(self, col, ox):
        #starting from the bottom of the board for col
        for row in range(1, self.height+1): 
            #if the space is empty
            if self.data[-1 * row][col] == ' ':
                #replace the space with ox
                self.data[-1 * row][col] = ox
                break

    def clear(self):
        #replaces each position with ' '
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '
    
    def delMove(self, col):
        for row in range(self.height):
            #if upper most row in col is not empty,
            if self.data[row][col] != ' ':
                #replace checker with ' '
                self.data[row][col] = ' '
                break
    
    def allowsMove(self, col):
        #allow move if col is in the board and row 0 of that column is empty
        if col in range(self.width) and self.data[0][col] == ' ':
            return True
        else:
            return False
    
    def isFull(self):
        
        counter = 0
        for i in range(self.width):
            counter += self.allowsMove(i)
        if counter == 0: #if allowsMove() for all columns return False
            return True 
        else:
            return False

    def winsFor(self,ox):
        #checks horizontal
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row][col+1] == ox and \
                   self.data[row][col+2] == ox and \
                   self.data[row][col+3] == ox:
                    return True
        
        #checks vertical
        for row in range(self.height-3):
            for col in range(self.width ):
                if self.data[row][col] == ox and \
                   self.data[row+1][col] == ox and \
                   self.data[row+2][col] == ox and \
                   self.data[row+3][col] == ox:
                    return True

        #checks NE to SW
        for row in range(self.height-3):
            for col in range(3, self.width):
                if self.data[row][col] == ox and \
                    self.data[row+1][col-1] == ox and \
                    self.data[row+2][col-2] == ox and \
                    self.data[row+3][col-3] == ox:
                    return True

        #checks NW to SE
        for row in range(self.height-3):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True

        return False
    
    def hostGame(self):
        player = '' #keeps track of player turn
        print(' _____ _____ __  __ __  __ _____ _____ ______   __ __')
        print(' | __| | _ | | \\ || | \\ || | __| | __| |_  _|   ||_||')
        print(' ||    || || |  \\|| |  \\|| ||__  ||      ||     |__ |' )
        print(' ||__  ||_|| ||\\  | ||\\  | ||__  ||__    ||        ||')
        print(' |___| |___| || \\_| || \\_| |___| |___|   ||        ||\n')
        print('Starting game . . .\n')
        #for each turn on the board
        for turn in range(self.width * self.height):
            print(self)
            if turn % 2 == 0: #player X if turn is even
                player = 'X'
            else: #player O if turn is odd
                player = 'O'
            print('Player ', player, ' turn')
            colNum = int(input('Choose a column. . . '))
            #while input for colNum is invalid
            while self.allowsMove(colNum) == False:
                #keep asking for colNum
                colNum = int(input('Invalid Column.\n Choose a column. . . '))
            #add player checker to colNum
            self.addMove(colNum, player)
            #if the player just won
            if self.winsFor(player):
                print(self)
                print('Player ', player, ' wins!')
                break
            #if no winners and board is full
            elif self.isFull():
                print(self)
                print('Full board. Tie game.')
                
def main():
    b = Connect4(7,6)
    b.hostGame()

if __name__ == '__main__':
    main()
