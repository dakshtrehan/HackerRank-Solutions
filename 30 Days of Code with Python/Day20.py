#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
number_swaps = 0

for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            swap = a.pop(j)
            a.insert(j+1, swap)
            number_swaps += 1

print(f"Array is sorted in {number_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
