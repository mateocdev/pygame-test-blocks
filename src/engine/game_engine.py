import pygame


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
        pass

    def _calculate_time(self):
        pass

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        pass

    def _draw(self):
        """Color the screen"""
        self.screen.fill((0, 200, 128))
        """Clean the screen"""
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
