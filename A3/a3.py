#a3.py
import random

class tic_tac_toe():

    def __init__(self):
        #board init
        self.board = [0,0,0,0,0,0,0,0,0]

    def display(self):
        #a copy of board

        displayboard=list(self.board)
        for x in range(len(self.board)):
            if self.board[x] == 0:
                displayboard[x]="_"
        print()
        #print board on the left and the corresponding number pad on the right
        print(displayboard[6],displayboard[7],displayboard[8],"|","7","8","9")
        print(displayboard[3],displayboard[4],displayboard[5],"|","4","5","6")
        print(displayboard[0],displayboard[1],displayboard[2],"|","1","2","3")
        print()

    def gameover(self,board):
        # win state is (1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9) but -1
        endgamecase = [(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8)]
        #variable
        variable="0"
        count=0
        tie=False
        if board == None:
            board = self.board

        #check game end result and save the variable
        for index in endgamecase:
            if board[index[0]] == board[index[1]] == board[index[2]]:
                variable=board[index[0]] 
                if variable!=0:
                    break
        #count for tie
        for i in range(len(board)):
            if board[i]!=0:
                count+=1    
           
        #return if variable is obtained or tie, else do nothing
        #you win
        if variable=="X":
            return True,0
        #bot win
        elif variable=="O":
            return True,2
        #tie
        elif count==9:
            return True,1

    def placemove(self):
    #user make a move
        print("Place your move, enter number 1-9: ")
        while True:
            #record user input and change the corresponding tile
            choice = input()
            if int(choice)<1 or int(choice)>9:
                print("invalid move,please enter again:")
            elif self.board[int(choice)-1]=="X" or self.board[int(choice)-1]=="O":
                print("invalid move,please enter again:")
            else:
                self.board[int(choice)-1]="X"
                return

    def all_move(self,board):
    #find all the move within a board given
        all_moves=[]
        for x in range(len(board)):
            if board[x] == 0:
                all_moves.append(x)
        return all_moves

    def AIplacemove(self):
        count = 0
        totalscore = []
        all_moves=list(self.all_move(self.board))
        #if there is only last move left, place the move and return
        if(len(all_moves)==1):
            self.board[all_moves[0]]="O"
            return
        #for every move
        for move in all_moves:
            board = list(self.board)
            variable="O"
            board[move]=variable
            #dont run if there  is one move left
            score_for_1_move=[]
            #run 1000 times for every move to check score
            for times in range(1):
                boardcopy=list(board)
                flag=1
                while flag == 1:
                    copyboard_allmoves=self.all_move(boardcopy)
                    if variable == 'X':
                        variable = 'O'
                    else:
                        variable = 'X'
                    boardcopy[random.choice(copyboard_allmoves)] = variable
                    #if game is done, input score into a list
                    if(self.gameover(boardcopy)!=None):
                        score_for_1_move.append(self.gameover(boardcopy)[1])
                        flag=0
            totalscore.append([move,sum(score_for_1_move)])          
        #find the max score and the index from the score list
        maxscore=0
        index=0
        for i in range(len(totalscore)):
            if(totalscore[i][1]>maxscore):
                maxscore=totalscore[i][1]
                index=totalscore[i][0]
        self.board[index]="O"


def play_a_new_game():
    whosfirst = input('Do you want to go first? (y or Y for yes, otherwise bot go first): ')
    if whosfirst == "Y" or whosfirst == "y":
        flag=0
    else:
        flag=1
    new_game=tic_tac_toe()
    new_game.display()

    while not new_game.gameover(new_game.board):
        print("----------------------------------")
        #user's move
        if flag==0:
            new_game.placemove()
            print("My move:")
            new_game.display()
            flag=1
        #bot's move
        else:
            new_game.AIplacemove()
            print("Ai's move:")
            new_game.display()
            flag=0
    print("----------------------------------")
    if(new_game.gameover(new_game.board)[1]==0):
        print("You Win!")
    elif(new_game.gameover(new_game.board)[1]==1):
        print("Tie Game")
    elif(new_game.gameover(new_game.board)[1]==2):
        print("Bot Win!")

if __name__ == '__main__':
    play_a_new_game()