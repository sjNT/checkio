"""
Любой настоящий путешественник должен уметь делать три вещи:
добывать огонь, находить воду и извлекать полезную информацию из природы, окружающей его.
Программирование не поможет вам с огнем и водой, но с добычей информации справится вполне.

Ваша задача - определить угол солнца над горизонтом, зная время суток.
Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов.
В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00),
функция должна вернуть фразу "I don't see the sun!".
"""

def sun_angle(time):
    h = int((time.split(':')[0]).lstrip('0'))
    m = int((time.split(':')[1]))
    if h < 6 or h > 18 or h == 18 and m > 0:
        return "I don't see the sun!"
    t = ((h - 6) * 15) + ((m / 60) * 15)
    return t
    
    
    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
