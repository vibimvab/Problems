import string


class Letter:
    def __init__(self, num, c, belongs=None):
        self._num = num
        self._belongs: Word = belongs
        self._char = c

    def set_belongs(self, belongs):
        self._belongs = belongs

    def belongs(self):
        return self._belongs

    def get_word_num(self):
        return self._belongs.get_num()

    def get_num(self):
        return self._num

    def get_char(self):
        return self._char


class Word:
    def __init__(self, s: [Letter], num: int):
        self._letters: [Letter] = s.copy()
        self._num = num
        for letter in self._letters:
            letter.set_belongs(self)

    def get_letters(self):
        return self._letters

    def get_num(self):
        return self._num

    def set_num(self, n):
        self._num = n

    def is_empty(self):
        return not self._letters

    def remove_letters(self, t: str, new_word_num: int):
        # query 2
        target_set = set(t)

        new_letters = []
        return_letters = []
        for letter in self._letters:
            if letter.get_char() in target_set:
                return_letters.append(letter)
            else:
                new_letters.append(letter)

        self._letters = new_letters
        new_word = Word(return_letters, new_word_num)
        return new_word

    def remove_one_letter(self, letter_i):
        # query 3
        # find index
        index = next(i for i, x in enumerate(self._letters) if x.get_num() == letter_i)
        # pop the element
        self._letters.pop(index)

    def extend_word(self, w: [Letter]):
        # query 4
        self._letters.extend(w)
        for letter in w:
            letter.set_belongs(self)

    def add_letters(self, result):
        # query 5
        letter_count = {char: 0 for char in string.ascii_lowercase}
        for letter in self._letters:
            letter_count[letter.get_char()] += 1

        result_str = ""
        for letter, count in letter_count.items():
            if count > 0:
                result_str += letter + ' ' + str(count) + ' '
        result.append(result_str[:-1])


class WordList:
    def __init__(self, s: str):
        self.letter_list: [Letter] = []
        for i, c in enumerate(s):
            self.letter_list.append(Letter(i+1, c, None))
        self.word_list: [Word] = []
        self.word_list.append(Word(self.letter_list, 1))

    def query_1(self, x: int, y: int, result: []):
        """
        x번 문자와 y번 문자가 같은 문자열에 포함돼 있는지 확인합니다.
        같은 문자열에 포함되어 있으면 "YES"를, 포함되어있지 않으면 "NO"를 result 배열의 뒤에 추가합니다.
        """
        if self.letter_list[x-1].get_word_num() == self.letter_list[y-1].get_word_num():
            result.append("YES")
        else:
            result.append("NO")

    def query_2(self, x: int, w: str):
        """
        x번 문자가 있는 문자열을 찾습니다. 해당 문자열에서 word에 포함된 알파벳을 모두 새로 생성한 빈 문자열로 옮깁니다.
        """
        word_num = self.letter_list[x-1].get_word_num()
        self.word_list.append(self.word_list[word_num-1].remove_letters(w, len(self.word_list)+1))

        if self.word_list[-1].is_empty():
            self.word_list.pop()

        elif self.word_list[word_num-1].is_empty():
            self.word_list.pop(word_num-1)
            # update word numbers
            for i, word in enumerate(self.word_list[word_num-1:]):
                word.set_num(i+1)

    def query_3(self, x: int, y: int, w: str):
        """
        빈 문자열을 생성한 뒤, x~y번 문자들 중 word에 포함된 알파벳을 모두 새로 생성한 빈 문자열로 옮깁니다.
        """
        target_set = set(w)
        new_word = []
        empty_words = []
        for i in range(x, y+1):
            if self.letter_list[i-1].get_char() in target_set:
                new_word.append(self.letter_list[i-1])
                self.letter_list[i-1].belongs().remove_one_letter(i)
                if self.word_list[self.letter_list[i-1].get_word_num()-1].is_empty():
                    empty_words.append(self.letter_list[i-1].get_word_num()-1)
        self.word_list.append(Word(new_word, len(self.word_list)+1))

        if self.word_list[-1].is_empty():
            self.word_list.pop()
        elif not empty_words:
            for i in sorted(empty_words, reverse=True):
                self.word_list.pop(i)
            for i, word in enumerate(self.word_list):
                word.set_num(i+1)

    def query_4(self, x: int, y: int):
        """
        x번 문자가 포함된 문자열과 y번 문자가 포함된 문자열을 하나의 문자열로 합칩니다.
        먼저 생성된 문자열에 늦게 생성된 문자열이 합쳐지는 형식으로 먼저 생성된 문자열만 남고 늦게 생성된 문자열은 사라집니다.
        """
        x_word = self.letter_list[x-1].get_word_num()
        y_word = self.letter_list[y-1].get_word_num()

        if x_word == y_word:
            return
        elif x_word < y_word:
            # append y to x
            self.word_list[x_word-1].extend_word(self.word_list[y_word-1].get_letters())
            self.word_list.pop(y_word-1)
        else:
            # append x to y
            self.word_list[y_word-1].extend_word(self.word_list[x_word-1].get_letters())
            self.word_list.pop(x_word-1)

        # update word numbers
        for i, word in enumerate(self.word_list):
            word.set_num(i+1)

    def query_5(self, result: []):
        """
        존재하는 모든 문자열에 대해 문자열의 알파벳 구성을 각각 result 배열의 뒤에 추가합니다.
        모든 문자열의 알파벳 구성을 문자열이 먼저 생성된 순으로 result 배열의 뒤에 추가합니다.
        """
        for word in self.word_list:
            word.add_letters(result)


def solution(s: str, query: [str]):
    word_list = WordList(s)
    result = []

    for q in query:
        texts = q.split()
        if texts[0] == '1':
            word_list.query_1(int(texts[1]), int(texts[2]), result)
        elif texts[0] == '2':
            word_list.query_2(int(texts[1]), texts[2])
        elif texts[0] == '3':
            word_list.query_3(int(texts[1]), int(texts[2]), texts[3])
        elif texts[0] == '4':
            word_list.query_4(int(texts[1]), int(texts[2]))
        elif texts[0] == '5':
            word_list.query_5(result)

    return result


if __name__ == '__main__':
    print(solution("qwertyuiopasdfghjklzxcvbnm" * 4, [
        "2 1 zxc",
        "3 5 40 rty",


        # "3 10 50 opm",
        # "4 8 18",
        "1 7 80",
        "5"
    ]))

    print(solution("abcdef" * 50, [
        # "1 10 20",
        "2 3 ac",
        "3 50 100 bd",
        # "1 30 200",
        "4 10 15",
        # "1 1 300",
        "2 25 fe",
        "3 100 250 de",
        "4 20 80",

        "1 60 150",
        "2 5 ab",
        "3 30 70 cd",
        "4 2 10",
        "1 1 150",
        "2 15 bc",
        "3 40 90 ef",
        "4 5 20",
        "1 10 300",
        "2 50 ab",
        "5"
    ]))

    # print(solution("zxy" * 40, [
    #     "1 1 60",
    #     "2 10 zx",
    #     "3 5 100 y",
    #     "4 2 15",
    #     "1 3 80",
    #     "2 20 xy",
    #     "3 10 90 zx",
    #     "4 5 30",
    #     "1 1 120",
    #     "2 15 zy",
    #     "3 2 50 x",
    #     "4 8 40",
    #     "1 20 70",
    #     "2 30 zy",
    #     "5"
    # ]))
