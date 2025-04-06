import pygame

class Renderer:
    """class responsible for rendering the display of the game
    """
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)
        pygame.display.flip()