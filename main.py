import config
import pygame
import random

from garbage_can import GarbageCan
from garbage import Garbage
from garbage_type import GarbageType

pygame.init()

background_image = pygame.image.load("images/background_2.webp")
background_image = pygame.transform.scale(background_image, (config.WIDTH, config.HEIGHT))

DISPLAY = pygame.display.set_mode([config.WIDTH, config.HEIGHT])
FONT = pygame.font.SysFont("Cute", 25)

playing = True
clock = pygame.time.Clock()

time = 0
count = 0
points = 0

garbage_can = GarbageCan(GarbageType.WHITE)
garbages: list[Garbage] = []


def move(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        garbage_can.move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        garbage_can.move_right()


def gen_garbage():
    pos = config.GARBAGE_POSITIONS

    random.shuffle(pos)

    garbages.append(Garbage(pos[0], GarbageType.WHITE))
    garbages.append(Garbage(pos[1], GarbageType.GREEN))
    garbages.append(Garbage(pos[2], GarbageType.BLACK))


while playing:

    DISPLAY.blit(background_image, (0, 0))

    time += clock.tick(config.FPS)
    if time > config.GEN_GARBAGE_TIME and count < config.COUNT_GEN_GARBAGE:
        gen_garbage()
        count += 1
        time = 0

    move(pygame.key.get_pressed())

    events = pygame.event.get()
    for evento in events:
        if evento.type == pygame.QUIT:
            playing = False

    garbage_can.draw(DISPLAY)
    for garbage in garbages:
        garbage.draw(DISPLAY)

        if garbage.colliderect(garbage_can):
            if garbage.garbage_type == garbage_can.garbage_type:
                points += 1
            garbages.remove(garbage)

        elif garbage.y > config.HEIGHT:
            garbages.remove(garbage)

        garbage.move()

    text_points = FONT.render(f"Puntos: {points}", True, "white")
    DISPLAY.blit(text_points, (20, 20))

    if len(garbages) == 0 and count == config.COUNT_GEN_GARBAGE:
        playing = False

    pygame.display.update()


pygame.quit()

quit()
