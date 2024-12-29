import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius = 2):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # this will draw circles as asteroids on the screen
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)

    def update(self, dt):
        # this will update the position of the asteroids and make them move on a straight line
        self.position += self.velocity * dt
