def count(board, character) -> int:
    num = 0
    for row in board:
        num += row.count(character)

    return num


def possible_win(board, character) -> int:
    num = 0
    win = [character]*3
    for row in board:
        if row == character*3:
            num += 1

    for i in range(3):
        if [board[0][i], board[1][i], board[2][i]] == win:
            num += 1

    if [board[0][0], board[1][1], board[2][2]] == win:
        num += 1

    if [board[0][2], board[1][1], board[2][0]] == win:
        num += 1

    return num


def solution(board):
    num_o = count(board, "O")
    num_x = count(board, "X")

    if num_o != num_x + 1 and num_x != num_o:
        return 0

    possible_win_o = possible_win(board, "O")
    possible_win_x = possible_win(board, "X")
    if possible_win_o > 1 or possible_win_x > 1:
        return 0

    if possible_win_o == 1:
        if num_o != num_x + 1:
            return 0
        elif possible_win_x == 1:
            return 0

    if possible_win_x == 1 and num_o != num_x:
        return 0

    return 1
