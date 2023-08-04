from os import system

Depth = 4
infinity = 999


def move(input_board, row, column, turn):
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(input_board[i][j])

    if board[row][column] != ' ':
        return False, board
    opposite = 'O' if turn == 'X' else 'X'
    ans = False
    if row > 1:
        if board[row - 1][column] == opposite:
            flag = False
            i = 2
            while row - i >= 0:
                if board[row - i][column] == turn:
                    flag = True
                    ans = True
                    break
                elif board[row - i][column] == ' ':
                    break
                i += 1
            if flag:
                board[row - 1][column] = turn
                i = 2
                while row - i >= 0:
                    if board[row - i][column] == turn:
                        break
                    board[row - i][column] = turn
                    i += 1

        if column > 1:
            if board[row - 1][column - 1] == opposite:
                flag = False
                i = 2
                while row - i >= 0 and column - i >= 0:
                    if board[row - i][column - i] == turn:
                        flag = True
                        ans = True
                        break
                    elif board[row - i][column - i] == ' ':
                        break
                    i += 1
                if flag:
                    board[row - 1][column - 1] = turn
                    i = 2
                    while row - i >= 0 and column - i >= 0:
                        if board[row - i][column - i] == turn:
                            break
                        board[row - i][column - i] = turn
                        i += 1

        if column < 6:
            if board[row - 1][column + 1] == opposite:
                flag = False
                i = 2
                while row - i >= 0 and column + i < 8:
                    if board[row - i][column + i] == turn:
                        flag = True
                        ans = True
                        break
                    elif board[row - i][column + i] == ' ':
                        break
                    i += 1
                if flag:
                    board[row - 1][column + 1] = turn
                    i = 2
                    while row - i >= 0 and column + i < 8:
                        if board[row - i][column + i] == turn:
                            break
                        board[row - i][column + i] = turn
                        i += 1

    if row < 6:
        if board[row + 1][column] == opposite:
            flag = False
            i = 2
            while row + i < 8:
                if board[row + i][column] == turn:
                    flag = True
                    ans = True
                    break
                elif board[row + i][column] == ' ':
                    break
                i += 1
            if flag:
                board[row + 1][column] = turn
                i = 2
                while row + i < 8:
                    if board[row + i][column] == turn:
                        break
                    board[row + i][column] = turn
                    i += 1

        if column > 1:
            if board[row + 1][column - 1] == opposite:
                flag = False
                i = 2
                while row + i < 8 and column - i >= 0:
                    if board[row + i][column - i] == turn:
                        flag = True
                        ans = True
                        break
                    elif board[row + i][column - i] == ' ':
                        break
                    i += 1
                if flag:
                    board[row + 1][column - 1] = turn
                    i = 2
                    while row + i < 8 and column - i >= 0:
                        if board[row + i][column - i] == turn:
                            break
                        board[row + i][column - i] = turn
                        i += 1
        if column < 6:
            if board[row + 1][column + 1] == opposite:
                flag = False
                i = 2
                while row + i < 8 and column + i < 8:
                    if board[row + i][column + i] == turn:
                        flag = True
                        ans = True
                        break
                    elif board[row + i][column + i] == ' ':
                        break
                    i += 1
                if flag:
                    board[row + 1][column + 1] = turn
                    i = 2
                    while row + i < 8 and column + i < 8:
                        if board[row + i][column + i] == turn:
                            break
                        board[row + i][column + i] = turn
                        i += 1

    if column > 1:
        if board[row][column - 1] == opposite:
            flag = False
            i = 2
            while column - i >= 0:
                if board[row][column - i] == turn:
                    flag = True
                    ans = True
                    break
                elif board[row][column - i] == ' ':
                    break
                i += 1
            if flag:
                board[row][column - 1] = turn
                i = 2
                while column - i >= 0:
                    if board[row][column - i] == turn:
                        break
                    board[row][column - i] = turn
                    i += 1
    if column < 6:
        if board[row][column + 1] == opposite:
            flag = False
            i = 2
            while column + i < 8:
                if board[row][column + i] == turn:
                    flag = True
                    ans = True
                    break
                elif board[row][column + i] == ' ':
                    break
                i += 1
            if flag:
                board[row][column + 1] = turn
                i = 2
                while column + i < 8:
                    if board[row][column + i] == turn:
                        break
                    board[row][column + i] = turn
                    i += 1

    if ans:
        board[row][column] = turn

    return ans, board


