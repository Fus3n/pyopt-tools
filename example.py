from pyopt_tools import string_tools
from pyopt_tools import math_tools
from pyopt_tools.pyvec import Vec2, Vec3
from pyopt_tools import listools
from pyopt_tools import file_tools
from pyopt_tools.colors import Color
from pyopt_tools.console import Loader
import time

# String Tools
print("--" * 10 + "String Tools", "--" * 10)
print("Split str", string_tools.split_str("Hello World", 2))
print("Randomize String", string_tools.randomize_string("Hello world"))
print("Count Vowels", string_tools.count_vowels("Hello world"))
print("Count Consonants", string_tools.count_consonants("Hello world"))
print("Count lines", string_tools.count_lines("Hello world"))
print("Reverse String", string_tools.reverse_string("Hello world"))
print("is palindrome", string_tools.is_palindrome("ABA"))
print("is_pangram", string_tools.is_pangram("The quick brown fox jumps over the lazy dog"))
print("is_rotation", string_tools.is_rotation("ABA", "ABA"))
print("is_anagram", string_tools.is_anagram("waterbottle", "erbottlewat"))
print("encodeMorse", string_tools.encodeMorse("Hello world"))
print("decodeMorse", string_tools.decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print("encodeCaesar", string_tools.encodeCaesar("Hello world", 3))
print("decodeCaesar", string_tools.decodeCaesar("IFMMP XPSME", 1))
print("to_binary", string_tools.to_binary("Hello"))
print("bin_to_text", string_tools.bin_to_text("1001000 1100101 1101100 1101100 1101111"))  # only works with spaces
print("make_n_gram", string_tools.make_n_gram("Hello world", 2))
print("get_random_color", string_tools.get_random_color())
print("get_random_string", string_tools.get_random_string(10))

print("\n")

# Math Tools
print("--" * 10 + "Int Tools", "--" * 10)
print("reverse_int", math_tools.reverse_int(123))
print("persistence", math_tools.persistence(1234))
print("is_prime", math_tools.is_prime(6))
print("is_triangular", math_tools.is_triangular(6))
print("is_square", math_tools.is_square(4))
print("is_pentagonal", math_tools.is_pentagonal(6))
print("is_hexagonal", math_tools.is_hexagonal(5))
print("lerp", math_tools.lerp(0, 10, 0.5))
print("clamp", math_tools.clamp(0, 10, -1))
print("clamp01", math_tools.clamp01(10))
print("prime_factors", math_tools.prime_factors(12))

# pyvec # Vec2 and Vec3 contains all same functions
print("\n")
print("--" * 10 + "pyvec", "--" * 10)
print("Vec2", Vec2(1, 2))
print("Vec3", Vec3(1, 2, 3))
print("Vec2.dot", Vec2(1, 2).dot(Vec2(3, 4)))
print("Vec3.cross", Vec3.cross(Vec3(1, 2, 3), Vec3(3, 4, 5)))  # static method
print("Vec3.angle_between", Vec3(1, 2, 3).angle_between(Vec3(3, 4, 5)))
print("Vec3.distance", Vec3(1, 2, 3).distance(Vec3(3, 4, 5)))
print("Vec3.angle", Vec3.angle(Vec3(1, 2, 3), Vec3(3, 4, 5)))  # static method
print("Vec3.normalize", Vec3(1, 2, 3).normalize())
print("Vec3.length", Vec3(1, 2, 3).length())
print("Vec3.length_squared", Vec3(1, 2, 3).length_sqr())
print("Vec3.reflect", Vec3(1, 2, 3).reflect(Vec3(3, 4, 5)))
print("Vec3.max", Vec3.max(Vec3(1, 2, 3), Vec3(3, 4, 5)))  # static method
print("Vec3.min", Vec3.min(Vec3(1, 2, 3), Vec3(3, 4, 5)))  # static method
print("Vec3.lerp", Vec3(1, 2, 3).lerp(Vec3(3, 4, 5), 0.5))

# List Tools
print("\n")
print("--" * 10 + "List Tools", "--" * 10)
test_list = [2, "hello", 1, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, "hello"]
print("listools.remove_duplicates",
      listools.remove_duplicates(test_list))
print("listools.remove_duplicates_sort",
      listools.remove_duplicates_sort(test_list))

print("listools.sort_list",
      listools.sort_list([2, 3, 2, 1, "string1", "string2", "string3", 3.3, 2.2], (str, int, float),
                         sort_elements=True))
print("listools.sort_list",
      listools.sort_list([2, 3, 2, 1, "string1", "string2", "string3", 3.3, 2.2], (str, int, float),
                         sort_elements=False))  # sort_elements = False is default
print("listools.subdivide_by_type", listools.subdivide_by_type([1, 2, 3, "hello", 2.3, "world", "hello"], (
    int, float, str)))  # if type not specified but list contains it that type of value will be excluded

# File tools
print("\n")
print("--" * 10 + "File Tools", "--" * 10)
print("file_tools.get_size", file_tools.get_size("pyopt_tools/string_tools.py"))
print("file_tools.get_size", file_tools.get_size("pyopt_tools/string_tools.py", "bytes"))
# find string in multiple files in the given folder
result = file_tools.find_in_files("F:/Random Script/", "test string", ["py", "cup", "txt"])
for res in result:
    filename, line, string = res
    print("file_tools.find_in_files", repr(filename), line, repr(string))

# Colors
print("\n")
print("--" * 10 + "Colors", "--" * 10)

color = Color(Color.PaleGreen)  # Color.LightBlue is tuple every static color is a tuple
# another way: Color("FF0000")
print("Color", color)
print("Color.to_hex", color.to_hex())
print("Color.to_rgb", color.to_rgb())
print("Color.to_hsv", color.to_hsv())
print("Color.to_cmyk", color.to_cmyk())
print("Color.to_kivy",
      color.to_kivy(alpha=1))  # Convert to kivy color format (r, g, b, a) in range of 0-1 (alpha is optional)
print("Color red", color[0])
print("Color green", color[1])
print("Color blue", color[2])
print("Color MATHS!", Color(Color.Red) + Color(Color.Green))
print("Color.hex_to_rgb", Color.hex_to_rgb("#ffffff"))

# Console
print("\n")
print("--" * 10 + "Console", "--" * 10)
print("console.Loader")
loader = Loader(['-_-', '0_-', '-_0', '0_0'])
loader.start(threaded=True)
time.sleep(0.5)
loader.stop()
