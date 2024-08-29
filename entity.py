import pygame


class Entity(pygame.Rect):
    def __init__(self, width: int, height: int, x: int, y: int, image_path: str):
        super().__init__(x, y, width, height)
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.width, self.height))

    def draw(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))
