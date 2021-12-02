#
# MIT License
# Copyright (c) 2021 FUSEN
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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

    Example:\n
        >>>to_binary("test")\n
        >>>"1110100 1100101 1110011 1110100"
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

    Example:\n
        >>>bin_to_text("1110100 1100101 1110011 1110100")\n
        >>>'test'
    """
    return "".join([chr(int(binary, 2)) for binary in string.split(" ")])


def reverse_string(string: str) -> str:
    """
        Returns a new reversed string

    """
    return string[::-1]


def encodeMorse(sequence: str) -> str:
    """
       Encodes the given string to Morse Code

       Morse code is case-insensitive and traditonally Capital Letters are used
       Lower cases are converted to Upper cases

       Every Character code is seperated by a single space between them

       A space in the sequence is translated as '   ' three spaces

    Example:\n
        >>>encodeMorse("HELLO WORLD")\n
        >>>".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
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

    Example:\n
        >>>decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")\n
        >>>"HELLO WORLD"

    """
    return ' '.join(
        ''.join(_MORSE_DECODE_DICT[letter] for letter in word.split(' ')) for word in sequence.strip().split('   '))


def encodeCaesar(sequence: str, shift: int = 1) -> str:
    """
    Encodes the given string to Caesar Cipher

    Example:\n
        >>>encodeCaesar("HELLO WORLD", 1)\n
        >>>"IFMMP XPSME"
    """
    return ''.join(chr(((ord(c) - 65 + shift) % 26) + 65) if 65 <= ord(c) <= 90 else c for c in sequence)


def decodeCaesar(sequence: str, shift: int = 1) -> str:
    """
    Decodes the given string to Caesar Cipher

    Example:\n
        >>>decodeCaesar("IFMMP XPSME", 1)\n
        >>>"HELLO WORLD"
    """
    return ''.join(chr(((ord(c) - 65 - shift) % 26) + 65) if 65 <= ord(c) <= 90 else c for c in sequence)


def split_str(str: str, maxsplit: int = 1) -> list:
    """
    Splits characters of a String into List

    :param str: Specify a input String
    :param maxsplit: It is the number of skips in character before splitting, DEFAULT = 1
    :return: Returns the Array containing elements of characters splitted from the String
    """
    txt = ""
    str_list = []

    for i in str:
        txt += i
        if len(txt) == maxsplit:
            str_list.append(txt)
            txt = ''
    return str_list


def is_pangram(string: str) -> str:
    """
    Checks if the given string is a pangram or not

    Example:\n
        >>>is_pangram("The quick, brown fox jumps over the lazy dog!")\n
        >>>True

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

    Example:\n
        >>>is_palindrome("ABA")\n
        >>>True

    """
    if string == string[::-1]:
        return True
    return False


def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if the given string is an anagram of another string

    Example:\n
        >>>is_anagram("waterbottle", "erbottlewat")\n
        >>>True

    """
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def is_rotation(str1: str, str2: str) -> bool:
    """
    Checks if the given string is a rotation of another string

    Example:\n
        >>>is_rotation("waterbottle", "erbottlewat")\n
        >>>True

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
    """
    n_grams = []
    for i in range(len(string) - n + 1):
        n_grams.append(string[i:i + n])
    return n_grams


def randomize_string(string: str) -> str:
    """
    Randomizes the given string

    Example:\n
        >>>randomize_string("Hello World")\n
        >>>'rldloHW'

    """
    return ''.join(sample(string, len(string)))


def get_random_color() -> str:
    """
    Returns a random color

    Example:\n
        >>>get_random_color()\n
        >>>'#ff0000'

    """
    return '#{:06x}'.format(randint(0, 0xFFFFFF))


def get_random_string(length: int) -> str:
    """
    Returns a random string of given length

    Example:\n
        >>>get_random_string(10)\n
        >>>'qwertzuiop'

    """
    return ''.join(sample(ascii_letters, length))


def count_vowels(string: str) -> int:
    """
    Counts the number of vowels in the given string

    Example:\n
        >>>count_vowels("Hello World")\n
        >>>3

    """
    return sum(1 for char in string if char.lower() in 'aeiou')


def count_consonants(string: str) -> int:
    """
    Counts the number of consonants in the given string

    Example:\n
        >>>count_consonants("Hello World")\n
        >>>7

    """
    return sum(1 for char in string if char.lower() in 'bcdfghjklmnpqrstvwxyz')


def count_lines(string: str) -> int:
    """
    Counts the number of lines in the given string

    Example:\n
        >>>count_lines("Hello World")\n
        >>>1

    """
    return len(string.splitlines())


