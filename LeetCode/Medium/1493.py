from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        remove_idx = -1
        max_count = 0
        for i, n in enumerate(nums):
            if not n:
                if remove_idx != -1:
                    max_count = max(max_count, i - left - 1)
                    left = remove_idx + 1
                remove_idx = i
        max_count = max(max_count, len(nums) - left - 1)

        return max_count - (remove_idx == -1)


if __name__ == '__main__':
    s = Solution()
    # print(s.longestSubarray([1,1,0,1]))
    print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))