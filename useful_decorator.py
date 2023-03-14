import random


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time elapse: {end-start} seconds")
        return result
    return wrapper  # again, pay attention to not have: return wrapper() !!!


@timer
def call_qsort(arr):
    quick_sort(arr)


@timer
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


list1 = [random.randint(1, 10**6) for _ in range(10**4)]
bubble_sort(list1)

list2 = [random.randint(1, 10**6) for _ in range(10**6)]
call_qsort(list2)
