# Написать алгоритм, для того,
# чтобы в массиве оставить только уникальные элементы, большие 5


def get_unique(numbers):
    unique_numbers = [
        num for index, num in enumerate(numbers)
        if num > 5 and num not in numbers[index + 1:]
        and num not in numbers[:index]
    ]
    '''
    Вместо списковых включений можно использовать следующую конструкцию
    
    unique_numbers = []
    for index, number in enumerate(numbers):
        if number <= 5:
            continue
        if number in numbers[index + 1:] or number in numbers[:index]:
            continue
        if number not in unique_numbers:
            unique_numbers.append(number)
    '''

    return unique_numbers


def test_get_unique():
    result = get_unique([1, 5, 8, 8, 10])
    assert result == [10], f'Wrong answer: {result}'
    result = get_unique([])
    assert result == [], f'Wrong answer: {result}'
    result = get_unique([1, 2, 4, 5, 9, 87, 7, 11])
    assert result == [9, 87, 7, 11], f'Wrong answer: {result}'
    print('Good!')


if __name__ == '__main__':
    test_get_unique()
