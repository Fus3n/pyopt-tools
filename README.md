[![PYPI](https://img.shields.io/pypi/v/pyopt-tools?color=green&label=pyopy-tools&logo=python&logoColor=green)](https://pypi.org/project/pyopt-tools/0.7/)

# Pyopt-tools
PyOpt-tools contains a set of mirco function most of these functions are easy but **most of us** don't want to waste time searching for "how to reverse a string in python" or "how to sort a list by type in python" but as you're here I am assuming you fall into "most of us" category.

You may find some function useful for you, but you may also find some of them useless. because there just way too small and you can write them anytime but It's not about the functions' complexity. it's about knowing how to do it. most of us don't want to spend time finding functions like this just to prototype a project or just to test a function.

[Full Documentation](https://fus3n.github.io/pyopt-tools/)

## What kind of functions?
Functions are separated into different files. there are currently **string_tools, math_tools, list_tools** and also **pyvec** pyvec contains vector 2 and 3 class that has some useful vector maths for game development. or you can use it to do normal stuff (not that game development isn't normal just saying)

Every function has proper documentation and comments with examples. But I also included all the functions in [example]("https://github.com/Fus3n/pyopt-tools/blob/main/example.py") file. Which will be updated as I add more functions.


### Some Functions it includes

```python
from pyopt_tools import listools
from pyopt_tools import string_tools
from pyopt_tools import math_tools
from pyopt_tools.pyvec import Vec2, Vec3
from pyopt_tools import file_tools

## string tools
print("Split str", string_tools.split_str("Hello World", 2))
print("Randomize String", string_tools.randomize_string("Hello world"))
print("encodeMorse", string_tools.encodeMorse("Hello world"))
print("decodeMorse", string_tools.decodeMorse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print("to_binary", string_tools.to_binary("Hello"))
print("bin_to_text", string_tools.bin_to_text("1001000 1100101 1101100 1101100 1101111"))  # only works with spaces
print("Reverse String", string_tools.reverse_string("Hello world"))


## math tools
print("reverse_int", math_tools.reverse_int(123))
print("persistence", math_tools.persistence(1234))
print("is_square", math_tools.is_square(6))
print("is_pentagonal", math_tools.is_pentagonal(6))
print("is_hexagonal", math_tools.is_hexagonal(5))
print("lerp", math_tools.lerp(0, 10, 0.5))
print("clamp", math_tools.clamp(0, 10, -1))

# pyvec # Vec2 and Vec3 contains all same functions
print("Vec2", Vec2(1, 2))
print("Vec3", Vec3(1, 2, 3))
print("Vec2.dot", Vec2(1, 2).dot(Vec2(3, 4)))
print("Vec3.cross", Vec3.cross(Vec3(1, 2, 3), Vec3(3, 4, 5)))  # static method

## list tools
test_list = [2, "hello", 1, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, "hello"]
print("listools.remove_duplicates",
      listools.remove_duplicates(test_list))
print("listools.remove_duplicates_sort",
      listools.remove_duplicates_sort(test_list))
print("listools.sort_list", listools.sort_list([2, 3, 2, 1, "string1", "string2", "string3",  3.3, 2.2], (str, int, float), sort_elements=True)) # sort list by types and in which order also option to sort each element in the list
# find string in multiple files in the given folder
result = file_tools.find_in_files("F:/Important Folder/", "test string", ["py", "cup", "txt"])
for res in result:
    filename, line, string = res
    print("file_tools.find_in_files", repr(filename), line, repr(string))
```

## Check out [documentation](https://fus3n.github.io/pyopt-tools/) for more information