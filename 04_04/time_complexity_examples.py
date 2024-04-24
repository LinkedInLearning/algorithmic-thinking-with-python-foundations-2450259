# This simple statement takes O(1) time.
n = 100  # Assignment statement occurs once.

# For Loop. The output statement occurs n times, so the loop is O(n).
for i in range(n):
    print(n)  # Output statement occurs n times.

# This while loop takes O(n) time. The smaller, constant time operation (O(1)) is ignored.
count = 0  # Assignment statement takes O(1) time.
while count < n:
    count += 1

# If the for loop counter increases or decreases by a constant, the cost is O(n).
for i in range(0, n, 5):  # i ranges from 0 to n-1 in steps of 5.
    print(i)  # Output statement occurs n/5 times.

for i in range(n, 0, -5):  # i ranges from n to 1 in steps of 5.
    print(i)

#  If a loop counter increases or decreases by a multiple, the cost is O(log(n)).
n = 100
while n > 0:
    n = n // 2
    print(n)  # Output statement occurs approx. log₂(n) times.

# Nested loop. Here the cost is O(n^2).
n = 100
for i in range(n):
    for j in range(n):
        print(i, j)  # Output statement occurs n^2 times.
