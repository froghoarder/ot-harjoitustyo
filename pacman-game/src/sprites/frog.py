import pygame
import os

directoryname = os.path.dirname(__file__)

class Frog(pygame.sprite.Sprite):
    """Class that creates and manages the sprite "frog"

    """

    def __init__(self, x=0, y=0):
        """constructor of this class, creates a new frog

        Args:
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(directoryname, "..", "pngs", "frog.png")
        )

        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
