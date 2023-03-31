import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface


def system_rendering(word: esper.World, screen: pygame.Surface):
    components = word.get_components(CTransform, CSurface)
    c_t: CTransform
    c_s: CSurface
    for entity, (c_t, c_s) in components:
        screen.blit(c_s.surf, c_t.pos)
