"""
string_tools contains functions for manipulating strings and other useful string-related functions.
"""

from string import ascii_letters
from random import sample, randint

_MORSE_DECODE_DICT = {"-.-.--": "!", ".-..-.": '"', "...-..-": "$", ".-...": "&", ".----.": "\\", "-.--.": "(",
                      "-.--.-": ")", ".-.-.": "+", "--..--": ",", "-....-": "-", ".-.-.-": ".", "-..-.": "/",
                      "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6",
                      "--...": "7", "---..": "8", "----.": "9", "---...": ":", "-.-.-.": ";", "-...-": "=",
                      "..--..": "?", ".--.-.": "@", ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
                      "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
                      "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
                      "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", "..--.-": "_",
                      "...---...": "SOS"}
_MORSE_ENCODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                      '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                      '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def to_binary(string: str) -> str:
    """
    Convert String to numerical binary numbers
    returns numerical binary string
    :param string: String to convert

    Example:
        >>> to_binary("test")
        >>> "1110100 1100101 1110011 1110100"
    """
    bin_conv = []
    for c in string:
        ascii_val = ord(c)
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])

    return ' '.join(bin_conv)


def bin_to_text(string: str) -> str:
    """
    Convert Binary Numerical Values back to string
    returns utf-8 String
    :param string: Binary String
    :return: str

    Example:
        >>> bin_to_text("1110100 1100101 1110011 1110100")
        >>> 'test'
    """
    return "".join([chr(int(binary, 2)) for binary in string.split(" ")])


def reverse_string(string: str) -> str:
    """
    Returns a new reversed string
    :param string: String to reverse
    :return: str

    Example:
        >>> reverse_string("test")
        >>> "tset"


    """
    return string[::-1]


def encodeMorse(sequence: str) -> str:
    """
       Encodes the given string to Morse Code

       Morse code is case-insensitive and traditonally Capital Letters are used
       Lower cases are converted to Upper cases

       Every Character code is seperated by a single space between them

       A space in the sequence is translated as '   ' three spaces
    :param sequence: String to encode
    :return: str

    Example:
        >>> encodeMorse("HELLO WORLD")
        >>> ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
    """
    encoded = ''
    for letter in sequence.upper():
        if letter != ' ':
            encoded += _MORSE_ENCODE_DICT[letter] + ' '
        else:
            encoded += '  '

    return encoded.strip()


def decodeMorse(sequence: str) -> str:
    """
    Fully Decodes to Morse codes encoded using encodeMorse() to Upper Case Alphabets
    //Morse codes encoded using external encoders may raise error//
    :param sequence: String to decode
    :return: str

    Example:
        >>> decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        >>> "HELLO WORLD"

    """
    return ' '.join(
        ''.join(_MORSE_DECODE_DICT[letter] for letter in word.split(' ')) for word in sequence.strip().split('   '))


def encodeCaesar(sequence: str, shift: int = 1) -> str:
    """
    Encodes the given string to Caesar Cipher
    :param sequence: String to encode
    :param shift: Shift value

    Example:
        >>> encodeCaesar("HELLO WORLD", 1)
        >>> "IFMMP XPSME"
    """
    return ''.join(chr(((ord(c) - 65 + shift) % 26) + 65) if 65 <= ord(c) <= 90 else c for c in sequence)


def decodeCaesar(sequence: str, shift: int = 1) -> str:
    """
    Decodes the given string to Caesar Cipher
    :param sequence: String to decode
    :param shift: Shift value

    Example:
        >>> decodeCaesar("IFMMP XPSME", 1)
        >>> "HELLO WORLD"
    """
    return ''.join(chr(((ord(c) - 65 - shift) % 26) + 65) if 65 <= ord(c) <= 90 else c for c in sequence)


def split_str(string: str, maxsplit: int = 1) -> list:
    """
    Splits characters of a String into List of Strings
    :param string: String to split
    :param maxsplit: It is the number of skips in character before splitting, DEFAULT = 1
    :return: Returns the Array containing elements of characters splitted from the String

    Example:
        >>> split_str("HELLO WORLD", 2)
        >>> ['He', 'll', 'o ', 'Wo', 'rl']

    """
    txt = ""
    str_list = []
    for i in string:
        txt += i
        if len(txt) == maxsplit:
            str_list.append(txt)
            txt = ''
    return str_list


def is_pangram(string: str) -> bool:
    """
    Checks if the given string is a pangram or not
    :param string: String to check
    :return: bool

    Example:
        >>> is_pangram("The quick, brown fox jumps over the lazy dog!")
        >>> True

    """
    count = 0
    for character in range(97, 123):
        if chr(character) in string or chr(character).upper() in string:
            count += 1
    if count == 26: return True
    return False


def is_palindrome(string: str) -> bool:
    """
    Checks if the given string is a palindrome or not
    :param string: String to check
    :return: bool

    Example:
        >>> is_palindrome("ABA")\n
        >>> True

    """
    if string == string[::-1]:
        return True
    return False


def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if the given string is an anagram of another string
    :param str1: String to check
    :param str2: String to check
    :return: bool

    Example:
        >>> is_anagram("waterbottle", "erbottlewat")
        >>> True

    """
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def is_rotation(str1: str, str2: str) -> bool:
    """
    Checks if the given string is a rotation of another string
    :param str1: String to check
    :param str2: String to check
    :return: bool

    Example:
        >>> is_rotation("waterbottle", "erbottlewat")
        >>> True

    """
    if len(str1) != len(str2):
        return False
    return str2 in (str1 + str1)


def make_n_gram(string: str, n: int) -> list:
    """
    Creates n-grams from the given string

    :param string: Specify a input String
    :param n: Specify the n-gram size
    :return: Returns the Array containing n-grams

    Example:
        >>> make_n_gram("Hello world", 2)
        >>> ['He', 'el', 'll', 'lo', 'o ', ' w', 'wo', 'or', 'rl', 'ld']

    """
    n_grams = []
    for i in range(len(string) - n + 1):
        n_grams.append(string[i:i + n])
    return n_grams


def randomize_string(string: str) -> str:
    """
    Randomizes the given string
    :param string: String to randomize
    :return: str

    Example:
        >>> randomize_string("Hello World")
        >>> 'rldloHW'

    """
    return ''.join(sample(string, len(string)))


def get_random_color() -> str:
    """
    Returns a random hex color
    :return: str


    Example:
        >>> get_random_color()
        >>> '#ff0000'

    """
    return '#{:06x}'.format(randint(0, 0xFFFFFF))


def get_random_string(length: int) -> str:
    """
    Returns a random string of given length
    :param length: Length of the string
    :return: str

    Example:
        >>> get_random_string(10)
        >>> 'qwertzuiop'

    """
    return ''.join(sample(ascii_letters, length))


def count_vowels(string: str) -> int:
    """
    Counts the number of vowels in the given string
    :param string: String to count
    :return: int

    Example:
        >>> count_vowels("Hello World")
        >>> 3

    """
    return sum(1 for char in string if char.lower() in 'aeiou')


def count_consonants(string: str) -> int:
    """
    Counts the number of consonants in the given string
    :param string: String to count
    :return: int

    Example:
        >>> count_consonants("Hello World")
        >>> 7

    """
    return sum(1 for char in string if char.lower() in 'bcdfghjklmnpqrstvwxyz')


def count_lines(string: str) -> int:
    """
    Counts the number of lines in the given string
    :param string: String to count
    :return: int

    Example:
        >>> count_lines("Hello World")
        >>> 1

    """
    return len(string.splitlines())


