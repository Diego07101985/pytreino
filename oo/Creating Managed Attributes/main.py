# You want to add extra processing(e.g., type checking or validation) to the getting or setting of an instance attribute.

# Don’t write properties that don’t actually add anything extra like this. For one, it makes your code more verbose and confusing to others.


import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
        # Deleter function (optional)

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    a = Person('Guido')
    # del a.first_name
    # a.first_name = 42

    c = Circle(4.0)
    print('Area = {0} ,  Radius {1} , Perimeter{2}'.format(
        c.area, c.radius, c.perimeter))

# Code repetition leads to bloated, error prone, and ugly code. As it turns out, there are much better ways
# to achieve the same thing using descriptors or closures. See Recipes
