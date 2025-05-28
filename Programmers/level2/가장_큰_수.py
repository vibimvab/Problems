def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(reverse=True, key=lambda x: (x*3))
    if numbers[0] == "0":  # return 0 when all elements in numbers are 0
        return "0"
    return "".join(numbers)


if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
