import config
from entity import Entity
from garbage_type import GarbageType


class GarbageCan(Entity):
    def __init__(self, garbage_type: GarbageType):
        self.speed = config.GARBAGE_CAN_SPEED
        self.garbage_type = garbage_type

        super().__init__(config.GARBAGE_CAN_WIDTH, config.GARBAGE_CAN_HEIGHT, config.WIDTH // 2,
                         config.HEIGHT - config.GARBAGE_CAN_HEIGHT, f"images/{garbage_type}_garbage_can.png")

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < config.WIDTH - self.width:
            self.x += self.speed
