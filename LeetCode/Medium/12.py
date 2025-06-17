class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        # thousands
        q, num = divmod(num, 1000)
        result += 'M'*q

        # hundreds
        q, num = divmod(num, 100)
        if q % 5 != 4:
            q, r = divmod(q, 5)
            result += 'D'*q
            result += 'C'*r
        elif q == 9:
            result += "CM"
        else:
            result += "CD"

        # tens
        q, num = divmod(num, 10)
        if q % 5 != 4:
            q, r = divmod(q, 5)
            result += 'L'*q
            result += 'X'*r
        elif q == 9:
            result += "XC"
        else:
            result += "XL"

        # ones
        if num % 5 != 4:
            q, r = divmod(num, 5)
            result += 'V'*q
            result += 'I'*r
        elif num == 9:
            result += "IX"
        else:
            result += "IV"

        return result
