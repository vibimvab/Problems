from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            try:
                if i != d[num]:
                    return i, d[num]
            except KeyError:
                pass

            d[target - num] = i