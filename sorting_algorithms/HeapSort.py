'''
Куча - это дерево, в котором все родительские узлы не меньше чем узлы-потомки
Этапы:
1. Формируем из всего массива кучу. Для этого проходим справа-налево элементы и если у элемента есть потомки,
то для него делаем просейку.
2. Максимумы ставим в конец неотсортированной части массива
'''
import random


# Просейка сверху вниз, в рез-те которой создаётся куча
def heap_sift(arr, start, end):
    root = start

    # Цикл пока есть потомки, бОльшие чем их родитель
    while True:
        child = root * 2 + 1  # Левый потомок

        # Левый потомок за пределами подмассива - завершаем просейку
        if child > end:
            break

        # Если правый потомок тоже в пределах подмассива,
        # то среди потомков выбираем наибольший
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        # Если больший потомок больше корня, то меняем местами
        # при этом больший потомок сам становится корнем
        # от которого дальше опускаемся внз по дереву
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def heap_sort(arr):
    # Формируем кучу, проходимся справа-налево по эл-ам массива(у к-х есть потомки)
    # и делаем для каждого из них просейку
    for start in range(((len(arr) - 2) // 2), -1, -1):
        heap_sift(arr, start, len(arr) - 1)

    # Первый элемент массива - корень кучи
    # и он является максимумом для неотсортированной части массива
    for end in range(len(arr) - 1, 0, -1):
        # Меняем этот максимум местами с последним
        # элементом неотсортированной части массива
        arr[end], arr[0] = arr[0], arr[end]
        # После обмена в корне кучи немаксимальный элемент
        # Восстанавливаем кучу
        # Просейка для неотсортированной части массива
        heap_sift(arr, 0, end - 1)
    return arr


mas = [random.randint(-50, 50) for i in range(20)]
print(heap_sort(mas))

# O(n * log(n)) - average
