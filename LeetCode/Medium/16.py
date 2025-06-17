from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # return self.search_third_binary(nums, target)  # slow
        return self.search_two_sum_linear(nums, target)  # fast

    # O(n^2) solution
    def search_two_sum_linear(self, nums: List[int], target: int) -> int:
        nums.sort()  # O(nlog(n))
        sum_three = sum(nums[-3:])
        for i, num in enumerate(nums[:-3]):  # pick the first number
            first_three_sum = sum(nums[i:i+3])
            if first_three_sum > target:  # in this case, further iteration is unnecessary
                if abs(first_three_sum - target) < abs(sum_three - target):
                    sum_three = first_three_sum
                break

            num += self.two_sum(nums[i+1:], target - num)  # add two sum from the remaining list

            if num == target:
                return target

            if abs(num - target) < abs(sum_three - target):
                sum_three = num

        return sum_three

    @staticmethod
    def two_sum(nums: List[int], target: int) -> int:
        """
        Definition:
            nums = a_1, a_2, ..., a_n
            a_i <= a_j if i < j

        Bellman Equation:
            Case 1: a_1 + a_2   if n == 2 (base case)
            Case 2: closer_to_target(a_1 + a_2, two_sum(a_1, ..., a_n-1))
            Case 3: closer_to_target(a_1 + a_2, two_sum(a_2, ..., a_n))

        Proof by Induction:
            two_sum is true for the base case: n = 2
            Suppose two_sum returns optimal solution, or the closest sum of pairs to the target,
            for the following sub-arrays: a_1, ..., a_n-1 and a_2, ..., a_n (weak induction).
            When a_1 + a_n < target, a_1 cannot be paired with any other element a_k, k < n to form closer sum to the
            target since a_1 + a_k <= a_1 + a_n < target. This let us safely ignore other pairs containing a_1.
            Therefore, comparing a_1 + a_n and two_sum(a_2, ..., a_n) yields the optimal solution.
            The same logic applies for the case a_1 + a_n > target.

        Time Complexity:
            O(n)
        """
        left = 0
        right = len(nums)-1
        closest_sum = nums[left] + nums[right]
        while left < right:
            sum_ends = nums[left] + nums[right]
            if abs(sum_ends - target) < abs(closest_sum - target):
                closest_sum = sum_ends

            if sum_ends < target:
                left += 1
            else:
                right -= 1

        return closest_sum

    def two_sum_recursive(self, nums: List[int], target: int) -> int:
        # still O(n) but slow compared to the alternative above
        # base case
        length = len(nums)
        if length == 2:
            return sum(nums)
        elif length < 2:
            raise RuntimeError("two_sum got nums with length < 2")

        sum_ends = nums[0] + nums[-1]
        if sum_ends > target:
            sub_result = self.two_sum_recursive(nums[:-1], target)
        elif sum_ends < target:
            sub_result = self.two_sum_recursive(nums[1:], target)
        else:
            return target

        if abs(sub_result - target) < abs(sum_ends - target):
            return sub_result
        else:
            return sum_ends

    # O(n^2log(n)) solution
    def search_third_binary(self, nums: List[int], target: int) -> int:
        # for every pair, binary search the third
        nums.sort()
        diff = sum(nums[-3:]) - target
        for i, first in enumerate(nums[:-3]):
            for j, second in enumerate(nums[i+1:-1]):
                third = self.find_nearest(nums[i+j+2:], target - first - second)
                three_diff = first + second + third - target
                if abs(three_diff) < abs(diff):
                    diff = three_diff

                if first + second + nums[i+j+2] - target >= 0:
                    break

        return diff + target

    @staticmethod
    def find_nearest(nums: List[int], target: int) -> int:
        begin = 1
        end = len(nums) - 2
        closest_lower = nums[0]
        closest_higher = nums[-1]
        while begin <= end:
            i = (begin + end) // 2
            if nums[i] > target:
                closest_higher = nums[i]
                end = i - 1
            else:
                closest_lower = nums[i]
                begin = i + 1

        return closest_higher if abs(closest_higher - target) < abs(closest_lower - target) else closest_lower


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([1,1,1,0], -100))
    # print(s.threeSumClosest([0,0,0], 1))
    # print(s.threeSumClosest([0,3,97,102,200], 300))
    # print(s.threeSumClosest([1,3,4,7,8,9], 15))
    # edge_case = [13,252,-87,-431,-148,387,-290,572,-311,-721,222,673,538,919,483,-128,-518,7,-36,-840,233,-184,-541,522,-162,127,-935,-397,761,903,-217,543,906,-503,-826,-342,599,-726,960,-235,436,-91,-511,-793,-658,-143,-524,-609,-728,-734,273,-19,-10,630,-294,-453,149,-581,-405,984,154,-968,623,-631,384,-825,308,779,-7,617,221,394,151,-282,472,332,-5,-509,611,-116,113,672,-497,-182,307,-592,925,766,-62,237,-8,789,318,-314,-792,-632,-781,375,939,-304,-149,544,-742,663,484,802,616,501,-269,-458,-763,-950,-390,-816,683,-219,381,478,-129,602,-931,128,502,508,-565,-243,-695,-943,-987,-692,346,-13,-225,-740,-441,-112,658,855,-531,542,839,795,-664,404,-844,-164,-709,167,953,-941,-848,211,-75,792,-208,569,-647,-714,-76,-603,-852,-665,-897,-627,123,-177,-35,-519,-241,-711,-74,420,-2,-101,715,708,256,-307,466,-602,-636,990,857,70,590,-4,610,-151,196,-981,385,-689,-617,827,360,-959,-289,620,933,-522,597,-667,-882,524,181,-854,275,-600,453,-942,134]
    # print(s.threeSumClosest(edge_case, -2805))
    # print(s.threeSumClosest([2, 5, 6, 7], 16))
    # print(s.threeSumClosest([-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38], 78))
