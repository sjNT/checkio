"""
В этой миссии Вам надо определить, все ли элементы массива равны.

Входные: List.

Выходные: Bool.

Precondition: all elements of the input list are hashable
"""

def all_the_same(data):
    if data == []:
        return True
    if len(data) != 0:
        if data.count(data[0]) == len(data):
            return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
