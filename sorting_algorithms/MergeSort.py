import random


def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)

    i = 0
    j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]

    return c


def split_and_merge_list(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2

    left = split_and_merge_list(arr[:middle])
    right = split_and_merge_list(arr[middle:])

    return merge_list(left, right)


mas = [random.randint(-50, 500) for i in range(100)]
print(split_and_merge_list(mas))

# O(n * log(n))
