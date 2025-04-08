import pygame

MOVEMENT_SPEED = 4

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
        self._running = True

        self._up = False
        self._down = False
        self._left = False
        self._right = False

    def start(self):
        """starts and runs the game loop
        """
        while self._running:
            self._events()
            self._move_character()
            self._render()
            self._clock.tick(60)

    def _events(self):
        """handles the events: arrow keys and quitting
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._left = True
                if event.key == pygame.K_RIGHT:
                    self._right = True
                if event.key == pygame.K_UP:
                    self._up = True
                if event.key == pygame.K_DOWN:
                    self._down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self._left = False
                if event.key == pygame.K_RIGHT:
                    self._right = False
                if event.key == pygame.K_UP:
                    self._up = False
                if event.key == pygame.K_DOWN:
                    self._down = False
            elif event.type == pygame.QUIT:
                self._running = False

    def _move_character(self):
        """moves the character
        """
        if self._left:
            self._level.move_frog(dx=-MOVEMENT_SPEED)
        if self._right:
            self._level.move_frog(dx=MOVEMENT_SPEED)
        if self._up:
            self._level.move_frog(dy=-MOVEMENT_SPEED)
        if self._down:
            self._level.move_frog(dy=MOVEMENT_SPEED)

    def _render(self):
        self._renderer.render()
