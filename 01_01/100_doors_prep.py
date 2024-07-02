import math
import time


def changeStatus(door) -> bool:
    return not door


def loopThroughDoors(doors, iteration) -> None:
    for i in range(iteration, len(doors), iteration):
        doors[i] = changeStatus(doors[i])


def efficient_door_toggle(n):
    doors = [False] * (n + 1)
    for i in range(1, int(math.sqrt(n)) + 1):
        doors[i * i] = True
    return doors


def count_open_doors(n):
    return int(math.sqrt(n))


def method1(n):
    doors = [False] * (n + 1)
    for i in range(1, n + 1):
        loopThroughDoors(doors, i)
    return doors[1:]  # Exclude the 0th door


def method2(n):
    return efficient_door_toggle(n)[1:]  # Exclude the 0th door


def method3(n):
    return [i * i <= n for i in range(1, n + 1)]  # Generate boolean list


def time_method(method, n, iterations=100):
    total_time = 0
    for _ in range(iterations):
        start = time.time()
        result = method(n)
        total_time += time.time() - start
    return result, total_time / iterations


def main() -> None:
    n = 1_000_000  # Increased number of doors for more accurate timing
    iterations = 10  # Number of times to run each method for average timing

    result1, time1 = time_method(method1, n, iterations)
    print(f"Method 1 average time: {time1:.6f} seconds")

    result2, time2 = time_method(method2, n, iterations)
    print(f"Method 2 average time: {time2:.6f} seconds")

    result3, time3 = time_method(method3, n, iterations)
    print(f"Method 3 average time: {time3:.6f} seconds")

    # Compare results
    if result1 == result2 == result3:
        print("All methods produce the same result.")
    else:
        print("Results differ between methods.")
        print(f"Method 1 open doors: {sum(result1)}")
        print(f"Method 2 open doors: {sum(result2)}")
        print(f"Method 3 open doors: {sum(result3)}")

    # Count open doors (using method1 result)
    open_doors = sum(result1)
    print(f"Number of open doors: {open_doors}")


if __name__ == "__main__":
    main()