def can_move(board, turn):
    for x in range(8):
        for y in range(8):
            can_player_move, _ = move(board, x, y, turn)
            if can_player_move:
                return True
    return False


def print_board(board):
    print("    0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print("   -------------------------------")
    for i in range(8):
        print(i, end=" ")
        for x in board[i]:
            print("| " + x, end=" ")
        print("|")
        print("   -------------------------------")
    print()


def score(board, maximizing_player):
    opposite = 'X' if maximizing_player == 'O' else 'O'
    flag = True
    ans = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                flag = False
            elif board[i][j] == maximizing_player:
                ans += 1
            else:
                ans -= 1

    if flag:
        if ans > 0:
            return 5
        elif ans < 0:
            return -5
        return 0

    if not can_move(board, maximizing_player) and not can_move(board, opposite):
        if ans > 0:
            return 5
        elif ans < 0:
            return -5
        return 0

    corners = 0
    if board[0][0] == maximizing_player:
        corners += 1
    elif board[0][0] == opposite:
        corners -= 1
    if board[0][7] == maximizing_player:
        corners += 1
    elif board[0][7] == opposite:
        corners -= 1
    if board[7][0] == maximizing_player:
        corners += 1
    elif board[7][0] == opposite:
        corners -= 1
    if board[7][7] == maximizing_player:
        corners += 1
    elif board[7][7] == opposite:
        corners -= 1

    return ans/64 + corners


def minimax(board, turn, alpha, beta, depth, maximizing_player):
    opposite = 'X' if turn == 'O' else 'O'
    if depth == 0:
        return board
    boards = []
    for i in range(8):
        for j in range(8):
            validity, state = move(board, i, j, turn)
            if validity:
                boards.append(state)

    if not boards:
        return board

    ans = []
    if maximizing_player:
        max_value = -infinity
        for state in boards:
            new_board = minimax(state, opposite, alpha, beta, depth - 1, False)
            value = score(new_board, turn)
            if value > max_value:
                ans = state
                max_value = value
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return ans

    min_value = infinity
    for state in boards:
        new_board = minimax(state, opposite, alpha, beta, depth - 1, True)
        value = score(new_board, opposite)
        if value < min_value:
            ans = state
            min_value = value
            beta = min(min_value, value)
            if beta <= alpha:
                break
    return ans


main_board = []
for index in range(8):
    main_board.append([])
    for _ in range(8):
        main_board[index].append(' ')
main_board[3][3] = 'X'
main_board[4][4] = 'X'
main_board[3][4] = 'O'
main_board[4][3] = 'O'


cpu = 'X'
player = input("Do you want to be the starter(X is the starter)? (y/n): ")
while player != "y" and player != "n":
    player = input("\nWrong Entry, Enter either y or n: ")


if player == 'n':
    main_board = minimax(main_board, cpu, -infinity, infinity, 1, True)
    player = 'O'
else:
    player = 'X'
    cpu = 'O'

while True:
    # system('cls')
    print()
    print_board(main_board)
    if can_move(main_board, player):
        player_move = input("Enter the position of your move as a two digit number(first digit is row): ")
        valid = False
        while not valid:
            if len(player_move) != 2:
                player_move = input("\nWrong Entry, Enter a two digit number: ")
                continue
            if not (0 <= int(player_move[0]) < 8 and 0 <= int(player_move[1]) < 8):
                player_move = input("\nWrong Entry, digits must be between 0 and 7, Enter again: ")
                continue
            valid, main_board = move(main_board, int(player_move[0]), int(player_move[1]), player)
            if not valid:
                player_move = input("\nCan't place your piece in this position, Enter again: ")
                continue
        print_board(main_board)
    elif can_move(main_board, cpu):
        print("There is no possible move for you, CPU's turn\n")
        main_board = minimax(main_board, cpu, -infinity, infinity, Depth, True)
        continue
    else:
        print()
        if score(main_board, player) > 0:
            print("You Won!")
        elif score(main_board, player) < 0:
            print("CPU Won!")
        else:
            print("Draw!")
        input("\nPress Enter to Exit the game\n")
        break

    if can_move(main_board, cpu):
        print("CPU is choosing ...")
        main_board = minimax(main_board, cpu, -infinity, infinity, Depth, True)
    else:
        print("There is no possible move for CPU, Your turn\n")
