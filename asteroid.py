import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius = 2):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # this will draw circles as asteroids on the screen
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)

    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            rotate_angle = random.uniform(20, 50)
            first_asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            second_asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            first_asteroid.velocity = pygame.Vector2.rotate(self.velocity, rotate_angle) * 1.2
            second_asteroid.velocity = pygame.Vector2.rotate(self.velocity, -rotate_angle) * 1.2

    def update(self, dt):
        # this will update the position of the asteroids and make them move on a straight line
        self.position += self.velocity * dt
        self.wrap_around_screen()
    # make the asteroids wrap around the screen
    def wrap_around_screen(self):
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def get_points(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            return 100
        elif self.radius > ASTEROID_MIN_RADIUS and self.radius <= ASTEROID_MIN_RADIUS * 2:
            return 75
        else:
            return 50
