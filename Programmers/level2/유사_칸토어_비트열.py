def solution(n, l, r):
    if n == 0:
        return 1

    answer = 0
    for i in range(5):
        if i == 2:
            continue

        # interval is inclusive
        left_end = i * 5**(n-1) + 1
        right_end = (i+1) * 5**(n-1)
        if right_end < l or r < left_end:
            # if the interval and l, r does not overlap
            continue
        else:
            if left_end < l:
                if right_end < r:
                    answer += solution(n-1, l-left_end+1, 5**(n-1))
                else:
                    answer += solution(n-1, l-left_end+1, r-left_end+1)

            else:
                if right_end < r:
                    answer += 4**(n-1)
                else:
                    answer += solution(n-1, 1, r-left_end+1)

    return answer


if __name__ == '__main__':
    for left in range(1, 25):
        for right in range(left, 26):
            print(left, right, solution(2, left, right))
