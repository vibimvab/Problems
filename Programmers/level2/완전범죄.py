def solution(info, n, m):
    candidates = {0: 0}

    for a, b in info:
        if not candidates:
            return -1

        for k in sorted(list(candidates.keys()), reverse=True):
            if k+a < n:
                candidates[k+a] = min(candidates[k], candidates.get(k+a, m))
            if candidates[k] + b < m:
                candidates[k] += b
            else:
                candidates.pop(k)

    if not candidates:
        return -1

    return min(candidates.keys())


if __name__ == '__main__':
    print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
    print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
    print(solution([[3, 3], [3, 3]], 7, 1))
    print(solution([[3, 3], [3, 3]], 6, 1))
