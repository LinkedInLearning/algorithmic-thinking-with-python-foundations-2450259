# 100 Doors

doors = [False] * 101

# Let's do just one pass
for i in range(1, 101):
    doors[i] = not doors[i]  # Using `not` to invert the Boolean value.

# Time for a nested for loop

# for x in range(1, 6):
#     for y in range(1, 4):
#         print("x:", x, "y:", y)

# Detour - steps in for loop
for i in range(1, 11, 2):
    print(i)
