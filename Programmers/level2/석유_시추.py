def solution(land):
    rows = len(land)
    cols = len(land[0])
    unvisited = {(i, j) for i in range(rows) for j in range(cols)}
    oils = [0 for _ in range(cols)]

    stack = []
    while unvisited:
        stack.append(unvisited.pop())
        if land[stack[-1][0]][stack[-1][1]] == 0:
            stack.pop()
            continue

        size = 0
        left = cols + 1
        right = -1
        while stack:
            cur = stack.pop()

            size += 1
            left = min(left, cur[1])
            right = max(right, cur[1])

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in moves:
                pos = (cur[0] + dx, cur[1] + dy)
                if pos in unvisited and land[pos[0]][pos[1]] == 1:
                    unvisited.discard(pos)
                    stack.append(pos)

        for i in range(left, right + 1):
            oils[i] += size

    return max(oils)
