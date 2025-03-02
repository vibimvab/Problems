from math import log


def solution(n, a, b):
    while n > 0:
        n //= 2

        if a > n and b > n:
            a -= n
            b -= n
        elif a <= n and b <= n:
            continue
        else:
            return log(n, 2) + 1
