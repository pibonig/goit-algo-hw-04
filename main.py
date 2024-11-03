import random
import timeit

import pandas as pd


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def compare_sorting_algorithms():
    sizes = [100, 500, 1000, 5000, 10000]
    merge_times = []
    insertion_times = []
    timsort_times = []

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        merge_times.append(merge_time)

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        insertion_times.append(insertion_time)

        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
        timsort_times.append(timsort_time)

    results = pd.DataFrame({
        'Input Size': sizes,
        'Merge Sort (s)': merge_times,
        'Insertion Sort (s)': insertion_times,
        'Timsort (s)': timsort_times
    })

    print(results)


if __name__ == "__main__":
    compare_sorting_algorithms()
