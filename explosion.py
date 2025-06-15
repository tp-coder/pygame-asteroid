import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(255, 200, 50), max_radius=100, duration=0.8):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.max_radius = max_radius
        self.duration = duration
        self.elapsed = 0
        self.radius = 1
        self.alpha = 255
        self.position = pygame.Vector2(x, y)

    def update(self, dt):
        self.elapsed += dt
        progress = min(self.elapsed / self.duration, 1)
        self.radius = int(self.max_radius * progress)
        self.alpha = int(255 * (1 - progress))
        if self.elapsed >= self.duration:
            self.kill()

    def draw(self, screen):
        if self.alpha > 0:
            surface = pygame.Surface((self.max_radius*2, self.max_radius*2), pygame.SRCALPHA)
            pygame.draw.circle(surface, (*self.color, self.alpha), (self.max_radius, self.max_radius), self.radius)
            screen.blit(surface, (self.x - self.max_radius, self.y - self.max_radius)) 