from itertools import product


def solution(users, emoticons):
    answer = (0, 0)
    for sales in list(product(range(10, 50, 10), repeat=len(emoticons))):
        user_spends = [0] * len(users)
        for user_idx, user in enumerate(users):
            for emoticon_idx, sale in enumerate(sales):
                if sale >= user[0]:
                    user_spends[user_idx] += emoticons[emoticon_idx] // 100 * (100 - sale)

        plus_count = 0
        total_sales = 0
        for i, user in enumerate(users):
            if user[1] <= user_spends[i]:
                plus_count += 1
            else:
                total_sales += user_spends[i]

        answer = max(answer, (plus_count, total_sales))

    return answer


if __name__ == '__main__':
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))