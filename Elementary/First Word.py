"""
Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:

В строке могут встречатся точки и запятые
Строка может начинаться с буквы или, к примеру, с пробела или точки
В слове может быть апостроф и он является частью слова
Весь текст может быть представлен только одним словом и все
"""
from string import punctuation


def first_word(text: str) -> str:
    f = list(punctuation)
    f.remove("'")
    for item in f:
        if item in text:
            text = text.replace(item, ' ')
    return text.lstrip().rstrip().split(' ')[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")