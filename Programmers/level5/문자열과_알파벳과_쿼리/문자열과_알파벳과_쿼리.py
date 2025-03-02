import string


class WordList:
    def __init__(self, s: str):
        self.letters = s
        self.letter_to_word = [0] * len(s)
        self.alphabet_to_letter_num: dict[str, set[int]] = {char: set() for char in string.ascii_lowercase}
        for i, c in enumerate(s):
            self.alphabet_to_letter_num[c].add(i)
        self.word_list: dict[int, set[int]] = {0: set(range(0, len(s)))}
        self.word_count = 0

    def query_1(self, x: int, y: int, result: []):
        """
        x번 문자와 y번 문자가 같은 문자열에 포함돼 있는지 확인합니다.
        같은 문자열에 포함되어 있으면 "YES"를, 포함되어있지 않으면 "NO"를 result 배열의 뒤에 추가합니다.
        """
        if self.letter_to_word[x] == self.letter_to_word[y]:
            result.append("YES")
        else:
            result.append("NO")

    def query_2(self, x: int, w: str):
        """
        x번 문자가 있는 문자열을 찾습니다. 해당 문자열에서 word에 포함된 알파벳을 모두 새로 생성한 빈 문자열로 옮깁니다.
        """
        word_num = self.letter_to_word[x]
        new_word = []
        target_letters = set(w)
        for alphabet in target_letters:
            intersection = self.alphabet_to_letter_num[alphabet] & self.word_list[word_num]
            self.word_list[word_num] -= intersection
            new_word.extend(intersection)

        if new_word:  # if the there exists a new word
            self.word_count += 1
            for letter_num in new_word:
                self.letter_to_word[letter_num] = self.word_count
            self.word_list[self.word_count] = set(new_word)
            if not self.word_list[word_num]:  # if all letters were removed from existing word
                self.word_list.pop(word_num)

    def query_3(self, x: int, y: int, w: str):
        """
        빈 문자열을 생성한 뒤, x~y번 문자들 중 word에 포함된 알파벳을 모두 새로 생성한 빈 문자열로 옮깁니다.
        """
        target_letters = set(w)
        new_word = []
        for letter_num in range(x, y+1):
            if self.letters[letter_num] in target_letters:
                new_word.append(letter_num)
                word_num = self.letter_to_word[letter_num]
                self.word_list[word_num].remove(letter_num)
                if not self.word_list[word_num]:
                    self.word_list.pop(word_num)
                self.letter_to_word[letter_num] = self.word_count+1

        if new_word:
            self.word_count += 1
            self.word_list[self.word_count] = set(new_word)

    def query_4(self, x: int, y: int):
        """
        x번 문자가 포함된 문자열과 y번 문자가 포함된 문자열을 하나의 문자열로 합칩니다.
        먼저 생성된 문자열에 늦게 생성된 문자열이 합쳐지는 형식으로 먼저 생성된 문자열만 남고 늦게 생성된 문자열은 사라집니다.
        """
        x_word = self.letter_to_word[x]
        y_word = self.letter_to_word[y]

        if x_word == y_word:
            return
        elif x_word < y_word:
            # append y to x
            for letter_num in self.word_list[y_word]:
                self.letter_to_word[letter_num] = x_word
                self.word_list[x_word].add(letter_num)
            self.word_list.pop(y_word)
        else:
            # append x to y
            for letter_num in self.word_list[x_word]:
                self.letter_to_word[letter_num] = y_word
                self.word_list[y_word].add(letter_num)
            self.word_list.pop(x_word)

    def query_5(self, result: []):
        """
        존재하는 모든 문자열에 대해 문자열의 알파벳 구성을 각각 result 배열의 뒤에 추가합니다.
        모든 문자열의 알파벳 구성을 문자열이 먼저 생성된 순으로 result 배열의 뒤에 추가합니다.
        """
        for word_num, letters in self.word_list.items():
            letter_count = {char: 0 for char in string.ascii_lowercase}
            for letter_num in letters:
                letter_count[self.letters[letter_num]] += 1

            result_str = ""
            for letter, count in letter_count.items():
                if count > 0:
                    result_str += letter + ' ' + str(count) + ' '
            result.append(result_str[:-1])


def solution(s: str, query: [str]):
    word_list = WordList(s)
    result = []

    for q in query:
        texts = q.split()
        if texts[0] == '1':
            word_list.query_1(int(texts[1])-1, int(texts[2])-1, result)
        elif texts[0] == '2':
            word_list.query_2(int(texts[1])-1, texts[2])
        elif texts[0] == '3':
            word_list.query_3(int(texts[1])-1, int(texts[2])-1, texts[3])
        elif texts[0] == '4':
            word_list.query_4(int(texts[1])-1, int(texts[2])-1)
        elif texts[0] == '5':
            word_list.query_5(result)

    return result


if __name__ == '__main__':
    print(solution("programmers", ["1 1 5", "2 1 rm", "1 1 5", "5"]))
    # print(solution("abacadae", ["3 1 4 aa", "1 1 5", "4 1 7", "1 1 5", "5"]))
