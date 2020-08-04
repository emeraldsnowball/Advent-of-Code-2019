num_range = [i for i in range(165432,707913)]
print(len(num_range))
new_list = []
for i in num_range:
    str_num = str(i)
    if not (len(str_num) != 6 or any(str_num[i] > str_num[i+1] for i in range(5))):
        new_list.append(i)

new_list1 = []
print(len(new_list))
for i in new_list:
    str_num = str(i)
    if any(str_num[j] == str_num[j+1] for j in range(5)):
        new_list1.append(i)

print(len(new_list1))
