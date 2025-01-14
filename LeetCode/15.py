from typing import List


class Solution:
    # time complexity: O(n^2)
    # O(n) pre-processing + O(n*log(n)) sorting + O(n^2) iterating first and second number * O(1) finding third number

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n) pre-processing
        num_count = {}
        for num in nums:
            try:
                num_count[num] += 1
            except KeyError:
                num_count[num] = 1

        # special case where all three numbers can be the same
        result = []
        try:
            if num_count[0] >= 3:
                result.append([0,0,0])
        except KeyError:
            pass

        # key: first number, value: sets of the second numbers
        # no need to keep track of third number since it's determined by first and second.
        duplicate = {0: {0}}
        nums.sort()
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i+1:]):
                third = 0-first-second
                if third < second:
                    break

                if third not in num_count.keys():
                    continue

                if second == third:
                    if num_count[third] >= 2:
                        try:
                            if second not in duplicate[first]:
                                duplicate[first].add(second)
                                result.append([first, second, third])
                        except KeyError:
                            duplicate[first] = {second}
                            result.append([first, second, third])
                else:
                    try:
                        if second not in duplicate[first]:
                            duplicate[first].add(second)
                            result.append([first, second, third])
                    except KeyError:
                        duplicate[first] = {second}
                        result.append([first, second, third])

            if first >= 0:
                break

        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.threeSum([-1,0,1,2,-1,-4]))
    # print(s.threeSum([0,0,0,0]))
    print(s.threeSum([1,1,-2]))
