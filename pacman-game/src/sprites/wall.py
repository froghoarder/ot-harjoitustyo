import os
import pygame

directoryname = os.path.dirname(__file__)


class Wall(pygame.sprite.Sprite):
    """Class that creates and manages the sprite "wall"

    """

    def __init__(self, x=0, y=0):
        """constructor of this class, creates a new piece of wall

        Args:
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(directoryname, "..", "pngs", "wall.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
