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


def split_and_merge_list(a):
    n1 = len(a) // 2
    a1 = a[:n1]
    a2 = a[n1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


mas = [random.randint(-50, 50) for i in range(100)]
print(split_and_merge_list(mas))

# O(n * log(n))
