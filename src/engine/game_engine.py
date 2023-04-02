import pygame
import esper
import json
from src.ecs.components.c_enemySpawner import CEnemySpawner

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.create.prefab_creator import create_square
from src.ecs.systems.s_spawner import system_spawner

window = open("assets/cfg/window.json")
data = json.load(window)

"""Read the square data from the json file"""
square = open("assets/cfg/enemies.json")
data_square = json.load(square)


"""Read the square level data from the json file"""
spawn = open("assets/cfg/level_01.json")
data_spawn = json.load(spawn)


class GameEngine:
    def __init__(self) -> None:
        pygame.init()

        title = data.get("title")
        size = data.get("size")
        framerate = data.get("framerate")

        """Create the game window and the clock"""
        self.screen = pygame.display.set_mode(
            (size.get("w"), size.get("h")), pygame.SCALED)
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.is_running = False
        """Set framerate"""
        self.framerate = framerate
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
        for i in data_spawn["enemy_spawn_events"]:
            spawn_entity = self.ecs_world.create_entity()
            self.ecs_world.add_component(spawn_entity, CEnemySpawner(
                i["time"], i["enemy_type"], i["position"]))

        system_spawner(self.ecs_world)

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
        background = data.get("bg_color")
        """Color the screen"""
        self.screen.fill(
            (background.get("r"), background.get("g"), background.get("b")))
        system_rendering(self.ecs_world, self.screen)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
