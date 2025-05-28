def solution(citations):
    citations.sort(reverse=True)
    l, r = 0, len(citations)-1
    h_index = 0
    while l <= r:
        cur = (l + r) // 2
        if citations[cur] > cur:
            h_index = cur + 1
            l = cur + 1
        else:
            r = cur - 1

    return h_index


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([0] * 100))
