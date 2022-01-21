doors = [False] * 101  # So we can start at door no. 1 We will ignore index 0.

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i, end=", ")
