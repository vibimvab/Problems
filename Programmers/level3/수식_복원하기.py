def test_base(exp, base):
    n = [exp[0] // 10, exp[0] % 10]
    m = [exp[2] // 10, exp[2] % 10]

    if exp[-1] == 'X':
        return not any(x >= base for x in n + m)

    expected = [exp[4] // 100, (exp[4] % 100) // 10, exp[4] % 10]
    if any(x >= base for x in n + m + expected):
        return False

    if exp[1] == '+':
        s = ((n[1] + m[1]) >= base) + (n[0] + m[0])
        actual = [s // base, s % base, (n[1] + m[1]) % base]
    else:
        actual = [0,  (n[0] - m[0]) - ((n[1] - m[1]) < 0), (n[1] - m[1] + base) % base]

    return all(actual[i] == expected[i] for i in range(3))


def find_valid(exp, bases):
    n = [exp[0] // 10, exp[0] % 10]
    m = [exp[2] // 10, exp[2] % 10]
    result = []

    for base in bases:
        if exp[1] == '+':
            s = ((n[1] + m[1]) >= base) + (n[0] + m[0])
            if not result:
                result = [s // base, s % base, (n[1] + m[1]) % base]
            else:
                new_result = [s // base, s % base, (n[1] + m[1]) % base]
                if any(result[i] != new_result[i] for i in range(3)):
                    return '?'
        else:
            if not result:
                result = [(n[0] - m[0]) - ((n[1] - m[1]) < 0), (n[1] - m[1] + base) % base]
            else:
                new_result = [(n[0] - m[0]) - ((n[1] - m[1]) < 0), (n[1] - m[1] + base) % base]
                if any(result[i] != new_result[i] for i in range(2)):
                    return '?'

    if not result:
        return '?'
    return ''.join(str(x) for x in result).lstrip('0') or '0'


def solution(expressions, verbose=False):
    unsolved = []
    bases = {i for i in range(2, 10)}

    # preprocessing: split the expressions and convert strings to integers
    for i, exp in enumerate(expressions):
        expressions[i] = exp.split()
        expressions[i][0] = int(expressions[i][0])
        expressions[i][2] = int(expressions[i][2])
        if exp[-1] != 'X':
            expressions[i][4] = int(expressions[i][4])
        else:
            unsolved.append(expressions[i][0:3])

    # find invalid bases
    for exp in expressions:
        invalid = set()
        for base in bases:
            if not test_base(exp, base):
                invalid.add(base)
        bases -= invalid
        if len(bases) < 2:
            break

    # complete unsolved expressions
    answer = []
    for exp in unsolved:
        answer.append(f"{exp[0]} {exp[1]} {exp[2]} = {find_valid(exp, bases)}")

    return answer


if __name__ == '__main__':
    # print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
    # print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
    # print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
    # print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
    # print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
    # print(solution(["41 + 25 = 66", "10 + 45 = X", "15 + 34 = X"]))
    # solution(["4 - 20 = 37"])

    for a in range(3):
        for b in range(3):
            for c in range(3):
                if (''.join(str(x) for x in [a, b, c]).lstrip('0') or '0') != (''.join(str(x) for i, x in enumerate([a, b, c]) if i == len([a, b, c])-1 or x > 0)):
                    print([a,b,c])
                    print((''.join(str(x) for x in [a, b, c]).lstrip('0') or '0'))
                    print((''.join(str(x) for i, x in enumerate([a, b, c]) if i == len([a, b, c])-1 or x > 0)))

