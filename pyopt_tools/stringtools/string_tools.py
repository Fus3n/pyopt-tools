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
        >>>bin_to_text("1110100 1100101 1110011 1110100")\n
        >>>'test'
    """
    return "".join([chr(int(binary, 2)) for binary in string.split(" ")])

