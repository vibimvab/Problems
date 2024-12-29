file_type_list = []
file_type_count = []


def return_file_type(file_name):
    file_name_list = file_name.split('.')
    # if '.' in file_name and file_name_list[len(file_type_list) - 1] != '':
    #     return file_name_list[len(file_name_list)-1]
    # else:
    #     print("invalid file name")

    if len(file_name_list) == 2 and 3 <= len(file_name) <= 100 and '' not in file_name_list:
        return file_name_list[1]
    else:
        print("invalid file name")


while 1:
    input_file_name = input("Enter file name (0 to stop): ")
    if input_file_name == '0':
        break

    file_type = return_file_type(input_file_name)
    if file_type:
        if file_type not in file_type_list:
            file_type_list.append(file_type)
            file_type_count.append(1)
        else:
            file_type_count[file_type_list.index(file_type)] += 1

print(file_type_list)
print(file_type_count)

for i in range(len(file_type_list)):
    temp = min(file_type_list)
    print(f"{temp}: {file_type_count[file_type_list.index(temp)]}")
    file_type_count.pop(file_type_list.index(temp))
    file_type_list.remove(temp)
