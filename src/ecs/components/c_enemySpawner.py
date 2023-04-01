
import pygame
import json


class SpawnEventData:
    def __init__() -> None:
        spawn = open("assets/cfg/level_01.json")
        data_spawn = json.load(spawn)

        return data_spawn


class CEnemySpawner:
    def __init__(self, spawn: SpawnEventData, type: any) -> None:
        self.spawn = spawn
