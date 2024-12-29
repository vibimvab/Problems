class Solution:
    @staticmethod
    def return_smaller_bigger(nums: [], target):
        # using binary search: O(log(m))
        # return 작은 수 개수, 큰 수 개수, 같은 수 개수, 다음 작은 수, 다음 큰 수 (int 5개)
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

            else:  # nums[mid] == target
                # 작은거 개수 찾기
                smaller_end = mid - 1
                while start <= smaller_end:
                    smaller_mid = (start + smaller_end) // 2
                    if nums[smaller_mid] == target:
                        smaller_end = smaller_mid - 1
                    else:
                        start = smaller_mid + 1

                # 큰거 개수 찾기
                bigger_start = mid + 1
                while bigger_start <= end:
                    bigger_mid = (bigger_start + end) // 2
                    if nums[bigger_mid] == target:
                        bigger_start = bigger_mid + 1
                    else:
                        end = bigger_mid - 1

                return start, len(nums) - bigger_start, bigger_start - start, \
                    nums[smaller_end] if not smaller_end == -1 else None, \
                    nums[bigger_start] if not bigger_start == len(nums) else None

        return start, len(nums) - start, 0, \
            nums[end] if not end == -1 else None, nums[start] if not start == len(nums) else None

    @staticmethod
    def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
        nums1_start = 0
        num1_end = len(nums1) - 1
        nums1_mid = (nums1_start + num1_end) // 2

        while True:
            nums1_smaller = nums1[nums1_mid - 1] if not nums1_mid <= 0 else None
            nums1_bigger = nums1[nums1_mid + 1] if not nums1_mid >= len(nums1) - 1 else None
            nums1_smaller_count, nums1_bigger_count = nums1_mid, len(nums1) - nums1_mid - 1

            nums2_smaller_count, nums2_bigger_count, nums2_same, nums2_smaller, nums2_bigger \
                = Solution.return_smaller_bigger(nums2, nums1[nums1_mid])

            smaller_bigger_comp = nums1_smaller_count + nums2_smaller_count - (nums1_bigger_count + nums2_bigger_count)
            if smaller_bigger_comp < -nums2_same - 1:  # bigger 더 많음, smaller_bigger_comp 음수
                nums1_mid = nums1_mid - (smaller_bigger_comp + 1) // 2
                # if nums1_mid >= len(nums1):
                #     return nums2[]

            elif smaller_bigger_comp > nums2_same + 1:  # smaller 더 많음, smaller_bigger_comp 양수
                nums1_mid = nums1_mid - (smaller_bigger_comp - 1) // 2
                # if nums1_mid < 0:
                #     return nums2[]

            elif abs(smaller_bigger_comp) <= nums2_same:
                return nums1[nums1_mid]
            elif smaller_bigger_comp == nums2_same + 1:
                return (nums1[nums1_mid] + max(nums1_smaller, nums2_smaller)) / 2
            elif smaller_bigger_comp == -nums2_same - 1:
                return (nums1[nums1_mid] + min(nums1_bigger, nums2_bigger)) / 2
