from Heap import Heap as Heap
arr = [1, 6, 7, 7, 9, 12, 14, 10, 14, 11]


a = Heap(arr)
print(f"1. {a.heap_arr = }")
a.BuildMinHeap()
print(arr == a.heap_arr)
a.ShowHeap()

print(a.HeapMin())
print(a.ExtractMin())
a.ShowHeap()
a.HeapDecreaseKey(index=3, data=0)
a.ShowHeap()
print(a.HeapDecreaseKey(index=3, data=12))
a.ShowHeap()
