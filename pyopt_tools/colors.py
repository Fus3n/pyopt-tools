"""
Contains:
    Colors:
        - Colors Class
        - Create & Convert colors to RGB, HEX, HSV and CMYK

    Colors tuples in RGB
"""

from math import floor
from typing import Tuple


class Color:
    """
    Color values in RGB
    """
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Yellow = (255, 255, 0)
    Cyan = (0, 255, 255)
    Magenta = (255, 0, 255)
    Orange = (255, 165, 0)
    Purple = (128, 0, 128)
    Brown = (165, 42, 42)
    Grey = (128, 128, 128)
    DarkGrey = (64, 64, 64)
    Pink = (255, 192, 203)
    LightBlue = (173, 216, 230)
    LightGreen = (144, 238, 144)
    LightGrey = (211, 211, 211)
    LightPink = (255, 182, 193)
    LightSalmon = (255, 160, 122)
    LightSeaGreen = (32, 178, 170)
    LightSkyBlue = (135, 206, 250)
    LightSlateGray = (119, 136, 153)
    LightSteelBlue = (176, 196, 222)
    LightYellow = (255, 255, 224)
    PaleGreen = (152, 251, 152)
    PaleTurquoise = (175, 238, 238)
    PaleVioletRed = (219, 112, 147)
    PapayaWhip = (255, 239, 213)
    PeachPuff = (255, 218, 185)
    Peru = (205, 133, 63)
    SeaGreen = (46, 139, 87)
    SkyBlue = (135, 206, 235)
    SlateBlue = (106, 90, 205)
    SlateGray = (112, 128, 144)
    Tan = (210, 180, 140)
    Teal = (0, 128, 128)
    Tomato = (255, 99, 71)
    Turquoise = (64, 224, 208)
    Violet = (238, 130, 238)
    Wheat = (245, 222, 179)
    YellowGreen = (154, 205, 50)

    def __init__(self, color: (tuple, "Color") = None):
        """
        Create a color from rbg or another color object
        :param color: tuple of rbg values or Color object

        Example:
            >>> clr1 =Color((255, 0, 0))
            >>> clr1
            >>> Color(255, 0, 0)
            >>> clr2 = Color(clr2.to_rgb())
            >>> clr2
            >>> Color(255, 0, 0)
            >>> clr3 = Color(clr2)
            >>> clr3
            >>> Color(255, 0, 0)
        """
        if isinstance(color, tuple):
            self.r, self.g, self.b = color
        elif isinstance(color, Color):
            self.r, self.g, self.b = color.to_rgb()
        elif color is None:
            self.r, self.g, self.b = 255, 255, 255
        else:
            raise TypeError(f"Color must be a tuple or a Color object, not {type(color)}")

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __str__(self):
        return f"{self.r}, {self.g}, {self.b}"

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __add__(self, other):
        return Color((self.r + other.r, self.g + other.g, self.b + other.b))

    def __getitem__(self, item):
        if item == 0:
            return self.r
        elif item == 1:
            return self.g
        elif item == 2:
            return self.b
        else:
            raise IndexError(f"Index must be 0, 1 or 2, not {item}")

    def to_hex(self) -> str:
        """
        Convert color to hexadecimal

        :return: hexadecimal string
        """
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def to_rgb(self) -> Tuple[int, int, int]:
        """
        Convert color to rgb

        :return: rgb tuple
        """
        return self.r, self.g, self.b

    def to_hsv(self) -> Tuple[int, int, int]:
        """
        Convert color to hsv
        :return: hsv tuple
        """
        r, g, b = self.r / 255, self.g / 255, self.b / 255
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx - mn
        h = 0
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / df) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / df) + 120) % 360
        elif mx == b:
            h = (60 * ((r - g) / df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = df / mx
        v = mx
        return floor(h), floor(s * 100), floor(v * 100)

    def to_cmyk(self) -> Tuple[int, int, int, int]:
        """
        Convert color to cmyk
        :return: cmyk tuple
        """
        r, g, b = self.r / 255, self.g / 255, self.b / 255
        k = 1 - max(r, g, b)
        if k == 1:
            c = 0
            m = 0
            y = 0
        else:
            c = (1 - r - k) / (1 - k)
            m = (1 - g - k) / (1 - k)
            y = (1 - b - k) / (1 - k)
        return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

    def to_kivy(self, alpha: float = 1.0) -> Tuple[float, float, float, float]:
        """
        Convert color to kivy color (rgba) rbg values are in range 0-1
        :return: kivy color tuple
        """
        return self.r / 255, self.g / 255, self.b / 255, alpha

