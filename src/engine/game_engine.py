import pygame
import esper
import json

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.create.prefab_creator import create_square

window = open("assets/cfg/window.json")
data = json.load(window)

"""Read the square data from the json file"""
square = open("assets/cfg/enemies.json")
data_square = json.load(square)


"""Read the square level data from the json file"""
square_level = open("assets/cfg/level_01.json")
data_square_level = json.load(square_level)


spawn = open("assets/cfg/level_01.json")
data_spawn = json.load(spawn)
for i in data_spawn["enemy_spawn_events"]:
    print(i["enemy_type"])


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
        for i in data_square:
            create_square(self.ecs_world, pygame.Vector2(
                data_square[i]["size"]["x"], data_square[i]["size"]["y"]), pygame.Vector2(0, 0), pygame.Vector2(data_square[i]["velocity_min"], data_square[i]["velocity_max"]), pygame.Color(
                data_square[i]["color"]["r"], data_square[i]["color"]["g"], data_square[i]["color"]["b"]))

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
