def isArithmetic(nums: list[int]) -> bool:
    nums.sort()
    diff = nums[1] - nums[0]
    for i in range(1, len(nums)-1):
        if nums[i+1] - nums[i] != diff:
            return False
        
    return True
        
    
def checkArithmeticSubarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    answer = []
    for i in range(len(l)):
        answer.append(isArithmetic(nums[l[i]: r[i] + 1]))

    return answer

if __name__ == '__main__':
    print(checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
    print(checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))