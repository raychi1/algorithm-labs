

def mergeSort(Array: list):
    if len(Array) > 1:
        mid = len(Array) // 2
        L = Array[:mid]
        R = Array[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                Array[k] = L[i]
                i += 1
            else:
                Array[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            Array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            Array[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = input('Please write your array: ').split()
    arr = [int(item) for item in arr]
    print("Given array is", end="\n")
    print(*arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    print(*arr)
