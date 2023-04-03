import json


class CEnemySpawner:
    def __init__(self, time, enemy_type, enemy_position, events, spawn_event_data):
        self.time = time
        self.enemy_type = enemy_type
        self.enemy_position = enemy_position
        self.events = events
        self.spawn_event_data = spawn_event_data
