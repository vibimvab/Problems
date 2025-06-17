from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        answer = []
        for kid in candies:
            answer.append(kid + extraCandies >= max_candies)
        return answer
