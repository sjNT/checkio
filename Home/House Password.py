"""
Стефан и София забывают о безопасности и используют простые пароли для всего.
Помогите Николе разработать модуль для проверки паролей на безопасность.
Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит,
как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре.
Пароль может содержать только латинские буквы и/или цифры.

Вх. данные: Пароль как строка.

Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных,
который может быть сконвертирован и представлен как булево значение (True или False)

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

Предусловия:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""

import re
def checkio(data):
    if re.search('[a-z]', data) and re.search('[A-Z]', data) and re.search('[0-9]', data) and len(data) >=10:
        return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
