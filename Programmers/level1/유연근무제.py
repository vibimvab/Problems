def solution(schedules, timelogs, startday):
    answer = 0
    # 각 사람마다
    for person, schedule in enumerate(schedules):
        # 출근 인정 시간 계산
        schedule_hour, schedule_min = divmod(schedule+10, 100)
        schedule_hour += schedule_min // 60
        schedule_min %= 60

        # 출근 시간 체크
        for day, timelog in enumerate(timelogs[person]):
            if (startday + day + 1) % 7 < 2:  # 토/일 체크
                continue

            hour, minute = divmod(timelog, 100)
            if hour >= schedule_hour and (hour != schedule_hour or minute > schedule_min):
                break  # 지각
        else:
            answer += 1  # 한주간 잘 출근했다면 (break 없이 for 문 통과)

    return answer


if __name__ == '__main__':
    print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
    print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))