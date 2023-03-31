import pygame
import esper

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.create.prefab_creator import create_square


class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        """Create the game window and the clock"""
        self.screen = pygame.display.set_mode((640, 360), pygame.SCALED)
        pygame.display.set_caption("Game Engine")

        self.clock = pygame.time.Clock()
        self.is_running = False
        """Set framerate"""
        self.framerate = 60
        """Set delta time"""
        self.delta_time = 0

        self.ecs_world = esper.World()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        create_square(self.ecs_world, pygame.Vector2(50, 50),
                      pygame.Vector2(0, 0), pygame.Vector2(100, 100), pygame.Color(255, 255, 255))
        create_square(self.ecs_world, pygame.Vector2(50, 250),
                      pygame.Vector2(150, 300), pygame.Vector2(-200, 300), pygame.Color(255, 100, 100))

    def _calculate_time(self):
        """Calculate delta time"""
        self.delta_time = self.clock.tick(self.framerate) / 1000

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        """Color the screen"""
        self.screen.fill((0, 0, 0))
        system_rendering(self.ecs_world, self.screen)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
