"""
Один робот был занят простой задачей: объединить последовательность строк в
одно выражение для создания инструкции по обходу корабля.
Но робот был левша и зачастую шутил и запутывал своих друзей правшей.

Дана последовательность строк. Вы должны объединить эти строки в
блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения
слова "right" на слова "left", даже если это часть другого слова.
Все строки даны в нижнем регистре.
"""
def left_join(phrases):
    phrases = [i.replace('right', 'left') for i in phrases]
    return ','.join(phrases)

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
