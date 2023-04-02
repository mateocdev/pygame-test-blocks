import esper
from src.create.prefab_creator import create_square
from src.ecs.components.c_enemySpawner import CEnemySpawner
from src.ecs.components.c_transform import CTransform
import json
import pygame

"""Read the square data from the json file"""
square = open("assets/cfg/enemies.json")
data_square = json.load(square)


def system_spawner(world: esper.World, delta_time: float):
    components = world.get_components(CEnemySpawner, CTransform)

    c_e: CEnemySpawner
    c_t: CTransform
    for entity, (c_e, c_t) in components:
        c_e.time -= delta_time
        if c_e.time <= 0:
            world.delete_entity(entity)
            for i in data_square:
                if i == c_e.enemy_type:
                    create_square(world, pygame.Vector2(
                        data_square[i]["size"]["x"], data_square[i]["size"]["y"]), c_t.pos, pygame.Vector2(data_square[i]["velocity_min"], data_square[i]["velocity_max"]), pygame.Color(
                        data_square[i]["color"]["r"], data_square[i]["color"]["g"], data_square[i]["color"]["b"]))
            c_e.time = c_e.spawn_time
