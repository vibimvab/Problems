def maximumSumOfHeights(heights: list[int]) -> int:
        result = -1
        for i in range(len(heights)):
            sum = heights[i]
            left = heights[i]
            right = heights[i]

            for j in range(i-1, -1, -1):
                if heights[j] < left:
                    sum += heights[j]
                    left = heights[j]
                else:
                    sum += left

            for j in range(i+1, len(heights)):
                if heights[j] < right:
                    sum += heights[j]
                    right = heights[j]
                else:
                    sum += right
        
            result = max(result, sum)

        return result


if __name__ == "__main__":
    print(maximumSumOfHeights([5,3,4,1,1]))
    print(maximumSumOfHeights([6,5,3,9,2,7]))
    print(maximumSumOfHeights([3,2,5,5,2,3]))
