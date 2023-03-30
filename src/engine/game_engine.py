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
        """Create the velocity"""
        self.vel_cuad = pygame.Vector2(50, 50)
        """Create the game objects"""
        self.pos_cuad = pygame.Vector2(0, 0)
        size_cuad = pygame.Vector2(50, 50)
        col_cuad = pygame.Color(255, 255, 255)

        """Create surface"""
        self.surf_cuad = pygame.Surface(size_cuad)
        """Fill surface"""
        self.surf_cuad.fill(col_cuad)

    def _calculate_time(self):
        """Calculate delta time"""
        self.delta_time = self.clock.tick(self.framerate) / 1000

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        self.pos_cuad.x += self.vel_cuad.x * self.delta_time
        self.pos_cuad.y += self.vel_cuad.y * self.delta_time

        """Check if the square is out of the screen"""
        screen_rect = self.screen.get_rect()
        cuad_rect = self.surf_cuad.get_rect(topleft=self.pos_cuad)

        if cuad_rect.left <= 0 or cuad_rect.right >= screen_rect.width:
            self.vel_cuad.x *= -1
            cuad_rect.clamp_ip(screen_rect)
            self.pos_cuad.x = cuad_rect.x

        if cuad_rect.top <= 0 or cuad_rect.bottom >= screen_rect.height:
            self.vel_cuad.y *= -1
            cuad_rect.clamp_ip(screen_rect)
            self.pos_cuad.y = cuad_rect.y

    def _draw(self):
        """Color the screen"""
        self.screen.fill((0, 0, 0))

        """Draw the surface"""
        self.screen.blit(self.surf_cuad, self.pos_cuad)
        """Clean the screen"""
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
