from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        multiplied_to_right = [1]
        for n in nums[:-1]:
            multiplied_to_right.append(multiplied_to_right[-1] * n)
        print(multiplied_to_right)

        multiplied_to_left = [1]
        for n in nums[-1:0:-1]:
            multiplied_to_left.append(multiplied_to_left[-1] * n)
        print(multiplied_to_left)

        result = [multiplied_to_right[i] * multiplied_to_left[-1-i] for i in range(len(nums))]
        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        all_multiplied = 1
        zero_count = 0
        zero_idx = -1
        result = [0] * len(nums)
        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
                zero_idx = i
                if zero_count >= 2:
                    return result
                continue
            all_multiplied *= n

        if zero_count == 1:
            result[zero_idx] = all_multiplied
            return result

        return [all_multiplied // n for n in nums]


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf1([1,2,3,4]))
    print(solution.productExceptSelf2([1,2,3,4]))
    print(solution.productExceptSelf2([-1,1,0,-3,3]))