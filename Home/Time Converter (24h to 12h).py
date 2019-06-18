"""
Вы предпочитаете использовать 12-часовой формат времени, но современный мир
живет в 24-часовом формате и вывидите это повсюду.
Ваша задача - переконвертировать время из 24-часового формата в 12-часовой,
использкя следующие правила:
- выходной формат должен быть 'чч:мм a.m.' (для часов до полудня) или 'чч:мм p.m.' (для часов после полудня)
- если часы меньше 10 - не пишите '0' перед ними. Например: '9:05 a.m.'
"""


def time_converter(time):
    h, m = time.split(':')
    if int(h) == 0:
        return '{}:{} a.m.'.format(int(h) + 12, m)
    if int(h) == 12:
        return '{}:{} p.m.'.format(int(h), m)
    if int(h) > 12:
        return '{}:{} p.m.'.format(int(h) - 12, m)
    return '{}:{} a.m.'.format(int(h), m)
    
        

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
