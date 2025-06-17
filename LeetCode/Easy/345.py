class Solution:
    def reverseVowels1(self, s: str) -> str:
        vowels = []
        for c in s:
            if c in "aeiouAEIOU":
                vowels.append(c)

        j = -1
        result = ""
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                result += vowels[j]
                j -= 1
            else:
                result += c

        return ''.join(result)


    def reverseVowels2(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        i = 0
        j = len(s) - 1
        result = list(s)
        while i < j:
            if s[i] in vowels:
                if s[j] in vowels:
                    result[i] = s[j]
                    result[j] = s[i]
                    i += 1
                j -= 1
            else:
                i += 1

        return ''.join(result)
