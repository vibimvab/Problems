import string


def update_reachable(x, y, rows, cols, reachable: set[(int, int)], taken: set[(int, int)]):
    stack = [(x, y)]
    while stack:
        i, j = stack.pop()
        if i > 0:
            if (i-1, j) in taken and (i-1, j) not in reachable:
                stack.append((i-1, j))
            reachable.add((i-1, j))

        if i < rows-1:
            if (i+1, j) in taken and (i+1, j) not in reachable:
                stack.append((i+1, j))
            reachable.add((i+1, j))

        if j > 0:
            if (i, j-1) in taken and (i, j-1) not in reachable:
                stack.append((i, j-1))
            reachable.add((i, j-1))

        if j < cols-1:
            if (i, j+1) in taken and (i, j+1) not in reachable:
                stack.append((i, j+1))
            reachable.add((i, j+1))


def fork_lift(c: str, rows: int, cols: int,
              containers: dict[str, [(int, int)]], reachable: set[(int, int)], taken: set[(int, int)]):
    update_list = []
    for x, y in containers[c]:
        if (x, y) in reachable:
            taken.add((x, y))
            update_list.append((x, y))

    for x, y in update_list:
        containers[c].remove((x, y))
        update_reachable(x, y, rows, cols, reachable, taken)


def crane(c: str, rows: int, cols: int,
          containers: dict[str, [(int, int)]], reachable: set[(int, int)], taken: set[(int, int)]):
    for x, y in containers[c]:
        taken.add((x, y))

        if (x, y) in reachable:
            update_reachable(x, y, rows, cols, reachable, taken)


def solution(storage: [str], requests: [str]):
    rows: int = len(storage)
    cols: int = len(storage[0])

    containers: dict[str, set[(int, int)]] = {k: set() for k in string.ascii_uppercase}
    for i in range(rows):
        for j in range(cols):
            containers[storage[i][j]].add((i, j))

    reachable: set[(int, int)] = set((i, 0) for i in range(rows))
    reachable.update((i, cols-1) for i in range(rows))
    reachable.update((0, i) for i in range(cols))
    reachable.update((rows-1, i) for i in range(cols))
    print(reachable)

    taken: set[(int, int)] = set()

    for request in requests:
        if len(request) == 1:
            fork_lift(request, rows, cols, containers, reachable, taken)
        if len(request) == 2:
            crane(request[0], rows, cols, containers, reachable, taken)

    return rows * cols - len(taken)


if __name__ == '__main__':
    print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))