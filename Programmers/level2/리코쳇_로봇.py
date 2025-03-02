from queue import Queue


def move_up(current, board):
    x = current[1]
    y = current[0]
    while y >= 0 and board[y][x] != 'D':
        y -= 1
    return y + 1, x


def move_down(current, board):
    x = current[1]
    y = current[0]
    while y < len(board) and board[y][x] != 'D':
        y += 1
    return y - 1, x


def move_right(current, board):
    x = current[1]
    y = current[0]
    while x < len(board[0]) and board[y][x] != 'D':
        x += 1
    return y, x - 1


def is_dest_in_visited(dest, visited, q, next_node_count):
    if dest not in visited:
        visited.add(dest)
        q.put(dest)
        return next_node_count + 1
    else:
        return next_node_count


def move_left(current, board):
    x = current[1]
    y = current[0]
    while x >= 0 and board[y][x] != 'D':
        x -= 1
    return y, x + 1


def solution(board):
    # find start
    start = (-1, -1)
    for i, row in enumerate(board):
        if row.find('R') != -1:
            start = (i, row.find('R'))
            break
    assert start != (-1, -1)

    visited = set()
    visited.add(start)
    q = Queue()
    q.put(start)
    layer = 0
    current_node_count = 1
    next_node_count = 0
    while not q.empty():
        current = q.get()
        if board[current[0]][current[1]] == 'G':
            return layer

        dest = move_up(current, board)
        next_node_count = is_dest_in_visited(dest, visited, q, next_node_count)

        dest = move_down(current, board)
        next_node_count = is_dest_in_visited(dest, visited, q, next_node_count)

        dest = move_right(current, board)
        next_node_count = is_dest_in_visited(dest, visited, q, next_node_count)

        dest = move_left(current, board)
        next_node_count = is_dest_in_visited(dest, visited, q, next_node_count)

        current_node_count -= 1
        if current_node_count == 0:
            current_node_count = next_node_count
            next_node_count = 0
            layer += 1

    return -1


if __name__ == '__main__':
    print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
