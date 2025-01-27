class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     s_index = 0
    #     p_index = 0
    #     preceding = ''
    #     while s_index < len(s) and p_index < len(p):
    #         try:
    #             star = p[p_index+1] == '*'
    #         except IndexError:
    #             return True if s[s_index] == '.' else s[s_index] == p[p_index]
    #
    #         if not star:
    #             if s[s_index] == '.' or s[s_index] == p[p_index]:
    #                 s_index += 1
    #                 p_index += 1
    #                 continue
    #
    #             else:
    #                 return False
    #
    #         else:
    #             preceding = p[p_index]
    #             if preceding == '.':

    def isMatch_recursive(self, s: str, p: str) -> bool:
        """
        apparently, quite slow.
        can be better with optimizing .* part though
        """
        # find first index of '*'
        star = p.find('*')

        # if there is no '*' in p
        if star == -1:
            if len(s) != len(p):
                return False

            for i in range(len(s)):
                if p[i] == '.':
                    continue

                if s[i] != p[i]:
                    return False

            return True

        # if there is a star
        # check until the star
        index = 0  # index of s to check
        while index < star-1:
            if index >= len(s):
                return False

            if p[index] == '.':
                index += 1
                continue

            if s[index] != p[index]:
                return False

            index += 1

        # if remaining s is an empty string
        if index >= len(s):
            return self.isMatch('', p[star+1:])

        # if '*' is at the end of the p
        preceding = p[star-1]
        if star == len(p)-1:
            if preceding == '.':
                return True

            while index < len(s):
                if s[index] != preceding:
                    return False
                index += 1

            return True

        # if '*' is not at the end of the p
        # and if preceding is '.'
        if preceding == '.':
            occurrences = range(index, len(s)+1)

            for occurrence in occurrences[::-1]:
                if self.isMatch(s[occurrence:], p[star + 1:]):
                    return True

            return False

        # if preceding is not '.'
        occurrences = [star-1]
        while index < len(s):
            if s[index] == preceding:
                occurrences.append(index+1)
            else:
                break
            index += 1

        for occurrence in occurrences[::-1]:
            if self.isMatch(s[occurrence:], p[star+1:]):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch("aab", "c*a*b"), "True")
    # print(s.isMatch("aa", "a*"), "True")
    # print(s.isMatch("ab", ".*"), "True")
    # print(s.isMatch("ab", ".*c"), "False")
    # print(s.isMatch("aaa", "aaaa"), "False")
    # print(s.isMatch("a", "ab*"), "True")
    # print(s.isMatch("a", "ab*a"), "False")
    # print(s.isMatch("bbbba", ".*a*a"), "True")
    # print(s.isMatch("a", ".*..a*"), "False")
    # print(s.isMatch("abcdede", "ab.*de"), "True")
    # print(s.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"), "True")
    print(s.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"), "True")
    print(s.isMatch("ac", ".*a*"), "True")
