from itertools import groupby


def get_unique_array(array):
    unique_array = [num for num, _ in groupby(array)]
    return unique_array


def second_max(array):
    array = get_unique_array(array)
    if len(array) < 2:
        return None
    if array[0] > array[1]:
        max_1, max_2 = array[0], array[1]
    else:
        max_1, max_2 = array[1], array[0]
    index = 2
    '''
    Можно использовать следующую конструкцию вместо ф-ии get_unique_array
    
    while max_1 == max_2 and index < len(array):
        if max_1 > array[index]:
            max_2 = array[index]
        elif max_1 < array[index]:
            max_1 = array[index]
        index += 1
    if max_1 == max_2:
        return None
    '''
    for num in array[index:]:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num
    return max_2


def test_second_max():
    result = second_max([32, 2, -1, 2, 110, 45, 64])
    assert result == 64, f'Wrong answer: {result}'
    result = second_max([50, 50, 11])
    assert result == 11, f'Wrong answer: {result}'
    result = second_max([100, 100])
    assert result == None, f'Wrong answer: {result}'
    result = second_max([100, 100, 100])
    assert result == None, f'Wrong answer: {result}'
    result = second_max([100, 100, 100, 100, 10])
    assert result == 10, f'Wrong answer: {result}'
    result = second_max([100, 100, 100, 100, 10, 5, 10, 10, 9, 9, 5, 5, 90, 90, 60, 90, 91])
    assert result == 91, f'Wrong answer: {result}'
    result = second_max([1])
    assert result == None, f'Wrong answer: {result}'
    result = second_max([])
    assert result == None, f'Wrong answer: {result}'
    print('Good!')


if __name__ == '__main__':
    test_second_max()
