import copy
from Sort import *


def readFromfile(filename: str = 'array.txt'):
    file = open(filename)
    res = file.readlines()
    file.close()
    res = [int(item) for item in res]
    return res


def readFrominput():
    res = input('Please, input your array: ')
    res = [int(item) for item in res.strip().split()]
    return res


func = {
    1: readFromfile,
    2: readFrominput,
}

# while True:
answer = input('Please, write way which do you want to use\n 1) Read from file\n 2) Read from terminal\n'
               'Your answer: ')
try:
    answer = int(answer)
except ValueError:
    print('Please, write number\n')
else:
    if answer not in func.keys():
        print('Please, write correct number\n')
    else:
        array = func[answer]()
        array_1 = copy.copy(array)
        array_1.sort()
        array_2 = copy.copy(array)
        answer = int(input("Which element do you want to find (from 1): "))
        if answer > len(array):
            print("Please, write correct number")
        else:
            print(f"Your array is:", *array, sep=' ')
            QuickSortRandomized(arr=array, start=0, end=len(array) - 1)
            print(f"Sorted array is:", *array, sep=' ')
            print(f"Is sorted right? {array == array_1}\n\n", )
            print(f"Your element", RandomaizedSelect(array_2, start=0, end=len(array_2)-1, i=answer))
            print(f"Min element = {array[0]}\nMax element = {array[-1]}")
            index = len(array) // 2
            if len(array) % 2 == 0:
                print(f"Mediana = {array[index]} and {array[index+1]}")
            else:
                print(f"Mediana = {array[index]}")

