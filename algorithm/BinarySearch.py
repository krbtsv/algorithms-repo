import random


def binary_search(mas, item):
    high_index = len(mas) - 1
    low_index = 0
    counter = 0
    while low_index <= high_index:
        middle_index = (high_index + low_index) // 2
        guess = mas[middle_index]
        if guess == item:
            counter += 1
            return f'Число {item} найдено за {counter} итераций'
        if guess < item:
            counter += 1
            low_index = middle_index + 1
        if guess > item:
            counter += 1
            high_index = middle_index - 1


arr = [i for i in range(1, 101)]
search_item = random.randint(1, 101)
print(binary_search(arr, search_item))

# O(log(n)) 
