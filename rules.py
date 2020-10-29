import re
import numpy as np

from rule import OrRule, AndRule

"""
parse rules
"""
class Header(OrRule):

    header_number_patterns = [
        re.compile('\d\.\d?'),
        re.compile('(\d+\.)+'),
        re.compile('[A-Z]\.\d?\.?'),
    ]
    capitalize_word_pattern = re.compile('[A-Z]\D+')
    all_capital_word_pattern = re.compile('[A-Z]+')
    camel_pattern = re.compile('[A-Z][a-z]*?[A-Z]+[A-Za-z]*?')

    def header_number(self, word):
        # ex. 2., 2.2, 2.2.
        for pattern in Header.header_number_patterns:
            if bool(pattern.fullmatch(word)):
                return True

        return False

    def capitalize_word(self, word):
        # ex. Abstract
        return bool(Header.capitalize_word_pattern.fullmatch(word))

    def all_capital_word(self, word):
        # ex. ABSTRACT
        return bool(Header.all_capital_word_pattern.fullmatch(word))

    def camel_word(self, word):
        # ex. AbstractIntroduction
        return bool(Header.camel_pattern.fullmatch(word))



def start(line, mark):
    return line[0] == mark

def end(text, mark):

    text = text.rstrip("\n")
    return text[-1] == mark


"""
noise paragraph rules
"""
class Noise(OrRule):

    def FF(self, text): # form feed (^L)

        return text == chr(12)

    def not_header(self, text):

        return not is_header(text[0]) and len(text) <= 5

    def is_short(self, text):

        return len(text) <= 2

    def all_digit(self, text):

        for word in text.split():

            if not is_float(word):
                return False

        return True


def is_float(s):

    try:
        float(s)

    except ValueError:
        return False

    else:
        return True

# parsers initialize
is_header = Header()
is_noise = Noise()


if __name__ == "__main__":

    #print("•")
    #print("" == chr(12))
    print(is_header("1"))
    print(is_header("1."))
    print(is_header("1.2."))
    print(is_header("1.2.3."))
    print(is_header("Abst"))
    print(is_header("ABSTRACT"))
    print(is_header("abst"))
    print(is_header("..."))

    print("----")

    print(is_noise("64x64"))
    print(is_noise("4.4 4.35 3.12"))
    print(is_noise("4.4 (4.35) 3.12"))
    print(is_noise("m = 100"))
    print(is_noise("i=1"))
