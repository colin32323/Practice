import time
import random


a = [random.randint(0, 100000000) for _ in range(1000000)]


start = time.time()
largest = 0
for i in a:
    if i > largest:
        largest = i

second_largest = 0
for i in a:
    if i > second_largest and i != largest:
        second_largest = i
end = time.time()
basic_time = end - start
print(basic_time)

start = time.time()
a = sorted(a)
largest = a[-1]
i = len(a) - 1
while i > 0:
    if a[i] != largest:
        second_largest2 = a[i]
        break
    i -= 1
end = time.time()
timsort_time = end - start
print(timsort_time)
