import random,msvcrt

#initialize the board
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#runFlag is used to check if the game is ended (won/lost). if it is false, game stops
runFlag,boardSize,moveMade=True,4,False

#To print the board
def printBoard():
    print(' ------------------- ')
    for temp in board:
        print('|'+'|'.join(str(x).center(4) for x in temp)+'|'+'\n'+' ------------------- ')

#randomly place 2 at one of the cells of the board
def placeRandom():
    while True:
        x, y = random.randint(0, 3), random.randint(0, 3)
        if (board[x][y] == 0):
            board[x][y] = 2
            return
def makeMove(xcor,ycor,direction,condition,tempdir): #Vert x=tempitr,y=j ; Horz x=j,y=tempitr
    global moveMade
    breakFlag = False
    while eval(condition) and breakFlag==False and (board[xcor][ycor] == 0 or board[xcor][ycor] == board[xcor - direction][ycor-tempdir]):
        if (board[xcor][ycor] == board[xcor - direction][ycor-tempdir]):
            breakFlag = True
        board[xcor][ycor] += board[xcor - direction][ycor-tempdir]
        board[xcor - direction][ycor-tempdir] = 0
        xcor,ycor = xcor+direction,ycor+tempdir
        moveMade = True
def moveVerticle(direction,lv1,lv2,lv3,condition): #direction is -1 for top, +1 for down,-1 for left,+1 for right
    for i in range(lv1,lv2,lv3):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                tempitr = i + direction
                makeMove(tempitr,j,direction,condition,0)
def moveHorizontal(direction,lv1,lv2,lv3,condition):
    for i in range(lv1,lv2,lv3):
        for j in range(len(board[i])):
            if board[j][i]!=0:
                tempitr=i+direction
                makeMove(j,tempitr,0,condition,direction)
def checkIfWon():
    global runFlag
    res=[x for j in board for x in j]
    if 2048 in res:
        runFlag=False
        print('WON')
        return
    if 0 not in res:
        if 0 not in [board[i][j]-board[i+1][j] for i in range(boardSize-1) for j in range(boardSize)] and 0 not in [board[i][j]-board[i][j+1] for i in range(boardSize) for j in range(boardSize-1)]:
            #Above condition checks if there exists a valid move
            print('LOST')
            runFlag=False
def start():
    global moveMade
    #Initialize the board with a 2 at any random position on the board
    board[random.randint(0,3)][random.randint(0,3)]=2
    placeRandom()
    printBoard()
    while runFlag:
        moveMade=False
        if ord(msvcrt.getch())==224:
            key=ord(msvcrt.getch())
            if key==72: #UP
                moveVerticle(-1,1,boardSize,1,'xcor>=0')
            elif key==75: #LEFT
                moveHorizontal(-1,1,boardSize,1,'ycor>=0')
            elif key==77: #RIGHT
                moveHorizontal(1,boardSize-2,-1,-1,'ycor<boardSize')
            elif key==80: #DOWN
                moveVerticle(1,boardSize-2,-1,-1,'xcor<boardSize')
            if (moveMade):
                placeRandom()
                checkIfWon()
            printBoard()
start()
