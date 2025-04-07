import pygame


class GameLoop:
    """class responsible for creating a new game loop, and for
        reading the user's input, updating the status of the game based on this input
        and updating the display inside this loop
    """

    def __init__(self, level, cell_size, renderer, event_queue, clock):
        self._level = level
        self._cell_size = cell_size
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.running = True

    def start(self):
        """starts and runs the game loop
        """
        while self.running:
            self._events()

            self._render()
            self._clock.tick(60)

    def _events(self):
        """handles the events
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_frog(dx=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._level.move_frog(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self._level.move_frog(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._level.move_frog(dy=self._cell_size)
            elif event.type == pygame.QUIT:
                self.running = False

    def _move_character(self):
        """moves the character
        """

    def _render(self):
        self._renderer.render()
