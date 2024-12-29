import sys

input_str: str = input()
input_str_len = len(input_str)
result = [-1 for x in range(26)]
print(input_str_len)

if input_str_len > 100:
    sys.exit("length of the string should be no bigger than 100")

# 가장 뒷 알파벳부터 차례로, 중복될 경우 앞의 것이 덧씌워짐.
for i in range(input_str_len):
    if 96 < ord(input_str[input_str_len - i - 1]) < 123:  # a~z 일 때
        result[ord(input_str[input_str_len - i - 1]) - 97] = input_str_len - i - 1
    else:
        sys.exit("string must contain only lower case English alphabets")

for i in range(26):
    print(result[i], end=" ")
