import random
import time


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def __str__(self):
        return f'Значение в данном месте: {self.key}'


def insert_node(root, node):  # Вставка узла в дерево
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)
        elif root.key < node.key:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)


def sort_max(root):
    if root is not None:
        sort_max(root.left)
        print(root.key)
        sort_max(root.right)


def sort_min(root):
    if root is not None:
        sort_min(root.right)
        print(root.key)
        sort_min(root.left)


def search_min(root):
    if root.left is None:
        return root.key
    else:
        return search_min(root.left)


def search_max(root):
    if root.right is None:
        return root.key
    else:
        return search_max(root.right)


Node = BinaryTree(8)
start = time.time()
for i in range(10000):
    insert_node(Node, BinaryTree(random.randint(-30, 1500)))
sort_max(Node)
end = time.time()
binary_sort_result = end - start

start = time.time()
gen = (random.randint(-30, 1500) for _ in range(10000))
arr = [*gen]
arr.sort()
for el in arr:
    print(el)
end = time.time()
built_in_sort_result = end - start

print("Binary sort execution time is:{arg1:9.5f}\nBuilt in sort() method execution time is:{arg2:9.5f}".format(
    arg1=binary_sort_result, arg2=built_in_sort_result))
