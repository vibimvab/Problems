def check_palindrome(s, odd_even, palindrome_list, count, run_other_bool):
    # return palindrome_list, run_bool, end
    temp_palindrome = []
    for index in palindrome_list:
        try:
            if index - count < 0:
                raise IndexError
            if s[index - count] == s[index + count + odd_even - 1]:
                temp_palindrome.append(index)
        except IndexError:
            pass

    if temp_palindrome:
        return temp_palindrome, True, False
    else:
        if run_other_bool:
            return palindrome_list, False, False
        else:
            return palindrome_list, False, True


def longest_palindrome(s: str) -> str:
    s_len = len(s)
    odd_len_palindrome = [i for i in range(s_len)]
    even_len_palindrome = []
    for i in range(s_len - 1):
        if s[i] == s[i + 1]:
            even_len_palindrome.append(i)

    run_odd = True if odd_len_palindrome else False
    run_even = True if even_len_palindrome else False

    i = 1
    while True:
        if run_odd:
            odd_len_palindrome, run_odd, end = check_palindrome(s, 1, odd_len_palindrome, i, run_even)
            if end:
                return s[odd_len_palindrome[0] - (i - 1):odd_len_palindrome[0] + i]

        if run_even:
            even_len_palindrome, run_even, end = check_palindrome(s, 2, even_len_palindrome, i, run_odd)
            if end:
                return s[even_len_palindrome[0] - (i - 1):even_len_palindrome[0] + (i + 1)]

        i += 1
