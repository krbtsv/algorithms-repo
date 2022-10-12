from random import randint
import time


class Binary_Tree:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def __str__(self):
        return f'Значение в данном месте: {self.value}'


def insert_tree(root, node):  # Вставка узла в дерево
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                insert_tree(root.left, node)
        elif root.key < node.key:
            if root.right is None:
                root.right = node
            else:
                insert_tree(root.right, node)


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


# tree = Binary_Tree(8)
# insert_tree(tree, Binary_Tree(3))
# insert_tree(tree, Binary_Tree(1))
# insert_tree(tree, Binary_Tree(6))
# insert_tree(tree, Binary_Tree(10))
# insert_tree(tree, Binary_Tree(13))
# insert_tree(tree, Binary_Tree(4))
# insert_tree(tree, Binary_Tree(7))
# insert_tree(tree, Binary_Tree(14))


tree = Binary_Tree(38)

start = time.time()
for i in range(100000):
    insert_tree(tree, Binary_Tree(randint(1, 101)))
sort_max(tree)
end = time.time()
result1 = end - start

start = time.time()
gen = (randint(1, 101) for _ in range(100000))
mas = [*gen]
mas.sort()
# for i in range(100000):
#     mas.append(randint(1,101))
# mas.sort()
for el in mas:
    print(el)
end = time.time()
result2 = end - start

print(f'Binary Sort execution time is:{result1:9.5f}\nBuilt in sort() method execution time is:{result2:9.5f}')
