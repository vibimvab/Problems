from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_length = 1
        for flower in flowerbed:
            if flower:
                n -= (empty_length - 1) // 2
                if n <= 0:
                    return True
                empty_length = 0
            else:
                empty_length += 1

        n -= empty_length // 2

        return n <= 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([1,0,0,0,1], 1))
