import os
import random
import pygame

directoryname = os.path.dirname(__file__)
IMAGE_NAME = "dog.png"


class Enemy(pygame.sprite.Sprite):
    """Class that creates and manages an enemy
    """

    def __init__(self, x=0, y=0):
        """constructor of this class, creates a new enemy

        Args:
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
        """
        super().__init__()

        self.previous_move_time = 0
        self.movement_options = [(1,0), (-1,0), (0,1), (0,-1)]
        self.movement_index = 0

        self.image = pygame.image.load(
            os.path.join(directoryname, "..", "pngs", IMAGE_NAME)
        )
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def should_move(self, current_time):
        """determines if the enemy should move 

        Args:
            current_time (int): current time

        Returns:
            bool: whether a set time has passed since the last movement or not
        """
        return current_time - self.previous_move_time >= 10

    def get_direction(self):
        """gets the movement direction of the sprite
        """
        return self.movement_options[self.movement_index]

    def next_direction(self):
        self.movement_index = random.randint(0,3)


