def selection_sort(xs):
    for i in range(len(xs) - 1):  # The last value will automatically be in correct position.
        # Find minimum value in unsorted region.
        min_index = i
        for j in range(i + 1, len(xs)):
            # Update min_index if the value at j is lower than current minimum value.
            if xs[j] < xs[min_index]:
                min_index = j
        # After finding the minimum value in the unsorted region, swap with the first unsorted value.
        xs[i], xs[min_index] = xs[min_index], xs[i]


# xs = [3, 2, 1, 5, 4]
xs = [-4, 2, 5, 8, -7, 3, 6, -1, 7]
print(xs)
selection_sort(xs)
print(xs)
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))  # A nice Pythonic way to check list is sorted.
