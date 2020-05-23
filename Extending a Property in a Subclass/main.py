class Person:
    def __init__(self, name):
        self.name = name
        # Getter function

    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

# Here is an example of a class that inherits from Person and extends the name property with new functionality:


# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name

#     @name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)

#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self)

class SubPerson(Person):

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


if __name__ == '__main__':
    s = SubPerson('Guido')
    print(s.name)
    s.name = 'Larry'
    print(s.name)
    s.name = 42
    print(s.name)
