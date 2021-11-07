from pyopt_tools import string_tools
from pyopt_tools import int_tools

# String Tools
print("--"*10 + "String Tools", "--"*10)
print("Split str", string_tools.split_str("Hello World", 2))
print("Randomize String", string_tools.randomize_string("Hello world"))
print("Count Vowels", string_tools.count_vowels("Hello world"))
print("Count Consonants", string_tools.count_consonants("Hello world"))
print("Count Words", string_tools.count_words("Hello world"))
print("Cout lines", string_tools.count_lines("Hello world"))
print("Reverse String", string_tools.reverse_string("Hello world"))
print("is palindrome", string_tools.is_palindrome("ABA"))
print("is_pangram", string_tools.is_pangram("The quick brown fox jumps over the lazy dog"))
print("is_rotation", string_tools.is_rotation("ABA", "ABA"))
print("is_anagram", string_tools.is_anagram("waterbottle", "erbottlewat"))
print("encodeMorse", string_tools.encodeMorse("Hello world"))
print("decodeMorse", string_tools.decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print("encodeCaesar", string_tools.encodeCaesar("Hello world", 3))
print("decodeCaesar", string_tools.decodeCaesar("Kello world", 3))
print("to_binary", string_tools.to_binary("Hello"))
print("bin_to_text", string_tools.bin_to_text("1001000 1100101 1101100 1101100 1101111")) # only works with spaces
print("make_n_gram", string_tools.make_n_gram("Hello world", 2))
print("get_random_color", string_tools.get_random_color())
print("get_random_string", string_tools.get_random_string(10))


print("\n")

# Int Tools
print("--"*10 + "Int Tools", "--"*10)
print("reverse_int", int_tools.reverse_int(123))
print("persistence", int_tools.persistence(1234))
print("is_prime", int_tools.is_prime(6))
print("is_triangular", int_tools.is_triangular(6))
print("is_square", int_tools.is_square(6))
print("is_pentagonal", int_tools.is_pentagonal(6))
print("is_hexagonal", int_tools.is_hexagonal(5))
print("lerp", int_tools.lerp(0, 10, 0.5))
print("clamp", int_tools.clamp(0, 10, -1))
print("clamp01", int_tools.clamp01(10))



