def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


mas = [0, 1, -11, 10, 5, 2, 7, 16]
print(bubble_sort(mas))

# O(n^2)
