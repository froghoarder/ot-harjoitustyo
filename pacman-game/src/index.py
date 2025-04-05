import pygame
from level import Level

LEVEL_1_MAP =   [[1,1,1,1],
                [1,3,0,1],
                [1,1,1,1]]

CELL_SIZE = 50


def main():
    level_map = LEVEL_1_MAP
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("f r o g.")

    level = Level(level_map, CELL_SIZE)

    pygame.init()
    level.all_sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
