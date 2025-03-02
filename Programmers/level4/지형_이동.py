from queue import Queue
import heapq


def cost_to_end(land, height):
    # 문제를 잘못 이해함, 지우기 아까워서 남겨둠
    dp = {}
    row_count = len(land)
    col_count = len(land[0])

    dp[(row_count-1, col_count-1)] = 0  # base case
    # rightmost column
    for i in range(row_count-2, -1, -1):
        diff = abs(land[i+1][col_count - 1] - land[i][col_count - 1])
        if diff > height:
            dp[(i, col_count-1)] = dp[(i+1, col_count-1)] + diff
        else:
            dp[(i, col_count-1)] = dp[(i+1, col_count-1)]

    # bottommost row
    for i in range(col_count-2, -1, -1):
        diff = abs(land[row_count-1][i+1] - land[row_count-1][i])
        if diff > height:
            dp[(row_count-1, i)] = dp[(row_count-1, i+1)] + diff
        else:
            dp[(row_count - 1, i)] = dp[(row_count - 1, i + 1)]

    # calculate cost on each tile
    for i in range(row_count-2, -1, -1):
        for j in range(col_count-2, -1, -1):
            down_diff = abs(land[i+1][j] - land[i][j])
            if down_diff > height:
                down_cost = dp[(i+1, j)] + down_diff
            else:
                down_cost = dp[(i+1, j)]

            right_diff = abs(land[i][j+1] - land[i][j])
            if right_diff > height:
                right_cost = dp[(i, j+1)] + right_diff
            else:
                right_cost = dp[(i, j + 1)]

            dp[(i, j)] = min(down_cost, right_cost)

    return dp[(0, 0)]


def solution(land, height):
    n = len(land)

    # split the land by chucks of lands that can be traveled without ladder: O(n^2)
    tiles = []
    for i in range(n):
        tiles.extend([(i, j) for j in range(n)])
    tiles = set(tiles)

    chunk_num_matrix = [[-1]*n for _ in range(n)]
    chunk_num = 0
    while tiles:
        q = Queue()
        current = tiles.pop()
        chunk_num_matrix[current[0]][current[1]] = chunk_num
        q.put(current)
        while not q.empty():
            current = q.get()
            row = current[0]
            col = current[1]

            # left
            if col > 0 and chunk_num_matrix[row][col-1] == -1 and abs(land[row][col-1] - land[row][col]) <= height:
                tiles.discard((row, col-1))
                chunk_num_matrix[row][col-1] = chunk_num
                q.put((row, col-1))

            # right
            if col < n-1 and chunk_num_matrix[row][col+1] == -1 and abs(land[row][col+1] - land[row][col]) <= height:
                tiles.discard((row, col+1))
                chunk_num_matrix[row][col+1] = chunk_num
                q.put((row, col + 1))

            # top
            if row > 0 and chunk_num_matrix[row-1][col] == -1 and abs(land[row-1][col] - land[row][col]) <= height:
                tiles.discard((row-1, col))
                chunk_num_matrix[row-1][col] = chunk_num
                q.put((row - 1, col))

            # bottom
            if row < n-1 and chunk_num_matrix[row+1][col] == -1 and abs(land[row+1][col] - land[row][col]) <= height:
                tiles.discard((row+1, col))
                chunk_num_matrix[row+1][col] = chunk_num
                q.put((row + 1, col))

        chunk_num += 1

    # print(chunk_num)
    # for row in chunk_num_matrix:
    #     print(row)

    # build the weighted graph with the chunks O(n^2)
    edge_dict = {i: {} for i in range(chunk_num)}
    for row in range(n):
        for col in range(n):
            current_chunk_num = chunk_num_matrix[row][col]

            # right
            if col < n - 1:
                r_chunk_num = chunk_num_matrix[row][col + 1]
                if r_chunk_num != current_chunk_num:
                    try:
                        edge_dict[r_chunk_num][current_chunk_num] = min(edge_dict[r_chunk_num][current_chunk_num], abs(land[row][col + 1] - land[row][col]))
                        edge_dict[current_chunk_num][r_chunk_num] = edge_dict[r_chunk_num][current_chunk_num]
                    except KeyError:
                        edge_dict[r_chunk_num][current_chunk_num] = abs(land[row][col + 1] - land[row][col])
                        edge_dict[current_chunk_num][r_chunk_num] = edge_dict[r_chunk_num][current_chunk_num]

            # bottom
            if row < n - 1:
                b_chunk_num = chunk_num_matrix[row + 1][col]
                try:
                    if b_chunk_num != current_chunk_num:
                        edge_dict[b_chunk_num][current_chunk_num] = min(edge_dict[b_chunk_num][current_chunk_num], abs(land[row + 1][col] - land[row][col]))
                        edge_dict[current_chunk_num][b_chunk_num] = edge_dict[b_chunk_num][current_chunk_num]
                except KeyError:
                    edge_dict[b_chunk_num][current_chunk_num] = abs(land[row + 1][col] - land[row][col])
                    edge_dict[current_chunk_num][b_chunk_num] = edge_dict[b_chunk_num][current_chunk_num]

    # Prim's algorithm
    connected = set()
    total_weight = 0
    min_heap = [(0, 0, -1)]  # (weight, node, parent)
    while len(connected) < chunk_num:
        weight, source, parent = heapq.heappop(min_heap)

        if source in connected:
            continue

        connected.add(source)
        if parent != -1:  # Exclude the first node (no parent)
            total_weight += weight

        for dest, w in edge_dict[source].items():
            if dest not in connected:
                heapq.heappush(min_heap, (w, dest, source))

    return total_weight


if __name__ == '__main__':
    print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
    print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
