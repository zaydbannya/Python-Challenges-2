
theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

board_keys = []
for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def check_winner(board, player):
    win_combinations = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], 
        ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'], 
        ['7', '5', '3'], ['9', '5', '1']                  
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def game():
    turn = 'x'
    count = 0       
    for i in range(10): 
        printBoard(theBoard) 
        print("It's your turn, " + turn + ". Move to which place?")
        
        move = input()  
        if theBoard[move] == ' ':
            theBoard[move] = turn  
            count += 1
        else:
            print("That place is already filled. Try again.")
            continue
        if count >= 5:
            if check_winner(theBoard, turn):
                printBoard(theBoard)  
                print(f"Player {turn} wins!")
                break
        if count == 9:
            printBoard(theBoard)
            print("It's a draw!")
            break
        turn = 'o' if turn == 'x' else 'x'
if __name__ == "__main__":
    game()