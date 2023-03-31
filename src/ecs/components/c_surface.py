import pygame


class CSurface(pygame.Surface):
    def __init__(self, size: pygame.Vector2, color: pygame.Color):
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
