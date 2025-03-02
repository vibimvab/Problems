from itertools import product, combinations


def solution(dice):
    n = len(dice)
    win_count = dict.fromkeys(combinations(range(0, n), n//2), 0)
    for case in product(range(6), repeat=n):
        values = [dice[i][case[i]] for i in range(n)]
        total = sum(values)
        for combo in win_count.keys():
            my_sum = sum([values[i] for i in combo])
            if my_sum > total - my_sum:
                win_count[combo] += 1

    best_win_count = -1
    best_combo = []
    for key in win_count:
        if win_count[key] > best_win_count:
            best_win_count = win_count[key]
            best_combo = key

    return [n+1 for n in best_combo]


if __name__ == '__main__':
    print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))
    print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))
