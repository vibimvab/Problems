def find_box_position(w, num) -> (int, int):
    """
    :param w: width
    :param num: box number
    :return: column number (1 indexed), height
    """
    q, r = divmod(num, (w * 2))
    q *= 2
    wrapped, r = divmod(r, w)
    q += wrapped

    if r == 0:
        # when r == 0, wrapped is 1 when top right corner, 0 when top left corner
        if wrapped == 1:
            return w, q
        else:
            return 1, q
    else:
        if wrapped == 0:
            return r, q + 1
        else:
            return w - r + 1, q + 1


def find_boxes_above(n, w, box_column, box_height):
    stack_height, r = divmod(n, (w * 2))
    stack_height *= 2
    wrapped, r = divmod(r, w)
    stack_height += wrapped

    if r == 0:
        return stack_height - box_height + 1
    else:
        if wrapped == 0:
            if box_column > r:
                return stack_height - box_height + 1
            else:
                return stack_height - box_height + 2
        else:
            if box_column > w-r:
                return stack_height - box_height + 2
            else:
                return stack_height - box_height + 1


def solution(n, w, num):
    box_column, box_height = find_box_position(w, num)
    answer = find_boxes_above(n, w, box_column, box_height)
    return answer


if __name__ == '__main__':
    print(solution(22, 6, 8))
    print(solution(13, 3, 6))
