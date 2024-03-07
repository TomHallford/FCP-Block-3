import math


class Vector:
    def __init__(self, vector):
        self.x = vector[0]
        self.y = vector[1]

    def vector_length(self):
        return math.sqrt((self.x**2)+(self.y**2))

    def vector_addition(self, x, y):
        return [(self.x + x), (self.y + y)]

    def dot_product(self, x, y):
        return (self.x*x)+(self.y*y)


def main():
    vector1 = Vector([3, 4])
    vector2 = Vector([1, 2])
    print(vector1.vector_length())
    print(vector1.vector_addition(vector2.x, vector2.y))
    print(vector1.dot_product(vector2.x, vector2.y))


if __name__ == "__main__":
    main()
    