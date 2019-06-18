"""
Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, 
будет передано в первом аргументе, а сами данные по товарам будут переданы вторым аргументом.
"""


def bigger_price(limit: int, data: list) -> list:
    bigger = []
    big_di = {}
    for items in range(len(data)):
        big_di[data[items]['price']] = items
    for big in range(limit):
        bigger.append({"name": data[big_di[max(big_di.keys())]]['name'], "price": data[big_di[max(big_di.keys())]]['price']})
        big_di.pop(max(big_di.keys()))
    return bigger





if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
