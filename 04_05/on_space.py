def double(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[i] * 2)
    return new_list


my_list = [5, 4, 3, 2, 1]
print(double(my_list))
