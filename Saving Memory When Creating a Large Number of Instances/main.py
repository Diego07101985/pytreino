class Date:
    __slots__ = ['year', 'month', 'day']
    # Attribute names listed in the __slots__ specifier are internally mapped to specific indices within this array.
    #To give you an idea, storing a single Date instance without slots requires 428 bytes of memory on a 64-bit version of Python.
    #  If slots is defined, it drops to 156 bytes.

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
