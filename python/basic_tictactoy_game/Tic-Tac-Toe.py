import time
import random
    
mapping = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)}

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print(("+"+"-"*7)*3+"+\n"+("|"+" "*7)*3+"|")
        print("|"+"   "+board[i][0]+"   "+"|"+"   "+board[i][1]+"   "+"|"+"   "+board[i][2]+"   "+"|")
        print(("|"+" "*7)*3+"|")
    print(("+"+"-"*7)*3+"+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    while True:
        try:
            user_input = int(input("Enter your move (1-9): "))
            if user_input in mapping:
                row,col=mapping[user_input]
                if board[row][col]!='x' and board[row][col]!='o':
                    board[row][col]='o'
                    break
                else:
                    print("Invalid Input: Please enter a number that are not marked yet")
                    display_board(board)
           
            else:
                print("Invalid Input: Please enter a valid number (1-9)")
                display_board(board)
        except ValueError:  
            print("Invalid Input: Please enter a number (1-9)")
            display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    lst=[]
    for i in range(1,10):
        row,col=mapping[i]
        if board[row][col]!='x' and board[row][col]!='o':
            lst.append(mapping[i])
            
    return lst

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    for i in range(3):    
        if board[i][0]==board[i][1]==board[i][2]==sign:
            return True
    for i in range(3):    
        if board[0][i]==board[1][i]==board[2][i]==sign:
            return True
    if board[0][0]==board[1][1]==board[2][2]==sign:
        return True
    if board[0][2]==board[1][1]==board[2][0]==sign:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_fields = make_list_of_free_fields(board)
    if free_fields:
        comp_move = random.choice(free_fields)
        row, col = comp_move
        board[row][col] = 'x'

while True:    
    print("____________Welcome to Tic-Tac-Toe!______________")

    board=[[str(i+3*j) for i in range(1,4)] for j in range(3)]
    display_board(board)
    time.sleep(2)
    board[1][1]='x'
    print("Here start's the game")
    display_board(board)


    while True:              
        enter_move(board)
        display_board(board)
        
        if victory_for(board, 'o'):
            print("Congratulations, You won! Well played!")
            break

        print("My move:")
        time.sleep(2)
        draw_move(board)
        display_board(board)

        if victory_for(board, 'x'):
            print("I won! Better luck next time.")
            break
        
        if len(make_list_of_free_fields(board)) == 0:
            print("OOPS, It's a draw!. Try again for a rematch.")
            break

    while True:
        play=input("Do you wanna play one more time?'yes' (y) or 'no' (n): ")
        play = play.lower()
        if play in ['y', 'n', 'yes', 'no']:
            break
        else:
            print("Please enter a valid input ('yes' (y) or 'no' (n)).")
    if play in ['n','no']:
        print("Thank you for playing, Have a wonderful day :)")
        break