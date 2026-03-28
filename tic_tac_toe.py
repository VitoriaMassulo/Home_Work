def create_board():
    return [str(index) for index in range(1, 10)]

def print_board(board: list):
    '''
    this one turns a list into a board
    '''

    rows = [board[0:3], board[3:6], board[6:9]]

    for index, row in enumerate(rows):
        print(" " + " | ".join(row))
        if index < 2:
            print("---+---+---")

def get_move(player, board):
    '''
    this one will check the player input,
    handling the given possible invalid inputs and moves.
    '''

    while True:
        move_rule =  (f"\n🎯 Rules:\n❌ A spot that is already taken cant be chosen.\n"
               f"❌ There are only spots from 1 - 9. Choose a preferable available spot.\n"
               f"😄 Now that you know, Try again.\n")

        print(f"Player {player}, choose your spot:")

        try:
            spot_choice = int(input("Enter a spot number (1 to 9): "))

            if spot_choice not in range(1, 10):
                print(f"{move_rule}")
                continue

            if board[spot_choice - 1] in ["X", "O"]:
                print(f"{move_rule}")
                continue

            return spot_choice

        except ValueError:
            print("\n❌ Cannot input letters or other simbols to choose a spot.\n")
            continue

def make_move(board, position, symbol):

    '''
    this one pretty much places the symbol on the board,
    on the chosen position.
    '''
    for index, spot in enumerate(board):
        if index == position - 1:
            board[index] = symbol
            break

def check_winner(board, symbol):
    '''
    this one loops through the winning indexes
    and if the symbols in there match.
    '''

    winning_spots = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]

    for W_spots in winning_spots:
        if all(board[index] == symbol for index in W_spots):
            return True

    return False

def is_tie(board):
    for spot in board:
        if spot.isdigit():
            return False

    return True

def score_print(score):
    print("\n=== SCOREBOARD ===\n")
    print(f"❌ Player X: {score['X']} wins!")
    print(f"⭕ Player O: {score['O']} wins!")
    print(f"👔 Ties: {score['Ties']}\n")

def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

def play_again():
    '''
    this just cheks whether to play again or not.
    '''

    while True:
        replay = input("Play again? Type your choice (yes/no): ").lower()
        if replay == "yes":
            return True
        elif replay == "no":
            print("\n✨ Thank you for playing my game ✨")
            return False
        else:
            print("Please, type yes or no.")

def play_game():
    print("=== ❌ Welcome to my Tic Tac Toe! ⭕ ===\n")

    score = {
        "X": 0,
        "O": 0,
        "Ties": 0
    }

    while True:
        board = create_board()
        current_player = "X"

        while True:
            print_board(board)
            position = get_move(current_player, board)
            make_move(board, position, current_player)

            if check_winner(board, current_player):
                print_board(board)
                print(f"\n🏆 Player {current_player} wins!\n")
                score[current_player] =+ 1
                score_print(score)
                break

            if is_tie(board):
                print_board(board)
                print("\nIt's a tie! 👔\n")
                score["Ties"] += 1
                score_print(score)
                break

            current_player = switch_player(current_player)

        replay = play_again()
        if replay == False:
            break



play_game()