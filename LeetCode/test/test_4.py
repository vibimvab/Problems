from unittest import TestCase
import p4_find_median_sorted_arrays as p4
import random


class TestSolution(TestCase):
    def test_return_smaller_bigger(self):
        nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 4
        expected = 2, 8, 0, 3, 5
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

        target = 5
        expected = 2, 7, 1, 3, 7
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

        target = 15
        expected = 7, 2, 1, 13, 17
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

    def test_return_smaller_bigger2(self):
        nums = sorted([random.randint(1, 100) for i in range(5000)])
        target = random.randint(1, 100)
        smaller_count, bigger_count, num_same, smaller, bigger = 0, 0, 0, None, None
        for index, num in enumerate(nums):
            if num < target:
                smaller_count = index + 1
                smaller = num
            elif num == target:
                num_same += 1
            elif num > target:
                bigger_count = len(nums) - index
                bigger = num
                break

        expected = smaller_count, bigger_count, num_same, smaller, bigger
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

    def test_return_smaller_bigger3(self):
        nums = sorted([random.randint(0, 10) for i in range(5000)])
        target = random.randint(0, 10)
        smaller_count, bigger_count, num_same, smaller, bigger = 0, 0, 0, None, None
        for index, num in enumerate(nums):
            if num < target:
                smaller_count = index + 1
                smaller = num
            elif num == target:
                num_same += 1
            elif num > target:
                bigger_count = len(nums) - index
                bigger = num
                break

        expected = smaller_count, bigger_count, num_same, smaller, bigger
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

    def test_return_smaller_bigger4(self):
        nums = sorted([random.randint(0, 10000) for i in range(5000)])
        target = random.randint(0, 10000)
        smaller_count, bigger_count, num_same, smaller, bigger = 0, 0, 0, None, None
        for index, num in enumerate(nums):
            if num < target:
                smaller_count = index + 1
                smaller = num
            elif num == target:
                num_same += 1
            elif num > target:
                bigger_count = len(nums) - index
                bigger = num
                break

        expected = smaller_count, bigger_count, num_same, smaller, bigger
        result = p4.Solution.return_smaller_bigger(nums, target)
        self.assertEqual(expected, result)

    def test_find_median_sorted_arrays(self):
        nums1 = [0, 2, 4]
        nums2 = [1, 3]
        expected = 2
        result = p4.Solution.find_median_sorted_arrays(nums1, nums2)
        self.assertEqual(expected, result)

        nums1 = [1, 2, 3]
        nums2 = [8, 9, 10]
        expected = 6
        result = p4.Solution.find_median_sorted_arrays(nums1, nums2)
        self.assertEqual(expected, result)

    # def test_find_median_sorted_arrays2(self):
    #     nums1 = sorted([random.randint(0, 10000) for i in range(500)])
    #     nums2 = sorted([random.randint(0, 10000) for i in range(500)])
    #     combined = nums1 + nums2
    #     combined.sort()
    #     expected = (combined[499] + combined[500]) // 2
    #     result = main.Solution.find_median_sorted_arrays(nums1, nums2)
    #     self.assertEqual(expected, result)
