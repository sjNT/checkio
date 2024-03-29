"""
Ваша задача в этой миссии определить популярность определенных слов в тексте.

На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность
которых необходимо определить.

При решении этой задачи обратите внимание на следующие моменты

Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово
"one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
"""

def popular_words(text: str, words: list) -> dict:
    dic = dict(zip(words, [i * 0 for i in range(len(words))]))
    for word in dic.keys():
        dic[word] = text.lower().replace('\n', ' ').split(' ').count(word)
    return dic


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
