"""
Наш калькулятор свихнулся на цензуре и отказывается использовать некоторые слова. Вам необходимо обмануть его и написать программу для для суммирования чисел.

Дан массив чисел, необходимо найти сумму этих чисел. Ваше решение не должно содержать запрещенные слова, даже как часть слов.

Список запретных слов:

sum
import
for
while
reduce
"""

def checkio(data):
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    next_sm = data[-1] + data[0]
    data.pop(0)
    data[-1] = next_sm
    return checkio(data)
