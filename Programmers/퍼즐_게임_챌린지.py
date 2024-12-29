def solution(diffs, times, limit):
    start = 0
    end = max(diffs)
    # level = (start + end) // 2
    level = 308
    n = len(diffs)

    while True:
        # try solving
        succeeded = True
        i = 1
        run_time = times[0]
        while i < n:
            if level >= diffs[i]:
                run_time += times[i]
            else:
                run_time += (diffs[i] - level) * times[i - 1]
                run_time += (diffs[i] - level + 1) * times[i]

            i += 1
            if run_time > limit:
                succeeded = False
                break

        if succeeded:  # succeeded solving
            end = level
        else:  # failed solving
            start = level

        level = (start + end) // 2
        if start == level:
            return level + 1


if __name__ == "__main__":
    # print(solution([1, 5, 3], [2, 4, 7], 30))
    # print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
    print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
    # print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))
