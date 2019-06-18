"""
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
"""


def checkio(number: int) -> str:
    msg = ''
    if number % 3 == 0:
        msg += 'Fizz '
    if number % 5 == 0:
        msg += 'Buzz'
    elif msg == '':
        msg = str(number)
    return msg.rstrip()

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
