"""
Вам даны текущие цены на акции. Вам необходимо выяснить за
какие акции дают большую цену.

Input: Словарь (dict), в котором ключи - это рыночный код,
а значение - это цена за акцию(float)

Output: Строка, рыночный код
"""

def best_stock(data):
    for i in data.keys():
        if data[i] == max(data.values()):
            return i


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
