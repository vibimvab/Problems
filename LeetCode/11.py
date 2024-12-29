def maxArea(heights: [int]) -> int:
    # size = 0
    size_list = []
    length = len(heights)

    flag_start_height = -1
    for start_pos, start_height in enumerate(heights):
        if flag_start_height < start_height:
            flag_start_height = start_height
        else:
            continue

        flag_end_height = -1
        for end_pos, end_height in enumerate(heights[-1:start_pos:-1]):
            if end_height >= start_height:
                size_list.append(start_height * (length - start_pos - end_pos - 1))
                break

            elif end_height > flag_end_height:
                flag_end_height = end_height
                size_list.append(end_height * (length - start_pos - end_pos - 1))

    return max(size_list)


if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea(range(10000)+range(9999, 0, -1)))
