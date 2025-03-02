def solution(n, words):
    turn = 1
    player = 1

    prev_end = words[0][0]
    word_list = set()
    for word in words:
        # if the word doesn't start with the previous word's end
        if word[0] != prev_end:
            break
        prev_end = word[-1]

        # if the word is repeated
        if word in word_list:
            break
        word_list.add(word)

        player += 1
        if player > n:
            player = 1
            turn += 1
    else:
        # the game ended with no loser
        return [0, 0]

    answer = [player, turn]
    return answer


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
