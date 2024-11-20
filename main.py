import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def rotate_z(self, angle_z):
        x = self.x
        y = self.y
        angle_cos = math.cos(angle_z)
        angle_sin = math.sin(angle_z)

        self.x, self.y = x * angle_cos - y * angle_sin, x * angle_sin + y * angle_cos

    def rotate_x(self, angle_x):
        y = self.y
        z = self.z
        angle_cos = math.cos(angle_x)
        angle_sin = math.sin(angle_x)

        self.y, self.z = y * angle_cos - z * angle_sin, y * angle_sin + z * angle_cos

    def rotate_y(self, angle_y):
        z = self.z
        x = self.x
        angle_cos = math.cos(angle_y)
        angle_sin = math.sin(angle_y)

        self.z, self.x = z * angle_cos - x * angle_sin, z * angle_sin + x * angle_cos

    def length(self):
        return abs((self.x ** 2 + self.y ** 2 + self.z ** 2)) ** 0.5

    def angle_cos(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z) / (self.length() * other.length())

class Face:
    def __init__(self, ver):
        self.ver = ver[:]

    def rotate_x(self, angle_x):
        for v in self.ver:
            v.rotate_x(angle_x)

    def rotate_y(self, angle_y):
        for v in self.ver:
            v.rotate_y(angle_y)

    def rotate_z(self, angle_z):
        for v in self.ver:
            v.rotate_z(angle_z)

    def normal(self):
        ver1 = self.ver[0]
        ver2 = self.ver[1]
        ver3 = self.ver[2]

        v1 = Point(ver1.x - ver2.x, ver1.y - ver2.y, ver1.z - ver2.z)
        v2 = Point(ver1.x - ver3.x, ver1.y - ver3.y, ver1.z - ver3.z)

        return Point(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x)

    def isVisible(self, other):
        return self.normal().angle_cos(other) > 0
    

view = Point(10, 10, 10)
v1 = Point(1, 2, 3)
v2 = Point(-2, 3, 4)
v3 = Point(5, -1, 5)
face_int = Face([v1, v2, v3])

print(face_int.isVisible(view))

v4 = Point(1.1, 2.2, 3.3)
v5 = Point(3.5, 7.8, 0.0)
v6 = Point(0.0, 1.2, 4.4)
face_float = Face([v4, v5, v6])

print(face_float.isVisible(view))