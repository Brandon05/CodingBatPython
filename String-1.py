# String-1 Coding Bat
# Link: http://codingbat.com/python


def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

    :param name: string
    :return: "Hello (name)!"
    """
    return "Hello %s!" % name


def make_abba(a, b):
    """
    Given two strings, a and b, return the result of putting them
    together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
    :param a: string e.g. "Hi"
    :param b: string e.g. "Bye"
    :return: "HiByeByeHi"
    """
    return a + b*2 + a


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

    :param tag: string e.g. "cite"
    :param word: string e.g. "Yay"
    :return: "<cite>Yay</cite>
    """
    return "<%s>%s</%s>" % (tag, word, tag)


def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new string where
    the word is in the middle of the out string, e.g. "<<word>>".

    :param out: string length 4 e.g. "<<>>"
    :param word: string e.g. "word"
    :return: "<<word>>"
    """
    return out[:2] + word + out[-2:]


def extra_end(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.

    :param str: string e.g. "hey"
    :return: new string made of 3 copies of the last 2 chars of the original string e.g. "eyeyey"
    """
    return str[-2:]*3


def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields
    the empty string "".

    :param str: string e.g. "Hello"
    :return: "He"
    """
    return str[:2]


def first_half(str):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

    :param str: string of even length e.g. "YesSir"
    :return: first half of str e.g. "Yes"
    """
    return str[:len(str)/2]


def without_end(str):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.

    :param str: string with length >= 2 e.g. "Hey"
    :return: str without the first or last char e.g. "e"
    """
    return str[1:-1]


def combo_string(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and
    the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    :param a: string e.g. "aaa"
    :param b: string e.g. "b"
    :return: string where the longer string is on the inside and shorter string on the outside e.g. "baaab"
    """
    return a + b + a if len(a) < len(b) else b + a + b


def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.
    The strings will be at least length 1.

    :param a: string with length >= 1 e.g. "hello"
    :param b: string with length >= 1 e.g. "hey"
    :return: concatenation without the first char of each e.g. "elloey"
    """
    return a[1:] + b[1:]


def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
    The string length will be at least 2.

    :param str: string with length >= 2
    :return: str with the first two chars are moved to the end
    """
    return str[2:] + str[:2]
