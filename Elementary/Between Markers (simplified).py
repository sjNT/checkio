"""
Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами.
Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers.

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
"""
def between_markers(text: str, begin: str, end: str) -> str:
    begin_pos = text.find(begin)
    end_pos = text.find(end)
    if begin_pos == - 1 and end_pos == -1:
        return text
    if begin_pos != -1:
        if end_pos != -1:
            return text[begin_pos + len(begin): end_pos]
        else:
            return text[begin_pos + len(begin):]
    return text[:end_pos]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
