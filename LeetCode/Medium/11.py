from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return self.maxArea_bf(heights)
        return self.maxArea_greedy(heights)

    def maxArea_greedy(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1

        area = []
        while left < right:
            area.append((right - left) * min(heights[left], heights[right]))
            if left < right:
                left += 1
            else:
                right -= 1

        return max(area)

    def maxArea_bf(self, heights: List[int]) -> int:
        # brute force solution
        n = len(heights)
        max_water = 0
        left_prev = 0

        for left, left_h in enumerate(heights):
            if left_h <= left_prev:
                continue

            right_h = 0
            water = [0]
            for right in range(n - 1, left - 1, -1):
                if right_h < heights[right]:
                    right_h = heights[right]

                    if right_h < left_h:
                        water.append((right - left) * right_h)
                    else:
                        water.append((right - left) * left_h)
                        break

            max_water = max(max_water, max(water))

        return max_water


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea(list(range(10000)) + list(range(9999, 0, -1))))
    print(s.maxArea([2, 0]))
    print(s.maxArea([1, 1]))
