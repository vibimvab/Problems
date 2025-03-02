def solution(X: str, Y: str):
    # count the numbers in X and Y
    x_count = [0] * 10
    y_count = [0] * 10
    for x in X:
        x_count[int(x)] += 1
    for y in Y:
        y_count[int(y)] += 1

    # from 9 to 1 add numbers to answer
    answer = ''
    for i in range(9, 0, -1):
        answer += str(i) * min(x_count[i], y_count[i])

    if answer:  # if answer is not an empty string
        answer += '0' * min(x_count[0], y_count[0])
        return answer
    elif min(x_count[0], y_count[0]) == 0:
        return '-1'
    else:
        return '0'
