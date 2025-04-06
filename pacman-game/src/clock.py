import pygame

class Clock:
    """internal clock of the game
    """
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """ticks the clock

        Args:
            fps (int): frames per second
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """gets and returns ticks of the clock
        """
        return pygame.time.get_ticks()
