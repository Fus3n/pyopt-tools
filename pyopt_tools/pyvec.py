import math
from math import floor, ceil, trunc, acos


# Vector2
class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __int__(self, other: "Vec2"):
        self.x = other.x
        self.y = other.y

    def distance(self, other: "Vec2"):
        """
        Returns the distance between two points.
        :param other: The other point.
        :return: The distance.
        """
        return abs(self - other)

    def scale(self, other: "Vec2"):
        """
        Returns the scaled vector.
        :param other: The scaling vector.
        :return: The scaled vector.
        """
        return Vec2(self.x * other.x, self.y * other.y)

    def reflect(self, normal):
        """
        Returns the reflected vector.
        :param normal: The normal vector.
        :return: The reflected vector.
        """
        return self - 2 * self.dot(normal) * normal

    def angle_between(self, other):
        """
        Returns the angle between two vectors.
        :param other: The other vector.
        :return: The angle.
        """
        return acos(self.dot(other) / (self.length() * other.length()))

    @property
    def normalize(self):
        """
        Returns a normalized vector.
        :return: The normalized vector.
        """
        return self / self.length()

    def dot(self, other):
        """
        Returns the dot product of two vectors.
        :param other: The other vector.
        :return: The dot product.
        """
        return self.x * other.x + self.y * other.y

    def length(self):
        """
        Returns the length of the vector.
        :return: The magnitude.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5


    def length_sqr(self):
        """
        Returns the squared length of the vector.
        :return: The squared magnitude.
        """
        return self.x ** 2 + self.y ** 2

    @staticmethod
    def angle(a, b):
        """
        Returns the angle between two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The angle.
        """
        return acos(a.dot(b) / (a.length() * b.length()))

    @staticmethod
    def zero():
        """
        Returns a zero vector.
        :return: The zero vector.
        """
        return Vec2(0, 0)

    @staticmethod
    def cross(a, b):
        """
        Returns the cross product of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The cross product.
        """
        return a.x * b.y - a.y * b.x

    @staticmethod
    def up():
        """
        Returns a vector pointing up.
        :return: The vector.
        """
        return Vec2(0, 1)

    @staticmethod
    def down():
        """
        Returns a vector pointing down.
        :return: The vector.
        """
        return Vec2(0, -1)

    @staticmethod
    def right():
        """
        Returns a vector pointing right.
        :return: The vector.
        """
        return Vec2(1, 0)

    @staticmethod
    def left():
        """
        Returns a vector pointing left.
        :return: The vector.
        """
        return Vec2(-1, 0)

    @staticmethod
    def forward():
        """
        Returns a vector pointing forward.
        :return: The vector.
        """
        return Vec2(0, 1)

    @staticmethod
    def backward():
        """
        Returns a vector pointing backward.
        :return: The vector.
        """
        return Vec2(0, -1)

    @staticmethod
    def max(a: "Vec2", b: "Vec2"):
        """
        Returns the maximum of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The maximum vector.
        """
        return Vec2(max(a.x, b.x), max(a.y, b.y))

    @staticmethod
    def min(a: "Vec2", b: "Vec2"):
        """
        Returns the minimum of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The minimum vector.
        """
        return Vec2(min(a.x, b.x), min(a.y, b.y))

    def linear_lerp(self, other: "Vec2", t):
        """
        Returns a vector between two vectors.
        :param other: The other vector.
        :param t: The interpolation value.
        :return: The interpolated vector.
        """
        return Vec2(self.x + (other.x - self.x) * t, self.y + (other.y - self.y) * t)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Vec2(self.x // other, self.y // other)

    def __mod__(self, other):
        return Vec2(self.x % other, self.y % other)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __round__(self):
        return Vec2(round(self.x), round(self.y))

    def __floor__(self):
        return Vec2(floor(self.x), floor(self.y))

    def __ceil__(self):
        return Vec2(ceil(self.x), ceil(self.y))

    def __trunc__(self):
        return Vec2(trunc(self.x), trunc(self.y))

    def __index__(self):
        return self.x, self.y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return 2

    def __iter__(self):
        yield self.x
        yield self.y

    def __contains__(self, item):
        return item in (self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __nonzero__(self):
        return self.x != 0 or self.y != 0


# Vector3
class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __int__(self, other: "Vec3"):
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def distance(self, other: "Vec3"):
        """
        Returns the distance between two vectors.
        :param other: The other vector.
        :return: The distance.
        """
        return abs(self - other)

    def scale(self, other):
        """
        Returns the scaled vector.
        :param other: The scale value.
        :return: The scaled vector.
        """
        return Vec3(self.x * other, self.y * other, self.z * other)

    def reflect(self, other: "Vec3"):
        """
        Returns the reflected vector.
        :param other: The normal vector.
        :return: The reflected vector.
        """
        return self - other * 2 * self.dot(other)

    def angle_between(self, other: "Vec3"):
        """
        Returns the angle between two vectors.
        :param other: The other vector.
        :return: The angle.
        """
        return acos(self.dot(other) / (self.length() * other.length()))

    def normalize(self):
        """
        Returns the normalized vector.
        :return: The normalized vector.
        """
        return self / self.length()

    def dot(self, other: "Vec3"):
        """
        Returns the dot product of two vectors.
        :param other: The other vector.
        :return: The dot product.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        """
        Returns the length of the vector.
        :return: The length.
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


    def length_sqr(self):
        """
        Returns the length squared of the vector.
        :return: The length squared.
        """
        return self.x ** 2 + self.y ** 2 + self.z ** 2



    def linear_lerp(self, other: "Vec3", t):
        """
        Returns the linear interpolated vector.
        :param other: The other vector.
        :param t: The interpolation value.
        :return: The linear interpolated vector.
        """
        return self + (other - self) * t

    @staticmethod
    def cross(a, b):
        """
        Returns the cross product of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The cross product.
        """
        return Vec3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

    @staticmethod
    def up():
        """
        Returns the up vector.
        :return: The up vector.
        """
        return Vec3(0, 1, 0)

    @staticmethod
    def down():
        """
        Returns the down vector.
        :return: The down vector.
        """
        return Vec3(0, -1, 0)

    @staticmethod
    def left():
        """
        Returns the left vector.
        :return: The left vector.
        """
        return Vec3(-1, 0, 0)

    @staticmethod
    def right():
        """
        Returns the right vector.
        :return: The right vector.
        """
        return Vec3(1, 0, 0)

    @staticmethod
    def forward():
        """
        Returns the forward vector.
        :return: The forward vector.
        """
        return Vec3(0, 0, 1)

    @staticmethod
    def backward():
        """
        Returns the backward vector.
        :return: The backward vector.
        """
        return Vec3(0, 0, -1)

    @staticmethod
    def zero():
        """
        Returns the zero vector.
        :return: The zero vector.
        """
        return Vec3(0, 0, 0)

    @staticmethod
    def angle(a: "Vec3", b: "Vec3"):
        """
        Returns the angle between two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The angle.
        """
        return acos(a.dot(b) / (a.length() * b.length()))

    @staticmethod
    def max(a: "Vec3", b: "Vec3"):
        """
        Returns the maximum of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The maximum vector.
        """
        return Vec3(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z))

    @staticmethod
    def min(a: "Vec3", b: "Vec3"):
        """
        Returns the minimum of two vectors.
        :param a: The first vector.
        :param b: The second vector.
        :return: The minimum vector.
        """
        return Vec3(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z))

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Vec3(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Vec3(self.x // other, self.y // other, self.z // other)

    def __mod__(self, other):
        return Vec3(self.x % other, self.y % other, self.z % other)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __abs__(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __round__(self):
        return Vec3(round(self.x), round(self.y), round(self.z))

    def __floor__(self):
        return Vec3(floor(self.x), floor(self.y), floor(self.z))

    def __ceil__(self):
        return Vec3(ceil(self.x), ceil(self.y), ceil(self.z))

    def __trunc__(self):
        return Vec3(trunc(self.x), trunc(self.y), trunc(self.z))

    def __index__(self):
        return self.x, self.y, self.z

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return 3

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __contains__(self, item):
        return item in (self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __bool__(self):
        return self.x != 0 or self.y != 0 or self.z != 0

    def __nonzero__(self):
        return self.x != 0 or self.y != 0 or self.z != 0
