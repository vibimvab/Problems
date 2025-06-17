from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flipped = 0
        max_count = 0
        for i, n in enumerate(nums):
            if not n:
                if flipped < k:
                    flipped += 1
                else:
                    max_count = max(max_count, i - left)
                    while nums[left]:
                        left += 1
                    left += 1
        max_count = max(max_count, len(nums) - left)

        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(s.longestOnes([0,0,1,1,1,0,0], 0))
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1], 0))
