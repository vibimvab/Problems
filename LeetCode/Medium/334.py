from typing import List


class Solution:
    def increasingTriplet1(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, first in enumerate(nums):
            for j in range(i + 1, n):
                if nums[j] <= first:
                    break

                second = nums[j]
                for k in range(j + 1, n):
                    if second < nums[k]:
                        print(first, second, nums[k])
                        return True
                    elif nums[k] > first:
                        second = nums[k]
                break

        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        layers = []
        for n in nums:
            flag = False
            for i, layer in enumerate(layers):
                if layer >= n:
                    layers[i] = n
                    flag = True
                    break

            if flag:
                continue

            layers.append(n)
            if len(layers) >= 3:
                return True
        return False

    def increasingTriplet3(self, nums: List[int]) -> bool:
        layers = [nums[0], float('inf')]
        for n in nums:
            if layers[0] >= n:
                layers[0] = n
            elif layers[1] >= n:
                layers[1] = n
            else:
                return True

        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.increasingTriplet2(nums)



if __name__ == "__main__":
    solution = Solution()
    # print(solution.increasingTriplet([1,2,3,4,5]))
    # print(solution.increasingTriplet([5,4,3,2,1]))
    # print(solution.increasingTriplet([2,1,5,0,4,6]))
    # print(solution.increasingTriplet([6,7,1,2]))
    print(solution.increasingTriplet([1] * 100))
