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


MORSE_DECODE_DICT = {"-.-.--": "!", ".-..-.": '"', "...-..-": "$", ".-...": "&", ".----.": "\\", "-.--.": "(",
                     "-.--.-": ")", ".-.-.": "+", "--..--": ",", "-....-": "-", ".-.-.-": ".", "-..-.": "/",
                     "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6",
                     "--...": "7", "---..": "8", "----.": "9", "---...": ":", "-.-.-.": ";", "-...-": "=",
                     "..--..": "?", ".--.-.": "@", ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
                     "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
                     "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
                     "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", "..--.-": "_", "...---...": "SOS"}
MORSE_ENCODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                     '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def to_binary(string: str) -> str:
    """
    Convert String to numerical binary numbers
    returns numerical binary string
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
        >>bin_to_text("1110100 1100101 1110011 1110100")\n
        >>'test'
    """
    return "".join([chr(int(binary, 2)) for binary in string.split(" ")])


def reverse_string(string: str) -> str:
    """
        Returns a new reversed string

        >>reverse_string("hello")\n
        >>'olleh'

    """
    return string[::-1]


def encodeMorse(sequence: str) -> str:
    """
       Encodes the given string to Morse Code

       Morse code is case-insensitive and traditonally Capital Letters are used
       Lower cases are converted to Upper cases

       Every Character code is seperated by a single space between them

       A space in the sequence is translated as '   ' three spaces

    """
    encoded = ''
    for letter in sequence.upper():
        if letter != ' ':
            encoded += MORSE_ENCODE_DICT[letter] + ' '
        else:
            encoded += '  '

    return encoded.strip()


def decodeMorse(sequence: str) -> str:
    """
    Fully Decodes to Morse codes encoded using encodeMorse() to Upper Case Alphabets
    //Morse codes encoded using external encoders may raise error//

    """
    return ' '.join(
        ''.join(MORSE_DECODE_DICT[letter] for letter in word.split(' ')) for word in sequence.strip().split('   '))


def is_pangram(string: str) -> str:
    """
    Checks if the given string is a pangram or not

    >>is_pangram("The quick, brown fox jumps over the lazy dog!")\n
    >>True

    """
    count = 0
    for character in range(97, 123):
        if chr(character) in string or chr(character).upper() in string:
            count += 1
    if count == 26: return True
    return False
