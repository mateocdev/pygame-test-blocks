import json


class CEnemySpawner:
    def __init__(self, spawn_event_data: list):
        for i in spawn_event_data:
            self.time = i["time"]
            self.enemy_type = i["enemy_type"]
