def length_of_longest_substring(s: str) -> int:
    substring_list = []
    substring_length_list = []
    for char in s:
        try:
            substring_list = substring_list[substring_list.index(char) + 1:]
        except ValueError:
            substring_length_list.append(len(substring_list) + 1)
        finally:
            substring_list.append(char)

    return max(substring_length_list) if substring_length_list else 0
