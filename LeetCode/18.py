from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # removing duplicate items: O(n)
        num_set = set(nums)
        nums = list(num_set)

        result = []
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i+1:]):
                for k, third in enumerate(nums[i+j+2:]):
                    fourth = target - first - second - third
                    if fourth in num_set and fourth != first and fourth != second and fourth != third:
                        result.append([first, second, third, fourth])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))
