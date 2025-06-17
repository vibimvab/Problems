class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            temp = str1
            str1 = str2
            str2 = temp

        divisors = {}
        for i in range(len(str1)):
            div_l = i + 1
            if len(str1) % div_l == 0 and div_l not in divisors:
                div_s = str1[:div_l]
                quotient = len(str1) // div_l
                for j in range(quotient):
                    # s = str1[div_l * j: div_l * j + div_l]
                    if str1[div_l * j: div_l * j + div_l] != div_s:
                        break
                else:
                    divisors[div_l] = div_s
                    k = 2
                    while div_l * k <= len(str1):
                        if len(str1) // (div_l * k) == 0:
                            divisors[i * k] = divisors[i] * k
                        k += 1

        divisors = dict(sorted(divisors.items(), reverse=True))
        for div_l, div_s in divisors.items():
            if len(str2) % div_l == 0:
                quotient = len(str2) // div_l
                for j in range(quotient):
                    # s = str2[div_l * j: div_l * j + div_l]
                    if str2[div_l * j: div_l * j + div_l] != div_s:
                        break
                else:
                    return div_s

        return ""

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        for div_l in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % div_l == 0 and len(str2) % div_l == 0:
                flag = False
                for q in range(len(str1) // div_l):
                    if str1[q * div_l:q * div_l + div_l] != str1[:div_l]:
                        flag = True
                        break
                if flag:
                    break
                for q in range(len(str2) // div_l):
                    if str2[q * div_l:q * div_l + div_l] != str1[:div_l]:
                        flag = True
                        break
                if flag:
                    break

                return str1[:div_l]
        return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return self.gcdOfStrings2(str1, str2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.gcdOfStrings("ABCABC", "ABC"))
    print(solution.gcdOfStrings("ABABAB", "ABAB"))
    print(solution.gcdOfStrings("ABAABA", "ABAB"))
    print(solution.gcdOfStrings("AAAAAA", "AAAA"))
