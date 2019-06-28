# #hardcode it first, then generalize it
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
        game_board(game)
        p2_row_input = int(input("Player 2: please enter row number"))
        p2_col_input = int(input("Player 2: please enter column number"))
        game[p2_row_input][p2_col_input] = 'O'
        game_board(game)
        if game[p1_row_input][p1_col_input] == 'X' and game[p1_row_input][p1_col_input + 1] == 'X' and game[p1_row_input][p1_col_input + 2] == 'X':
            playing = False
        if p2_row_input == 0 and p2_col_input == 0 and game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input + 2][p1_col_input] == 'X':
            playing = False
            if game[p1_row_input + 1][p1_col_input + 1] == 'X' and game[p1_row_input + 2][p1_col_input + 2] == 'X':
                playing = False
        if p2_row_input == 0 and p1_row_input == p2_col_input:
            if game[p2_row_input][p2_col_input + 1] == 'O' and game[p2_row_input][p2_col_input + 2] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p2_row_input + 2][p2_col_input] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input + 1] == 'O' and game[p2_row_input + 2][p2_col_input + 2]== 'O':
                playing = False
        if p1_row_input == 0 and p1_col_input == 1:
            if game[p1_row_input][p1_col_input - 1] == 'X' and game[p1_row_input][p1_col_input + 1] == 'X':
                playing = False
            if game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input + 2][p1_col_input] == 'X':
                playing = False
        if p2_row_input == 0 and p2_col_input == 1:
            if game[p2_row_input][p2_col_input - 1] == 'O' and game[p2_row_input][p2_col_input + 1] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p2_row_input + 2][p1_col_input] == 'O':
                playing = False
        if p1_row_input == 0 and p1_col_input == 2:
            if game[p1_row_input][p1_col_input - 1] == 'X' and game[p1_row_input][p1_col_input -2 ] == 'X':
                playing = False
            if game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input + 2][p1_col_input] == 'X':
                playing = False
        if p2_row_input == 0 and p2_col_input == 2:
            if game[p2_row_input][p2_col_input - 1] == 'O' and game[p2_row_input][p2_col_input -2 ] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p2_row_input + 2][p2_col_input] == 'O':
                playing = False
        if p1_row_input == 1 and p1_col_input == 0:
            if game[p1_row_input][p1_col_input + 1] == 'X' and game[p1_row_input][p1_col_input + 2 ] == 'X':
                playing = False
            if game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input - 1][p1_col_input] == 'X':
                playing = False
        if p2_row_input == 1 and p2_col_input == 0:
            if game[p2_row_input][p2_col_input + 1] == 'O' and game[p2_row_input][p2_col_input + 2 ] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p2_row_input - 1][p2_col_input] == 'O':
                playing = False
        if p1_row_input == 1 and p1_col_input == 1:
            if game[p1_row_input][p1_col_input + 1] == 'X' and game[p1_row_input][p1_col_input - 1] == 'X':
                playing = False
            if game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input - 1][p1_col_input] == 'X':
                playing = False
            if game[p1_row_input - 1][p1_col_input - 1] == 'X' and game[p1_row_input + 1][p1_col_input + 1] == 'X':
                playing = False
            if game[p1_row_input + 1][p1_col_input - 1] == 'X' and game[p1_row_input - 1][p1_col_input + 1] == 'X':
                playing = False
        if p2_row_input == 1 and p2_col_input == 1:
            if game[p2_row_input][p2_col_input + 1] == 'O' and game[p2_row_input][p2_col_input - 1] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p1_row_input - 1][p1_col_input] == 'O':
                playing = False
            if game[p2_row_input - 1][p2_col_input - 1] == 'O' and game[p2_row_input + 1][p2_col_input + 1] == 'O':
                playing = False
            if game[p2_row_input + 1][p2_col_input - 1] == 'O' and game[p2_row_input - 1][p2_col_input + 1] == 'O':
                playing = False
        if p1_row_input == 1 and p1_col_input == 2:
            if game[p1_row_input + 1][p1_col_input] == 'X' and game[p1_row_input - 1][p1_col_input] == 'X':
                playing = False
            if game[p1_row_input][p1_col_input - 1] == 'X' and game[p1_row_input][p1_col_input - 2] == 'X':
                playing = False
        if p2_row_input == 1 and p2_col_input == 2:
            if game[p2_row_input + 1][p2_col_input] == 'O' and game[p2_row_input - 1][p2_col_input] == 'O':
                playing = False
            if game[p2_row_input][p2_col_input - 1] == 'O' and game[p2_row_input][p2_col_input - 2] == 'O':
                playing = False
        if p1_row_input == 2 and p1_col_input == 0:
            if game[p1_row_input - 1][p1_col_input] == 'X' and game[p1_row_input - 2][p1_col_input] == 'X':
                playing = False
            if game[p1_row_input][p1_col_input + 1] == 'X' and game[p1_row_input][p1_col_input + 2] == 'X':
                playing = False
        if p2_row_input == 2 and p2_col_input == 0:
            if game[p2_row_input - 1][p2_col_input] == 'O' and game[p2_row_input - 2][p2_col_input] == 'O':
                playing = False
            if game[p2_row_input][p2_col_input + 1] == 'O' and game[p2_row_input][p2_col_input + 2] == 'O':
                playing = False
        if p1_row_input == 2 and p1_col_input == 1:
            if game[p1_row_input - 1][p1_col_input] == 'X' and game[p1_row_input - 2][p1_col_input] == 'X':
                playing = False
            if game[p1_row_input][p1_col_input + 1] == 'X' and game[p1_row_input][p1_col_input - 1] == 'X':
                playing = False
        if p2_row_input == 2 and p2_col_input == 1:
            if game[p2_row_input - 1][p2_col_input] == 'O' and game[p2_row_input - 2][p2_col_input] == 'O':
                playing = False
            if game[p2_row_input][p2_col_input + 1] == 'O' and game[p2_row_input][p2_col_input - 1] == 'O':
                playing = False
        if p1_row_input == 2 and p1_col_input == 2:
            if game[p1_row_input - 1][p1_col_input] == 'X' and game[p1_row_input - 2][p1_col_input] == 'X':
                playing = False
            if game[p1_row_input][p1_col_input - 1] == 'X' and game[p1_row_input][p1_col_input - 2] == 'X':
                playing = False
        if p2_row_input == 2 and p2_col_input == 2:
            if game[p2_row_input - 1][p2_col_input] == 'O' and game[p2_row_input - 2][p2_col_input] == 'O':
                playing = False
            if game[p2_row_input][p2_col_input - 1] == 'O' and game[p2_row_input][p2_col_input - 2] == 'O':
                playing = False

















