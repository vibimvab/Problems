class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        result.reverse()
        return ' '.join(result)
