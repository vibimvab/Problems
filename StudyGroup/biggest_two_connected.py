import sys

# number_list = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

number_list = [0] * 100

for i in range(100):
    temp = int(input())
    if temp != 0:
        number_list[i] = temp
    else:
        break

if number_list[0] == 0 or number_list[1] == 0:
    sys.exit('error')
else:
    biggest = number_list[0] + number_list[1]
    for j in range(1, 100):
        if number_list[j+1] == 0:
            break
        if biggest < number_list[j]+number_list[j+1]:
            biggest = number_list[j]+number_list[j+1]

print(biggest)
