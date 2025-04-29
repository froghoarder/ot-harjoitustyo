import pygame
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.collectible import Collectible
from sprites.frog import Frog
from sprites.enemy import Enemy


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
        self.points = 0
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.frog = None
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def move_frog(self, dx=0, dy=0):
        """moves the sprite frog

        Args:
            dx (int, optional): move horizontally by this amount. Defaults to 0.
            dy (int, optional): move vertivcally by this amount. Defaults to 0.
        """
        if not self._character_can_move(self.frog, dx, dy):
            if dx != 0 or dy != 0:
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
                elif dy > 0:
                    dy -= 1
                elif dy < 0:
                    dy += 1
                self.move_frog(dx, dy)

            return

        self.frog.rect.move_ip(dx, dy)

    def collect_stuff(self):
        """collect collectibles if the character is near enough and add up points

        """
        collected = pygame.sprite.spritecollide(
            self.frog, self.collectibles, True)

        if collected:
            self.points += 1

    def level_status(self):
        """checks the status of the level

        Returns:
            status (int): status of the level; 
                            0: 'normal', playing the level; 1: level cleared; 2: game over
        """
        status = 0
        if not self.collectibles:
            status = 1
        elif pygame.sprite.spritecollide(self.frog, self.enemies, False):
            status = 2
        return status

    def update_enemies(self, current_time):
        """updates enemy positions

        Args:
            current_time (int): time that has passed since starting the game
        """
        for enemy in self.enemies:
            if enemy.should_move(current_time):
                self._move_enemy(enemy)
                enemy.previous_move_time = current_time

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
                norm_y = y * self.cell_size + self.cell_size

                if cell == 0:
                    self.floors.add(Floor(norm_x, norm_y))
                elif cell == 1:
                    self.walls.add(Wall(norm_x, norm_y))
                elif cell == 2:
                    self.floors.add(Floor(norm_x, norm_y))
                    self.collectibles.add(Collectible(norm_x, norm_y))
                elif cell == 3:
                    self.floors.add(Floor(norm_x, norm_y))
                    self.frog = Frog(norm_x, norm_y)
                elif cell == 4:
                    self.floors.add(Floor(norm_x, norm_y))
                    self.enemies.add(Enemy(norm_x, norm_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.collectibles,
            self.frog,
            self.enemies
        )

    def _move_enemy(self, enemy):
        """moves an enemy

        Args:
            enemy (Enemy): enemy to be moved
        """
        dx, dy = enemy.get_direction()
        if not self._character_can_move(enemy, dx, dy):
            enemy.next_direction()
            self._move_enemy(enemy)
            return
        enemy.rect.move_ip(dx, dy)

    def _character_can_move(self, character, dx=0, dy=0):
        """checks whether the character will collide with a wall when moved

        Args:
            dx (int, optional): move horizontally by this amount. Defaults to 0.
            dy (int, optional): move vertically by this amount. Defaults to 0.

        Returns:
            True, if the character can move without colliding with a wall, if not, False
        """
        character.rect.move_ip(dx, dy)

        collision = pygame.sprite.spritecollide(character, self.walls, False)
        character_can_move = not collision

        character.rect.move_ip(-dx, -dy)

        return character_can_move
