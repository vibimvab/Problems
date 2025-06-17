from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        return self.maxOperations2(nums, k)


    def maxOperations1(self, nums: List[int], k: int) -> int:
        candidates = {}
        count = 0
        for n in nums:
            if candidates.get(n, 0) > 0:
                candidates[n] -= 1
                count += 1
            else:
                candidates[k - n] = candidates.get(k - n, 0) + 1

        return count

    def maxOperations2(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        answer = 0
        for n in counter:
            if k - n in counter:
                if n << 1 == k:
                    answer += counter[n] // 2
                else:
                    answer += min(counter[n], counter[k-n]) / 2

        return int(answer)


if __name__ == '__main__':
    s = Solution()
    # print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([2,2,2,3,1,1,4,1], 4))
