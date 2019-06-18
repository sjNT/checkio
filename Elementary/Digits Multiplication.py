"""
Дано положительное целое число.
Вам необходимо подсчитать произведение всех цифр в этом числе,
за исключением нулей.

Для примера: Дано число 123405.
Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
"""


def checkio(number: int) -> int:
    s = 1
    for item in [i for i in str(number).replace('0', '')]:
        s = s * int(item)
    return s

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
