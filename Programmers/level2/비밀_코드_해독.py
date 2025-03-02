def test_comb(a, b, c, d, e, q, ans):
    for i, trial in enumerate(q):
        count = 0
        # += 1 if True, += 0 if false
        count += a in trial
        count += b in trial
        count += c in trial
        count += d in trial
        count += e in trial

        if count != ans[i]:
            return 0

    return 1


def solution(n, q, ans):
    answer = 0
    # testing all combinations in range
    for a in range(1, n-3):
        for b in range(a+1, n-2):
            for c in range(b+1, n-1):
                for d in range(c+1, n):
                    for e in range(d+1, n+1):
                        answer += test_comb(a,b,c,d,e,q,ans)

    return answer


if __name__ == "__main__":
    print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
