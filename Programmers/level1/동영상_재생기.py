def solution(video_len, pos, op_start, op_end, commands):
    video_len = [int(n) for n in video_len.split(':')]
    pos = [int(n) for n in pos.split(':')]
    op_start = [int(n) for n in op_start.split(':')]
    op_end = [int(n) for n in op_end.split(':')]

    if op_start < pos < op_end:
        pos = op_end.copy()

    for command in commands:
        match command:
            case 'next':
                pos[0] += (pos[1] + 10) // 60
                pos[1] = (pos[1] + 10) % 60
            case 'prev':
                pos[0] -= (pos[1] - 10) < 0
                pos[1] = (pos[1] + 50) % 60

        if pos < [0, 0]:
            pos = [0, 0]
        elif pos > video_len:
            pos = video_len
        if op_start <= pos < op_end:
            pos = op_end.copy()

    pos = [str(n) for n in pos]
    for i in range(2):
        if len(pos[i]) < 2:
            pos[i] = f"0{pos[i]}"

    return ':'.join(pos)


if __name__ == '__main__':
    # print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
    # print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
    print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
