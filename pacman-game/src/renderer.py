import pygame


class Renderer:
    """class responsible for rendering the display of the game
    """

    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)
        self._display_score()

        pygame.display.flip()

    def _display_score(self):
        score_position = (50, 10)
        score_height = 15
        score_width = 100
        score_area = pygame.Rect(
            score_position[0], score_position[1], score_width, score_height)
        self._display.fill((0, 0, 0), score_area)

        font = pygame.font.SysFont("Arial", 17)
        text = f"SCORE: {self._level.points}"
        text_surface = font.render(text, False, (255, 255, 255))
        self._display.blit(text_surface, score_position)
