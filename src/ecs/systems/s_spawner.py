import esper
from src.create.prefab_creator import create_square
from src.ecs.components.c_enemySpawner import CEnemySpawner
from src.ecs.components.c_transform import CTransform
import json
import pygame

"""Read the square data from the json file"""
square = open("assets/cfg/enemies.json")
data_square = json.load(square)


def system_spawner(world: esper.World):
    component = world.get_component(CEnemySpawner)
    c_e: CEnemySpawner
    for entity, (c_e) in component:
        for i in data_square:
            if i == c_e.enemy_type:
                create_square(world, pygame.Vector2(
                    data_square[i]["size"]["x"], data_square[i]["size"]["y"]), pygame.Vector2(c_e.enemy_position["x"], c_e.enemy_position["y"]), pygame.Vector2(data_square[i]["velocity_min"], data_square[i]["velocity_max"]), pygame.Color(
                    data_square[i]["color"]["r"], data_square[i]["color"]["g"], data_square[i]["color"]["b"]))
