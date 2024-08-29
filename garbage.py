import config
from entity import Entity
from garbage_type import GarbageType
import random


class Garbage(Entity):
    def __init__(self, x, garbage_type: GarbageType):
        self.speed = config.GARBAGE_SPEED
        self.garbage_type = garbage_type

        int = random.randint(1, config.COUNT_GARBAGE)

        super().__init__(config.GARBAGE_WIDTH,
                         config.GARBAGE_HEIGHT, x, -100, f"images/{garbage_type}_{int}.png")

    def move(self):
        self.y += self.speed
