integer_list = []

i = 0
while i < 9:
    user_input = int(input())
    if user_input in integer_list:
        print(f"No duplicate number. Re-enter #{i+1}")
    else:
        integer_list.append(user_input)
        i += 1

print(max(integer_list))
for i in range(9):
    if integer_list[i] == max(integer_list):
        print(f"#{i+1} is the biggest")

# # 한 줄에 몰아받기, 중복 걸러내진 못함
# input_string = input()
# integer_list = input_string.split()
#
# max_integer = max(integer_list)
# print(max_integer)
# for i in range(len(integer_list)):
#     if integer_list[i] == max_integer:
#         print(f"{i+1}번째 수")
