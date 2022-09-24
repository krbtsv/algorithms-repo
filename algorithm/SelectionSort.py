import random


def FindSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def SelectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = FindSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


mas = [random.randint(0, 150) for i in range(150)]
print(SelectionSort(mas))


# O(n^2)
