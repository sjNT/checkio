"""
Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте.
Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте,
что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква,
которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

Вх. данные: Текст для анализа, как строка.

Вых. данные: Наиболее частая буква, как строка.

Предусловия:
text содержит только ASCII символы.
"""

def checkio(string):
    counter_ord = {}
    temp = []
    for alpha in string:
        if alpha.isalpha() is True:
            if ord(alpha.lower()) not in counter_ord.keys():
                counter_ord[ord(alpha.lower())] = 1
            else:
                counter_ord[ord(alpha.lower())] += 1
    maxim = max(counter_ord.values())
    for item in counter_ord:
        if counter_ord[item] >= maxim:
            temp.append(item)
            maxim = counter_ord[item]
    return chr(min(temp))
        

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
