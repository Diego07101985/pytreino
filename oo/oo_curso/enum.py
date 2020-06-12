from enum import Enum


class Directions(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')
    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.down))
    print(move(Directions.up))
