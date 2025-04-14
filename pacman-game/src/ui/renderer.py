import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Renderer:
    """class responsible for rendering the display of the game
    """

    def __init__(self, display, level):
        """constructor, initiates a new renderer

        Args:
            display (pygame.Surface): display of the game
            level (level.Level): current level and its information (map, sprites, etc.)
        """
        self._display = display
        self._level = level
        self._font = "Arial"
        self._font_size_small = 17
        self._font_size_large = 30
        self.__level_cleared = False
        self.__game_over = False

    def render(self):
        if self.__level_cleared:
            self._level_cleared_screen()
        elif self.__game_over:
            self._game_over_screen()
        else:
            self._level.all_sprites.draw(self._display)
            self._display_score()

        pygame.display.flip()

    def level_cleared(self):
        self.__level_cleared = True

    def game_over(self):
        self.__game_over = True

    def _create_text(self, font_size, text, color, position=None, centered=False):
        
        font = pygame.font.SysFont(self._font, font_size)
        text_surface = font.render(text, False, color)
        if centered:
            window = self._display.get_rect()
            position = text_surface.get_rect(center=window.center)
        self._display.blit(text_surface, position)

    def _display_score(self):
        score_position = (50, 10)
        score_height = 15
        score_width = 100
        score_area = pygame.Rect(
            score_position[0], score_position[1], score_width, score_height)
        self._display.fill(BLACK, score_area)

        
        text = f"SCORE: {self._level.points}"
        self._create_text(self._font_size_small, text, WHITE, score_position)

    def _level_cleared_screen(self):
        self._display.fill(BLACK)
        text = "Level cleared!"
        self._create_text(self._font_size_large, text, WHITE, centered=True)

    def _game_over_screen(self):
        ...

