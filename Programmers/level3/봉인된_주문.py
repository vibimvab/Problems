from string import ascii_lowercase


def add_1(target):
    for i in range(len(target)-1, -1, -1):
        target[i] += 1
        if target[i] > 26:
            target[i] = 1
        else:
            return

    target.insert(0, 1)


def solution(n, bans):
    target = []
    while n > 0:
        n -= 1  # shift to 0-based
        target.append(n % 26 + 1)
        n //= 26
    target = target[::-1]
    print(target)

    bans.sort(key=lambda s: (len(s), s))
    for ban in bans:
        if (len(target), target) >= (len(ban), [ord(c) - ord('a') + 1 for c in ban]):
            add_1(target)
        else:
            break

    return ''.join([ascii_lowercase[n-1] for n in target])


if __name__ == '__main__':
    print(solution(30, ["d", "e", "bb", "aa", "ae"]))
    print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))
    print(solution(701, ["d", "e", "bb", "aa", "ae"]))
    # print([ord(c) - ord('a') + 1 for c in "zz"])
    # print(''.join(chr(i + ord('a') - 1) for i in [26, 26]))
