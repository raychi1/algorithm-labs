import copy
from sort import *


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


while True:
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
            print(f"Your array is:", *array, sep=' ')

            res_array = RadixSort(arr=array)
            print(f"Sorted array is:", *res_array, sep=' ')
            print(f"Is sorted right? {res_array == array_1}\n\n", )
