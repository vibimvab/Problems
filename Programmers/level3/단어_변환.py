def solution(begin, target, words):
    words_set = set(words)
    if target not in words_set:
        return 0

    level = 1
    current_layer = {begin}
    next_layer = set()
    while words_set and current_layer:
        for current_word in current_layer:
            for word in words_set:
                diff = 0
                for i in range(len(begin)):
                    if current_word[i] != word[i]:
                        diff += 1
                if diff == 1:
                    if word == target:
                        return level
                    next_layer.add(word)
            words_set -= next_layer
        current_layer = next_layer
        next_layer = set()
        level += 1

    return 0


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
