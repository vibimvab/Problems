def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    result: str = s[::(num_rows - 1) * 2]
    for i in range(1, num_rows - 1):
        temp: str = ''
        for j in range(0, len(s) + i, (num_rows - 1) * 2):
            try:
                temp += s[j - i]
                temp += s[j + i]
            except IndexError:
                pass
        result += temp[1:]

    result += s[num_rows - 1::(num_rows - 1) * 2]

    return result
