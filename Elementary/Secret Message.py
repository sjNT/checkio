"""
Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь
услугами почты? Вы можете использовать газету,
чтобы рассказать кому-то свой секрет.
Даже если кто-то найдет ваше сообщение,
легко отмахнуться и сказать что это паранойя и теория заговора.
Один из самых простых способов спрятать ваше секретное сообщение это
использовать заглавные буквы.
Давайте найдем несколько такихсекретных сообщений.

Дан кусок текста. Соберите все заглавные буквы в одно слово
в том порядке как они встречаются в куске текста.

Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.",
если мы соберем все заглавные буквы, то получим сообщение "HELLO".
"""
import re

def find_message(text: str) -> str:
    """Find a secret message"""
    return ''.join(re.findall(r'[A-Z]', text))

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
