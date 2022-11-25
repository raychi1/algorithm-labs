import random


def Partition(arr: list = None, start: int = 0, end: int = 0):
    if arr is None:
        arr = []
    pivot_index = (start + end) // 2
    pivot = arr[pivot_index]
    while start < end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    return end


def RandomizedPartition(arr: list = None, start: int = 0, end: int = 0):
    if arr is None:
        arr = []
    randpivot = random.randrange(start, end)
    pivot_index = (start + end) // 2
    arr[randpivot], arr[pivot_index] = arr[pivot_index], arr[randpivot]
    return Partition(arr, start, end)


def RandomaizedSelect(arr: list = None, start: int = 0, end: int = 0, i: int = 0):
    if arr is None:
        arr = []
    if start == end:
        return arr[start]
    q = RandomizedPartition(arr, start, end)
    k = q - start + 1
    if i == k:
        return arr[q]
    elif i < k:
        return RandomaizedSelect(arr, start, q - 1, i)
    else:
        return RandomaizedSelect(arr, q + 1, end, i-k)


def QuickSort(arr=None, start: int = 0, end: int = 0):
    if arr is None:
        arr = []
    if start < end:
        pointer = Partition(arr, start, end)
        QuickSort(arr, start, pointer - 1)
        QuickSort(arr, pointer + 1, end)


def QuickSortRandomized(arr=None, start: int = 0, end: int = 0):
    if arr is None:
        arr = []
    if start < end:
        pointer = RandomizedPartition(arr, start, end)
        QuickSort(arr, start, pointer - 1)
        QuickSort(arr, pointer + 1, end)