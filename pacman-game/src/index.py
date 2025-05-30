import pygame
from entities.level import Level
from entities.gameloop import GameLoop
from entities.event_queue import EventQueue
from entities.clock import Clock
from ui.renderer import Renderer

LEVEL_1_MAP = [[1, 1, 1, 1, 1, 1],
               [1, 2, 0, 2, 2, 1],
               [1, 0, 1, 1, 2, 1],
               [1, 3, 0, 0, 2, 1],
               [1, 1, 1, 1, 1, 1]]

LEVEL_2_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 2, 0, 1, 2, 2, 4, 2, 2, 1],
               [1, 2, 1, 1, 1, 0, 1, 1, 1, 2, 1],
               [1, 2, 0, 0, 2, 0, 2, 2, 2, 3, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50


def main():
    level_map = LEVEL_2_MAP
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * CELL_SIZE + CELL_SIZE
    display_width = width * CELL_SIZE

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("frog game")

    level = Level(level_map, CELL_SIZE)
    renderer = Renderer(display, level)
    event_queue = EventQueue()
    clock = Clock()
    game_loop = GameLoop(level, CELL_SIZE, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
