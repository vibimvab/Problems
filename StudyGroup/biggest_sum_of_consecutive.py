import random
import sys
import time

# Gets length of the list from user,
input_list_len = int(input())

# Error message when input_list_len < 1
if input_list_len < 1:
    sys.exit('input must not be lesser than 1')

# Generate a list with random integers
integer_list = []
for i in range(input_list_len):
    integer_list.append(random.randint(-100, 100))
print(integer_list)

# Finding the biggest sum of consecutive
start = time.time()

sum_of_consecutive_list = []
i = 0
while i < input_list_len:
    if integer_list[i] <= 0:  # 시작점이 음수인 경우 제외, 이 부분은 없애도 if temp <= 0 에서 걸러지지만 넣는 버전이 더 빨랐음
        i += 1
        continue
    temp = 0
    for j in range(i, input_list_len):
        temp += integer_list[j]
        if temp <= 0:  # temp 값이 0 보다 작아질 경우 i = j 로 넘어감
            i = j
            break
        sum_of_consecutive_list.append(temp)
        if j == input_list_len-1:  # j 가 리스트의 끝에 도달하면 멈춤
            i = input_list_len
            break

    i += 1

if bool(sum_of_consecutive_list):  # list에 아무것도 안들어있을때 False를 반환
    print(max(sum_of_consecutive_list))
else:  # integer_list 의 모든 요소가 음수 -> sum_of_consecutive_list 가 생성되지 않았을 때
    print(max(integer_list))

end = time.time()
print(end-start)
# print(sum_of_consecutive_list)
