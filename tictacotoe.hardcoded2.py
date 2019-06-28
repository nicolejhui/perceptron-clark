# hardcode it first, then generalize it
def game_board(game):
    print("   0  1  2")
    count = -1
    for row in game:
        count += 1
        print(count, row)


if __name__ == "__main__":
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_board(game)
    playing = True
    while playing:
        # row
        p1_row_input = int(input("Player 1: please enter row number"))
        # col
        p1_col_input = int(input("Player 1: please enter column number"))
        game[p1_row_input][p1_col_input] = 'X'
        #game_board(game)
        print(game)
        p2_row_input = int(input("Player 2: please enter row number"))
        p2_col_input = int(input("Player 2: please enter column number"))
        game[p2_row_input][p2_col_input] = 'O'
        #game_board(game)
        print(game)
        if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
            print("if statement triggered")
            playing = False

