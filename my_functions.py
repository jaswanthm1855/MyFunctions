def convert_capital_letters_to_small_with_underscore(string):
    converted_string = ''
    for i in string:
        if 'A' <= i <= 'Z':
            converted_string += '_' + i.lower()
        else:
            converted_string += i
    return converted_string[1:]


def convert_small_letters_to_capitals_with_underscore_to_capitals(string):
    new_str = convert_capital_letters_to_small_with_underscore(string)
    return new_str.upper()

