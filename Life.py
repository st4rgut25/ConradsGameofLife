"""The game of life

Any live cell with fewer than two live neighbours dies, as if caused by under-
    population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by over-
    population.
Any dead cell with exactly three live neighbours becomes a live cell, as if by
    reproduction.
"""

import copy

cellCoords = [] #this list of original cells

class setup:
    def __init__(self,size,cells):
        """input is all integers. size is height and width of gameboard,
        cells refers to the number of living cells the user designates to
        start the board game"""
        self.size = size
        self.cells = cells
    def createBoard(self):
        """input integers width and height. Output is a board of 0s"""
        a = []
        for i in range(self.size):
            a.append([])
            for j in range(self.size):
                a[i].append(0)
        return a

    def updateBoard(self):
        print('update now')
        """initial board update to begin the game"""
        original = self.createBoard()
        print('create board')
        for i in range(self.cells):
            # number of cells = number of cell coordinates
            row = int(input('what row is the living cell in?'))
            column = int(input('what column is the living cell in?'))
            original[row][column] = 1
        return original #the first gameBoard

class printBoard:
    """printing the board"""
    def __init__(self,upboard,size):
        self.upboard = upboard
        self.size = size
    def pBoard(self):
        graf = ''
        for i in range(self.size):
            graf += '\n'
            for j in range(self.size):
               graf += str(self.upboard[i][j])
        print(graf)


class checkState:
<<<<<<< HEAD
    """this class will update the neighboring cells according to Jon Conway's rules of the game of life"""
    def __init__(self, upboard, size):#updateBoard will provide the initial living cells, but this will selfupdate
        self.upboard=upboard
        self.size=size
                
    def rules(self): #cycle through array coordinates of the board and apply rules to each coordinate
        b=self.upboard
        global copyd
        neighborcells=[[i,j] for j in range(len(b[i])) for i in range(len(b))]
        #print('neighborcells are '+str(neighborcells)) #a list of board coordinates

        ###FIRST LOOP###
        for x in range(len(neighborcells)):
            totalalive=0
            ninecells=[[neighborcells[x][0]+w,neighborcells[x][1]+h] for h in range(-1,2) for w in range(-1,2)]
            z=neighborcells[x] #original coord
            
            for cell in ninecells: #counts total number of live cells for each of the neighboring cooridnates
                    xn=cell[0] #row
                    yn=cell[1] #column
                    if cell==z: #convert original coordinate points into nested array checker
                        checkifOne=copyd[xn][yn]
                        
                    if (xn in list(range(size)) and yn in list(range(size))):
                
                        if copyd[xn][yn]==1: 
                            totalalive+=1
                        
            #DONT RUN UNTIL YOU ADD UP THE TOTAL NUMBER OF CELLS

            if (checkifOne!=1):
                #print('running live or die function')
                self.liveordie(totalalive,neighborcells[x]) #pass the array of alive cells
=======
    """this class will update the neighboring cells according to
    Jon Conway's rules of the game of life"""
    def __init__(self, upboard, size):
        # updateBoard will provide the initial living cells,
        # but this will selfupdate
        self.upboard = upboard
        self.size = size

    def rules(self):
        # cycle through array coordinates of the board and
        # apply rules to each coordinate
        b = self.upboard
        global board
        neighborcells = [[i,j] for j in range(len(b[i])) for i in range(len(b))]
        #print('neighborcells are '+str(neighborcells))
        #a list of board coordinates

        ###FIRST LOOP###
        for x in range(len(neighborcells)):
            totalalive = 0
            ninecells = ([[neighborcells[x][0] + w, neighborcells[x][1] + h]
                for h in range(-1,2) for w in range(-1,2)])
            print('\nthe ninecells are '+ str(ninecells))
            z = neighborcells[x] #original coord

            for cell in ninecells:
                # counts total number of live cells for each
                # of the neighboring cooridnates
                xn = cell[0] #row
                yn = cell[1] #column
                if cell == z:
                    # convert original coordinate points
                    # into nested array checker
                    checkifOne = board[xn][yn]

                if (xn in list(range(size)) and yn in list(range(size))):

                    if board[xn][yn] == 1:
                        totalalive += 1
            print('total number of live neighboring cells for original '
                + 'coordinate ' + str(z)+ ' is ' +str(totalalive))

            #DONT RUN UNTIL YOU ADD UP THE TOTAL NUMBER OF CELLS

            if (checkifOne != 1):
                print('the original coordinate is '+str(z))
                #print('running live or die function')
                print('the cell '+ str(z) + ' has '
                    + str(totalalive) + ' live neighbors')
                self.liveordie(totalalive,neighborcells[x])
                #pass the array of alive cells
