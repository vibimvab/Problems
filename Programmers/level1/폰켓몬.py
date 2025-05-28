def solution(nums):
    counted = set()
    count = 0
    for num in nums:
        if num not in counted:
            counted.add(num)
            count += 1

    return min(count, len(nums) // 2)
