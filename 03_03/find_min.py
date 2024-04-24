def find_min(xs):
    min_index = 0
    for i in range(len(xs)):
        if xs[i] < xs[min_index]:
            min_index = i
    return xs[min_index]


xs = [3, 2, 1, 5, 4]
min_value = find_min(xs)
print(f"The minimum value is {min_value}.")