>>>>>>> origin/master

            else: #SUBTRACT ONE LIVE CELL IF
                totalalive -= 1
<<<<<<< HEAD
=======
                print('Subtracting 1 live cell from the original: the cell '
                    + str(z) + ' has ' + str(totalalive) + ' live neighbors')
>>>>>>> origin/master
                self.liveordie(totalalive,neighborcells[x])

                    #else:
<<<<<<< HEAD
                        #print('the coordinate ' + str(xn) + 'by ' + str(yn) + 'is not within the board boundaries')
=======
                        #print('the coordinate ' + str(xn) + 'by ' + str(yn)
                        #+ 'is not within the board boundaries')
        print('upboard is ' +str(self.upboard))
>>>>>>> origin/master
        return self.upboard

    def liveordie (self,alive,originalcoord):
        xo = originalcoord[0]
        yo = originalcoord[1]
        if alive > 3:
<<<<<<< HEAD
            self.upboard[xo][yo]=0 #UPDATES original board           
        elif alive < 2:
            self.upboard[xo][yo]=0
        elif (self.upboard[xo][yo]==1) and (alive ==2 or alive ==3):
            self.upboard[xo][yo]=1
            
        elif (self.upboard[xo][yo]==0) and (alive==3):
            #Why does self.upboard update the original ?
            self.upboard[xo][yo]=1
            
        
=======
            self.upboard[xo][yo] = 0 #UPDATES original board
            print('Im too crowded im dead :(')
        elif alive < 2:
            self.upboard[xo][yo] = 0
            print('Im too lonely im dead :(')
        elif (self.upboard[xo][yo] == 1) and (alive == 2 or alive == 3):
            self.upboard[xo][yo] = 1
            print('theres just enough im still alive :)')

        elif (self.upboard[xo][yo] == 0) and (alive == 3):
            #Why does self.upboard update the original ?
            self.upboard[xo][yo] = 1
            print('perfect number of neighbors im alive :)')
            print('does origboard equal upboard?: '
                + str(self.upboard == board))

>>>>>>> origin/master




### GETTING STARTED###
<<<<<<< HEAD

        
size=int(input('What is the size of your gameboard?'))
cells=int(input('How many living cells do you want to start with?'))
=======
>>>>>>> origin/master

size = int(input('What is the size of your gameboard?'))
cells = int(input('How many living cells do you want to start with?'))

newgame = setup(size,cells)

print('OK here is your initial setup')

print('first  gameboard')
<<<<<<< HEAD
firstgame=newgame.updateBoard()#first  gameboard
copyd=copy.deepcopy(firstgame)

=======
firstgame = newgame.updateBoard()#first  gameboard

board = firstgame #initially set board to firstgame value
>>>>>>> origin/master

#Print Board
print('this is out what the board looks like in the beginning')
startGame = printBoard(firstgame, size)
#this is out what the board looks like in the beginning


print('print the board () refers to the instance we just created ')
startGame.pBoard() #print the board () refers to the instance we just created


repeat = int(input('enter the number of times you would like this to repeat'))

<<<<<<< HEAD
x=checkState(firstgame, size) #new object with the updated ORIGINAL board

=======
x = checkState(firstgame, size)
print('checkstate is the original value of x: ' + str(x))
>>>>>>> origin/master

###MAIN LOOP###

for i in range(repeat):

    print('i is ' + str(i))
<<<<<<< HEAD
    newboard=x.rules() #returns a NEW board
    x=checkState(newboard, size) #saves the state of NEW board for the next iteration

    copyd=copy.deepcopy(newboard)
    
=======
    newboard = x.rules() #returns a NEW board
    x = checkState(newboard, size)
    #saves the state of NEW board for the next iteration

>>>>>>> origin/master
    ###PRINTS THE BOARD###
    printupdate = printBoard(newboard, size)
    printupdate.pBoard()

<<<<<<< HEAD

    
    if i==repeat:
=======
    board = newboard #for global variable of original board

    if i == repeat:
>>>>>>> origin/master
        break;


























