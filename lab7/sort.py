def CountingSort(arr: list, **kwargs):
    if 'exp' in kwargs.keys():
        size = len(arr)
        exp = kwargs['exp']
        res_arr = [0 for _ in range(size)]
        count_arr = [0 for _ in range(10)]
        for item in arr:
            digit = (item // exp) % 10
            count_arr[digit] += 1

        for index in range(1, 10):
            count_arr[index] += count_arr[index-1]

        for index in range(size-1, -1, -1):
            digit = (arr[index] // exp) % 10
            res_arr[count_arr[digit] - 1] = arr[index]
            count_arr[digit] -= 1
    else:
        min_element = min(arr)
        max_element = max(arr)

        count_arr = [0 for _ in range(max_element-min_element+1)]
        res_arr = [0 for _ in range(len(arr))]

        for item in arr:
            count_arr[item - min_element] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]

        for item in arr:
            res_arr[count_arr[item - min_element] - 1] = item
            count_arr[item - min_element] -= 1

    return res_arr


def RadixSort(arr: list):
    max_number = max(arr)
    exp = 1
    while max_number / exp > 0:
        arr = CountingSort(arr=arr, exp=exp)
        exp *= 10
    return arr

