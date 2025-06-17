from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_back = 0
        for i, n in enumerate(nums):
            if n:
                nums[non_zero_back] = n
                non_zero_back += 1

        for i in range(1, len(nums) - non_zero_back+1):
            nums[-i] = 0
