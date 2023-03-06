import random
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


if __name__ == '__main__':
    for i in range(1, 11):
        a = [random.randint(0, 1000000) for _ in range(i*10000)]
        merge_sort_time = timeit.timeit(lambda: merge_sort(a.copy()), number=1)
        print(f'{i}  {merge_sort_time}')
