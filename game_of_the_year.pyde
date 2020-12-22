board = list(range(1,10))
def setup():
    global board
    size (340,340)
    main(board)
def draw():
    background (120, 120, 120)
    for y in range (3):
        for x in range(3):
            rect(100*x,100*y,100,100)
def take_input(player_token):
    valid = False
    while not valid:
        try:
            player_answer = int(input("Where do we put" + player_token+"?"))
        except:
            print ("Invalid input. Are you sure you entered the number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("This cell is already taken")
        else:
            print ("Invalid input. Enter a number from 1 to 9 to be like.")
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        draw()
        if counter % 2 == 0:
            take_input("x")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print tmp, ("won!")
                win = True
                break
        if counter == 9:
            print ("Draw!")
            break
    draw()
