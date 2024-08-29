from enum import Enum


class GarbageType(Enum):
    WHITE = 1
    GREEN = 2
    BLACK = 3

    def __str__(self):
        return self.name.lower()
