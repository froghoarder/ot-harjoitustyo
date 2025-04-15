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
            self._collect()
            self._check_level()
            self._render()
            self._clock.tick(60)

    def _events(self):
        """handles the events: arrow keys and quitting
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                self._event_keydown(event)
            if event.type == pygame.KEYUP:
                self._event_keyup(event)
            #button stuff
            elif event.type == pygame.QUIT:
                self._running = False

    def _event_keydown(self, event):
        """handles keys being pressed

        Args:
            event (pygame.event): event being handled
        """
        if event.key in (pygame.K_LEFT, pygame.K_a):
            self._left = True
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self._right = True
        if event.key in (pygame.K_UP, pygame.K_w):
            self._up = True
        if event.key in (pygame.K_DOWN, pygame.K_s):
            self._down = True

    def _event_keyup(self, event):
        """handles keys being released

        Args:
            event (pygame.event): event being handled
        """
        if event.key in (pygame.K_LEFT, pygame.K_a):
            self._left = False
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self._right = False
        if event.key in (pygame.K_UP, pygame.K_w):
            self._up = False
        if event.key in (pygame.K_DOWN, pygame.K_s):
            self._down = False

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

    def _collect(self):
        """collect collectibles, if applicable
        """
        self._level.collect_stuff()

    def _check_level(self):
        """checks the status of the level(normal, level completed, game over)
        """

        level_status = self._level.level_status()
        if level_status == 1:
            self._renderer.level_cleared()
        elif level_status == 2:
            self._renderer.game_over()

    def _render(self):
        self._renderer.render()
