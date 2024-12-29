import random
import time
import sys

# Gets length of the list from user, generates a random list with the length
input_list_len = int(input())
integer_list = []
time_spent1 = []
time_spent2 = []
time_spent3 = []
time_spent4 = []
time_spent5 = []
time_spent6 = []

if input_list_len < 1:
    sys.exit('input must not be lesser than 1')


for k in range(2000):
    for i in range(input_list_len):
        integer_list.append(random.randint(-100, 100))
    # print(integer_list)

    # 1번: 기본형
    '''
    start = time.time()

    sum_of_consecutive_list = []

    for i in range(0, input_list_len):
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()

    # print(end-start)
    time_spent1.append(end - start)
    '''

    # 2번: 시작점이 음수인 경우 제외
    '''
    start = time.time()

    sum_of_consecutive_list = []

    for i in range(0, input_list_len):
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if not bool(sum_of_consecutive_list):
        for i in range(0, input_list_len):
            temp = 0
            for j in range(i, input_list_len):
                temp += integer_list[j]
                sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()

    # print(end-start)
    time_spent2.append(end-start)
    '''

    # 3번: 시작점, 끝점이 음수인 경우 제외
    '''
    start = time.time()

    integer_list += [-1]
    sum_of_consecutive_list = []
    for i in range(0, input_list_len):
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            if integer_list[j] <= 0:  # 끝점이 음수인 경우 제외
                temp += integer_list[j]
                j += 1
                continue
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 마지막 요소를 제외한 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if not bool(sum_of_consecutive_list):
        for i in range(0, input_list_len):
            temp = 0
            for j in range(i, input_list_len):
                temp += integer_list[j]
                sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()

    # print(end-start)
    time_spent3.append(end-start)
    '''

    # 4번: 시작점, 끝점이 음수인 경우 제외, 끝점 다음 수가 양수일 경우 제외
    '''
    start = time.time()

    integer_list.append(-1)
    sum_of_consecutive_list = []
    for i in range(0, input_list_len):
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            if integer_list[j] <= 0 or integer_list[j + 1] >= 0:  # 끝점이 음수인 경우 제외, 다음 수가 양수일 경우도 제외
                temp += integer_list[j]
                j += 1
                continue
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 마지막 요소를 제외한 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if not bool(sum_of_consecutive_list):
        for i in range(0, input_list_len):
            temp = 0
            for j in range(i, input_list_len):
                temp += integer_list[j]
                sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()

    # print(end-start)
    time_spent4.append(end-start)
'''

    # 5번: 시작점 음수 제외, 시작점 앞 수 양수 제외 1
    '''
    start = time.time()

    integer_list.insert(0, -1)
    sum_of_consecutive_list = []
    for i in range(1, input_list_len + 1):
        if integer_list[i] <= 0 or integer_list[i - 1] >= 0:  # 시작점이 음수인 경우 제외, 시작점 앞의 수가 양수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len + 1):
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 마지막 요소를 제외한 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if not bool(sum_of_consecutive_list):
        for i in range(0, input_list_len):
            temp = 0
            for j in range(i, input_list_len):
                temp += integer_list[j + 1]
                sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()

    # print(end-start)
    time_spent3.append(end-start)

    integer_list.pop(0)
    '''

    # 6번: 시작점 음수 제외, 시작점 앞 수 양수 제외 2
    '''
    start = time.time()

    sum_of_consecutive_list = []
    for i in range(0, input_list_len):
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        if i > 0:  # 시작점 앞 수가 양수인 경우 제외, and 사용하면 안됨
            if integer_list[i - 1] >= 0:
                i += 1
                continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 마지막 요소를 제외한 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if not bool(sum_of_consecutive_list):
        for i in range(0, input_list_len):
            temp = 0
            for j in range(i, input_list_len):
                temp += integer_list[j]
                sum_of_consecutive_list.append(temp)

    print(max(sum_of_consecutive_list))

    end = time.time()
    time_spent3.append(end - start)
    '''

    # 7번: 헌이형 방법
    '''
    start = time.time()

    result = integer_list[0]
    for i in range(0, input_list_len):
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            result = max(result, temp)
    print(result)

    end = time.time()

    # print(end-start)
    time_spent2.append(end - start)
    '''

    # 8번: 시작점이 음수인 경우 제외, 시작점 앞수 양수 제외, 리스트 생성 안됐을 때 변형
    '''
    start = time.time()

    sum_of_consecutive_list = []

    for i in range(0, input_list_len):
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        if i > 0:  # 시작점 앞 수가 양수인 경우 제외, and 사용하면 안됨
            if integer_list[i - 1] >= 0:
                i += 1
                continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            sum_of_consecutive_list.append(temp)

    # integer_list의 모든 요소가 음수일 경우 sum_of_consecutive_list가 생성되지 않았을 때
    if bool(sum_of_consecutive_list):
        print(max(sum_of_consecutive_list))
    else:
        print(max(integer_list))

    end = time.time()

    time_spent3.append(end-start)
    '''

    # 9번: while문 사용하여 i 조정, 시작점 음수 제외
    start = time.time()

    sum_of_consecutive_list = []
    i = 0
    while i < input_list_len:
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]  # temp 값이 0 보다 작아질 경우 i = j 로 넘어감
            if temp <= 0:
                i = j
                break
            sum_of_consecutive_list.append(temp)
            if j == input_list_len - 1:  # j 가 리스트의 끝에 도달하면 멈춤
                i = input_list_len
                break

        i += 1

    if bool(sum_of_consecutive_list):
        print(max(sum_of_consecutive_list))
    else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
        print(max(integer_list))

    end = time.time()

    time_spent1.append(end-start)

    # 10번: while문 사용하여 i 조정, 시작점 음수 제외, set
    '''
    start = time.time()

    sum_of_consecutive_set = set()
    i = 0
    while i < input_list_len:
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            if temp <= 0:
                i = j
                break
            sum_of_consecutive_set.add(temp)
            if j == input_list_len - 1:
                i = input_list_len
                break

        i += 1

    if bool(sum_of_consecutive_set):
        print(max(sum_of_consecutive_set))
    else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
        print(max(integer_list))

    end = time.time()

    time_spent2.append(end-start)
    '''

    # 11번: while문 사용, 시작점 음수 제외, 끝점 음수, 끝점 다음수 양수 제외
    '''
    start = time.time()

    sum_of_consecutive_list = []
    i = 0
    while i < input_list_len:
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            if temp <= 0:
                i = j
                break
            if j == input_list_len - 1:
                i = input_list_len
                sum_of_consecutive_list.append(temp)
                break
            if j < input_list_len-1:
                if integer_list[j + 1] >= 0:  # 끝점이 음수인 경우 제외, 다음 수가 양수일 경우도 제외
                    continue
            sum_of_consecutive_list.append(temp)

        i += 1

    if bool(sum_of_consecutive_list):
        print(max(sum_of_consecutive_list))
    else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
        print(max(integer_list))

    end = time.time()
    time_spent2.append(end-start)
    '''

    # 12번: while문 사용하여 i 조정, 시작점 음수 제외 안함
    '''
    start = time.time()

    sum_of_consecutive_list = []
    i = 0
    while i < input_list_len:
        temp = 0
        for j in range(i, input_list_len):
            temp += integer_list[j]
            if temp <= 0:  # temp 값이 0 보다 작아질 경우 i = j 로 넘어감
                i = j
                break
            sum_of_consecutive_list.append(temp)
            if j == input_list_len - 1:  # j 가 리스트의 끝에 도달하면 멈춤
                i = input_list_len
                break

        i += 1

    if bool(sum_of_consecutive_list):
        print(max(sum_of_consecutive_list))
    else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
        print(max(integer_list))

    end = time.time()
    time_spent2.append(end-start)
    '''

    # 13번: double while
    '''
    start = time.time()
    sum_of_consecutive_list = []
    i = 0
    while i < input_list_len:
        if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외
            i += 1
            continue
        temp = 0
        j = i
        while j < input_list_len:
            temp += integer_list[j]
            if temp <= 0:  # temp 값이 0 보다 작아질 경우 i = j 로 넘어감
                i = j
                break
            sum_of_consecutive_list.append(temp)
            if j == input_list_len - 1:  # j 가 리스트의 끝에 도달하면 멈춤
                i = input_list_len
                break
            j += 1

        i += 1

    if bool(sum_of_consecutive_list):
        print(max(sum_of_consecutive_list))
    else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
        print(max(integer_list))

    end = time.time()
    time_spent2.append(end-start)
    '''

    integer_list = []


print(sum(time_spent1) / 2000)
# print(sum(time_spent2) / 10000)
# print(sum(time_spent3) / 10000)
# print(sum(time_spent4) / 100000)
# print(sum(time_spent5) / 100000)
# print(sum(time_spent6) / 100000)

'''
len == 1 : while-허헌=기본-for
len >= 2 : while-for-기본-허헌
13번 "double while"이 len <= 7 에서는 최종본보다 빠름
10번 set이 랜덤한 숫자 범위를 작게 하여 중복되는 것을 늘렸을 때는 더 빠름, (-1, 1)로 실험
'''