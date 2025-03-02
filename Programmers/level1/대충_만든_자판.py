def solution(keymap, targets):
    num_type_needed = {}
    result = []

    for target in targets:
        num_needed = 0
        try:
            for target_letter in target:
                try:
                    num_needed += num_type_needed[target_letter] + 1

                except KeyError:
                    location = 100
                    for keys in keymap:
                        for index, key in enumerate(keys[:location]):
                            if key == target_letter:
                                location = index
                                break

                    if location == 100:
                        raise RuntimeError
                    else:
                        num_needed += location + 1
                    num_type_needed[target_letter] = location

            result.append(num_needed)

        except RuntimeError:
            result.append(-1)

    return result
