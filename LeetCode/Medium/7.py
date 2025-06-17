def reverse(x: int) -> int:
    sign = 1 if x >= 0 else -1
    if x == -(2 ** 31):
        return 0

    else:
        x = sign * x
        # x > 10 ** 10 인 경우는 애초에 32bit에 저장이 안되기 때문에 input으로 들어올 수가 없음
        if x < 10 ** 9:
            return int(str(x)[::-1]) * sign
        else:
            range_num = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
            n = x
            for num in range_num:
                if n % 10 > num:
                    return 0
                elif n % 10 == num:
                    n //= 10
                else:
                    return int(str(x)[::-1]) * sign

            return int(str(x)[::-1]) * sign
