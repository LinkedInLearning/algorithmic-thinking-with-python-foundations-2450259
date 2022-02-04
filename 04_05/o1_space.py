def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


my_list = [5, 4, 3, 2, 1]
print(my_sum(my_list))
