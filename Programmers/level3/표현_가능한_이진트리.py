def solution(numbers):
    def have_root(n, length):
        if length == 1 or n == 0:
            return True

        split = length // 2 + 1
        if not n & (1 << (split - 1)):
            return False

        if length % 2 != 1:
            raise Exception

        mask = (1 << (split-1)) - 1
        # print(bin(n))
        first_part = n >> split
        second_part = n & mask

        return have_root(first_part, split - 1) and have_root(second_part, split - 1)

    result = []
    for number in numbers:
        tree_length = 1
        bit_length = number.bit_length()
        while tree_length < bit_length:
            tree_length = tree_length * 2 + 1
        result.append(int(have_root(number, tree_length)))

    return result


if __name__ == '__main__':
    # print(solution([7, 42, 5]))
    # print(solution([63, 111, 95]))
    print(solution([8]))
