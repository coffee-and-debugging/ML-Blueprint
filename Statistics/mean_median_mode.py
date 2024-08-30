import numpy as np
from scipy import stats

random_numbers= np.random.randint(1,100, size=200)

mean= np.mean(random_numbers)
median= np.median(random_numbers)
mode= stats.mode(random_numbers)

print(f"{mean}, {median}, {mode}")



import random
from collections import Counter

random_numbers = [random.randint(1, 100) for _ in range(20)]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def calculate_mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, cnt in count.items() if cnt == max_count]
    return modes, max_count

mean_value = calculate_mean(random_numbers)
median_value = calculate_median(random_numbers)
modes, mode_count = calculate_mode(random_numbers)

print("Random Numbers:", random_numbers)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {', '.join(map(str, modes))} (occurs {mode_count} times)")