import pygame
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.frog import Frog


class Level:
    """class responsible for creating and updating the current level of the game
    """

    def __init__(self, level_map, cell_size=50):
        """creates a new level

        Args:
            level_map (list): list of lists of integers that describe the composition of the level
            cell_size (int): size of cells in pixels
        """

        self.cell_size = cell_size
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.frog = None
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def move_frog(self, dx=0, dy=0):
        """moves the sprite frog

        Args:
            dx (int, optional): move horizontally by this amount. Defaults to 0.
            dy (int, optional): move vertivcally by this amount. Defaults to 0.
        """
        if not self._character_can_move(dx, dy):
            if dx != 0 or dy != 0:
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
                elif dy > 0:
                    dy -= 1
                elif dy < 0:
                    dy += 1
                print(dx, dy)
                self.move_frog(dx, dy)
               
            return

        self.frog.rect.move_ip(dx, dy)

    def _initialize_sprites(self, level_map):
        """initializes the sprites of the level

        Args:
            level_map (list): list of lists of integers that describe the composition of the level
        """
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(norm_x, norm_y))
                elif cell == 1:
                    self.walls.add(Wall(norm_x, norm_y))
                elif cell == 3:
                    self.floors.add(Floor(norm_x, norm_y))
                    self.frog = Frog(norm_x, norm_y)

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.frog
        )

    def _character_can_move(self, dx=0, dy=0):
        """checks whether the character will collide with a wall when moved

        Args:
            dx (int, optional): move horizontally by this amount. Defaults to 0.
            dy (int, optional): move vertically by this amount. Defaults to 0.

        Returns:
            True, if the character can move without colliding with a wall, if not, False
        """
        self.frog.rect.move_ip(dx, dy)

        collision = pygame.sprite.spritecollide(self.frog, self.walls, False)
        character_can_move = not collision

        self.frog.rect.move_ip(-dx, -dy)

        return character_can_move
        
