from sys import setrecursionlimit


def find_min_cost(strs_len, t, i, dp, sig):
    try:
        return dp[i]
    except KeyError:
        pass

    cost = sig
    for j in range(1, 6):
        next_chars = t[i:i+j]
        if next_chars in strs_len[j]:
            cost = min(1 + find_min_cost(strs_len, t, i+j, dp, sig), cost)

    dp[i] = cost
    return cost


def solution(strs, t):
    # index as a key, number of strs needed as value
    dp = {len(t): 0}  # base case

    # sorting the strs by their length
    strs_len = {key: set() for key in range(6)}
    for string in strs:
        strs_len[len(string)].add(string)

    setrecursionlimit(len(t) + 10)
    sig = len(t)+1  # when there is no possible way, it returns signal
    answer = find_min_cost(strs_len, t, 0, dp, sig)
    setrecursionlimit(1000)
    if answer == sig:
        return -1
    else:
        return answer


if __name__ == '__main__':
    print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
    print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
