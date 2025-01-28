import time
from typing import List, Dict
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Solution:
    combinations: Dict[int, Dict[int, List[int]]] = {}
    result: List[List[int]] = []

    def add_combination(self, a: List[int]):
        """
        param a: a list of four integers
        time complexity: O(1)

        add a new combination to result if there is no duplicate combination already
        """
        a.sort()
        try:
            if a[2] not in self.combinations[a[0]][a[1]]:
                self.combinations[a[0]][a[1]].append(a[2])
            else:
                return
        except KeyError:
            try:
                self.combinations[a[0]][a[1]] = [a[2]]
            except KeyError:
                self.combinations[a[0]] = {a[1]: [a[2]]}

        self.result.append(a)

    @staticmethod
    def is_valid(a, b, c, d):
        # check if no pair in the four integers have the same index
        return not (a == c or a == d or b == c or b == d)

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        fourSum1 and fourSum2 are essentially the same algorithm with different data structures for complement_pairs.
        fourSum1 uses more complex data structure to optimize the second part's running time when there is a lot of
        duplicate numbers. Experimental running time analysis showed that the fourSum1 is much faster than fourSum2 with
        random input.

        Experimental analysis with random inputs shows that the time complexity of the algorithms are close to O(n^3)
        My intuition is that the time complexity of the second part is O(n^2 + k) where k is the number of output.
        When the numbers are distributed sparsely, it will be close to O(n^2)
        """
        self.combinations = {}
        self.result = []
        complement_pairs: Dict[int, Dict[int, List[List[int]]]] = {}
        nums.sort()

        # first part: construct complement_pairs
        # time complexity: O(n^2)
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i + 1:]):
                c = target - first - second
                try:
                    complement_pairs[c][first].append([i, i+j+1])
                except KeyError:
                    try:
                        complement_pairs[c][first] = [[i, i+j+1]]
                    except KeyError:
                        complement_pairs[c] = {first: [[i, i+j+1]]}

        # second part.
        # time complexity: unknown, my intuition is O(n^2+k)
        # these prevs are to skip some iterations when there are a lot of duplicate numbers
        # it is unnecessary if there are not much duplicate numbers in nums. probably even sorting is unnecessary.
        prev_1 = nums[0] - 1
        prev_2 = nums[0] - 1
        for i, third in enumerate(nums[2:]):
            if third == prev_1:
                continue
            for j, fourth in enumerate(nums[i + 3:]):
                if fourth == prev_2:
                    continue
                try:
                    complements = complement_pairs[third + fourth]
                    for first, pairs in complements.items():
                        for k, l in pairs:
                            if self.is_valid(i+2, i+j+3, k, l):
                                # if no pair in the four integers has the same index
                                self.add_combination([nums[k], nums[l], third, fourth])
                                break
                except KeyError:
                    pass
                prev_2 = fourth
            prev_1 = third
            prev_2 = nums[0] - 1

        return self.result

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.combinations = {}
        self.result = []
        complement_pairs: Dict[int, List[List[int]]] = {}
        nums.sort()
        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i + 1:]):
                try:
                    complement_pairs[target - first - second].append([i, i + j + 1])
                except KeyError:
                    complement_pairs[target - first - second] = [[i, i + j + 1]]

        # these prevs are to skip some iterations when there are a lot of duplicate numbers
        # it is unnecessary if there are not much duplicate numbers in nums. probably even sorting is unnecessary.
        prev_1 = nums[0] - 1
        prev_2 = nums[0] - 1
        for i, third in enumerate(nums[2:]):
            if third == prev_1:
                continue
            for j, fourth in enumerate(nums[i + 3:]):
                if fourth == prev_2:
                    continue
                try:
                    other_pairs = complement_pairs[third + fourth]
                    for other_pair in other_pairs:
                        if self.is_valid(i + 2, i + j + 3, other_pair[0], other_pair[1]):
                            self.add_combination([nums[other_pair[0]], nums[other_pair[1]], third, fourth])
                except KeyError:
                    pass
                prev_2 = fourth
            prev_1 = third
            prev_2 = nums[0] - 1

        return self.result


if __name__ == '__main__':
    s = Solution()
    # print(s.fourSum1([1, 0, -1, 0, -2, 2], 0))
    # print(s.fourSum1([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 8))
    # print(s.fourSum1([0,1,5,0,1,5,5,-4], 11))
    # print(s.fourSum2([1, 0, -1, 0, -2, 2], 0))
    # print(s.fourSum2([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 8))
    # print(s.fourSum2([0,1,5,0,1,5,5,-4], 11))

    num_tests = 10
    t = 0

    x = np.array([n for n in range(100, 2001, 100)])
    alg1_runtime = []
    alg2_runtime = []

    for i, n in enumerate(x):
        test_cases = [[random.randint(-n//5, n//5) for _ in range(n)] for _ in range(num_tests)]
        print(f"n = {n}")
        # test_cases = [[2]*n]

        start = time.time()
        for test_case in test_cases:
            s.fourSum1(test_case, t)
        end = time.time()
        alg1_runtime.append((end - start)/num_tests)

        # start = time.time()
        # for test_case in test_cases:
        #     s.fourSum2(test_case, t)
        # end = time.time()
        # alg2_runtime.append((end - start)/num_tests)

    alg1_runtime = np.array(alg1_runtime)
    plt.plot(x, alg1_runtime, label="1")
    # alg2_runtime = np.array(alg2_runtime)
    # plt.plot(x, alg2_runtime, label="2")

    coefficients_deg_2 = np.polyfit(x, alg1_runtime, 2)
    coefficients_deg_3 = np.polyfit(x, alg1_runtime, 3)
    y_fit_deg_2 = np.polyval(coefficients_deg_2, x)
    y_fit_deg_3 = np.polyval(coefficients_deg_3, x)
    plt.plot(x, y_fit_deg_2, label="degree 2")
    plt.plot(x, y_fit_deg_3, label="degree 3")

    # coefficients_2 = np.polyfit(x, alg2_runtime, 2)
    # y_fit_2 = np.polyval(coefficients_2, x)
    # plt.plot(x, y_fit_2, label="fit 2")

    plt.legend()
    plt.show()
