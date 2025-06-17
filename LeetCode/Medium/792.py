from typing import List
from string import ascii_lowercase


class Solution:
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        next_char = {i: {} for i in range(len(s))}
        next_idx = {}
        for i in range(len(s)-1, -2, -1):
            next_char[i] = next_idx.copy()
            next_idx[s[i]] = i

        count = 0
        for word in words:
            s_idx = -1
            for i, c in enumerate(word):
                s_idx = next_char[s_idx].get(c, -1)
                if s_idx == -1:
                    break

            count += 1 - (s_idx == -1)

        return count

    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        word_list = {c: set() for c in ascii_lowercase}
        for word in words:
            word_list[word[0]].add(word)

        count = 0
        for c in s:
            target = word_list[c]
            word_list[c] = set()
            for word in target:
                if len(word) == 1:
                    count += 1
                else:
                    word_list[word[1]].add(word[1:])

        return count

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return self.numMatchingSubseq2(s, words)


if __name__ == '__main__':
    s = Solution()
    # print(s.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
    print(s.numMatchingSubseq("qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]))
