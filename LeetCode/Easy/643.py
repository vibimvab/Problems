from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for l, r in zip(range(0, len(nums) - k), range(k, len(nums))):
            current_sum += nums[r] - nums[l]
            # max_sum = max(max_sum, current_sum)
            if max_sum < current_sum:
                max_sum = current_sum

        return max_sum / k
