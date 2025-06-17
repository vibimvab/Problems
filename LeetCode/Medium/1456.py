class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        checker = []
        vowels = set("aeiou")
        count = 0
        for i in range(k):
            if s[i] in vowels:
                checker.append(True)
                count += 1
            else:
                checker.append(False)

        max_count = count
        for i, c in enumerate(s[k:]):
            if c in vowels:
                if not checker[i % k]:
                    checker[i % k] = True
                    count += 1
                    max_count = max(max_count, count)

            else:
                if checker[i % k]:
                    checker[i % k] = False
                    count -= 1

        return max_count
