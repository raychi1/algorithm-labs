INDENTATION = 5


class Heap:
    def __init__(self, InputList: list = None):
        self.heap_arr = InputList
        self.heap_len = len(InputList)
        self.swops = []

    def BuildMaxHeap(self):
        """Creates Heap from given array"""
        for i in range(self.heap_len // 2, -1, -1):
            self.SiftDownMax(index=i)

    def BuildMinHeap(self):
        """Creates Heap from given array"""
        for i in range(self.heap_len // 2, -1, -1):
            self.SiftDownMin(index=i)

    def MaxHeapify(self, index):
        """Sift down element in MaxHeap"""
        return self.SiftDownMax(index)

    def MinHeapify(self, index):
        """Sift Down element in MinHeap"""
        return self.SiftDownMin(index)

    def MaxHeapInsert(self, data):
        """Insert element in MaxHeap"""
        self.heap_arr.append(data)
        index = self.heap_len
        self.heap_len += 1
        self.SiftUpMax(index)

    def MinHeapInsert(self, data):
        """Insert element in MinHeap"""
        self.heap_arr.append(data)
        index = self.heap_len
        self.heap_len += 1
        self.SiftUpMin(index)

    def _Extract(self):
        """Swap First and Last element
        :return Last Element"""
        output = self.heap_arr[0]
        index = self.heap_len - 1
        self.heap_arr[0], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[0]
        self.heap_arr.pop()
        self.heap_len -= 1
        return output

    def HeapIncreaseKey(self, index: int = 0, data: int = 0):
        """Change data in MaxHeap"""
        try:
            self.heap_arr[index]
        except IndexError:
            return IndexError
        if self.heap_arr[index] < data:
            self.heap_arr[index] = data
            self.SiftUpMax(index)
        elif self.heap_arr[index] > data:
            return ValueError

    def HeapDecreaseKey(self, index: int = 0, data: int = 0):
        """Change data in MinHeap"""
        try:
            self.heap_arr[index]
        except IndexError:
            return IndexError
        if self.heap_arr[index] < data:
            return ValueError
        elif self.heap_arr[index] > data:
            self.heap_arr[index] = data
            self.SiftUpMin(index)

    def ExtractMax(self):
        """Remove Max element from MaxHeap"""
        output = self._Extract()
        self.SiftDownMax(0)
        return output

    def ExtractMin(self):
        """Remove Min element from MinHeap"""
        output = self._Extract()
        self.SiftDownMin(0)
        return output

    def HeapMin(self):
        """Returns Min element from MinHeap"""
        return self.heap_arr[0]

    def HeapMax(self):
        """Returns Max element from MaxHeap"""
        return self.heap_arr[0]

    def _HeapSortMax(self):
        output = list()
        for i in range(self.heap_len - 1, -1, -1):
            output.append(self.ExtractMax())
        return output

    def HeapSort(self, way_of_sorting: str = '>'):
        """Sort array using heap sort"""
        output = self._HeapSortMax()
        if way_of_sorting == '>':
            return output
        elif way_of_sorting == '<':
            return output[::-1]
        else:
            return None

    def SiftUpMax(self, index):
        """Sift up element for MaxHeap"""
        parent = self.parent(index)
        while self.HasParent(index) and self.heap_arr[parent] < self.heap_arr[index]:
            self.heap_arr[parent], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[parent]
            index = parent
            parent = self.parent(index)
        return index

    def SiftDownMax(self, index):
        """Sift down element for MaxHeap"""
        max_index = index
        left_child = self.left(index)
        if self.HasLeftChild(index) and self.heap_arr[left_child] > self.heap_arr[max_index]:
            max_index = left_child
        right_child = self.right(index)
        if self.HasRightChild(index) and self.heap_arr[right_child] > self.heap_arr[max_index]:
            max_index = right_child
        if index != max_index:
            self.heap_arr[index], self.heap_arr[max_index] = self.heap_arr[max_index], self.heap_arr[index]
            self.swops.append((self.heap_arr[index], self.heap_arr[max_index]))
            self.SiftDownMax(max_index)

    def SiftUpMin(self, index):
        """Sift up element for MinHeap"""
        parent = self.parent(index)
        while self.HasParent(index) and self.heap_arr[parent] > self.heap_arr[index]:
            self.heap_arr[parent], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[parent]
            index = parent
            parent = self.parent(index)
        return index

    def SiftDownMin(self, index):
        """Sift down element for MinHeap"""
        min_index = index
        left_child = self.left(index)
        if self.HasLeftChild(index) and self.heap_arr[left_child] < self.heap_arr[min_index]:
            min_index = left_child
        right_child = self.right(index)
        if self.HasRightChild(index) and self.heap_arr[right_child] < self.heap_arr[min_index]:
            min_index = right_child
        if index != min_index:
            self.heap_arr[index], self.heap_arr[min_index] = self.heap_arr[min_index], self.heap_arr[index]
            self.swops.append((index, min_index))
            self.SiftDownMin(min_index)

    def ShowHeap(self):
        print('-' * 44)
        self._ShowHeap()
        print('-' * 44)

    def _ShowHeap(self, index=0, d=0):
        if index >= self.heap_len:
            return
        l = self.left(index)
        r = self.right(index)
        self._ShowHeap(index=r, d=d + 1)
        print(' ' * INDENTATION * d + str(self.heap_arr[index]))
        self._ShowHeap(index=l, d=d + 1)

    @staticmethod
    def parent(index: int):
        return (index - 1) >> 1

    @staticmethod
    def left(index: int):
        return (index << 1) + 1

    @staticmethod
    def right(index: int):
        return (index << 1) + 2

    def HasParent(self, index: int):
        return self.heap_len > self.parent(index) >= 0

    def HasLeftChild(self, index: int):
        return self.left(index) < self.heap_len

    def HasRightChild(self, index: int):
        return self.right(index) < self.heap_len
