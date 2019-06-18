"""
Ваше задание здесь создать функцию, которая получает массив(tuple) и
возвращает набор с 3 элементами - первым, третьим, вторым с конца.
"""
def easy_unpack(el: tuple) -> tuple:
    return (el[0], el[2], el[-2])

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
