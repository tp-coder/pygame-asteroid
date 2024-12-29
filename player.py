import pygame
from circleshape import CircleShape
import constants
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        # print(f"triangle points: {a}, {b}, {c}")
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width = 2)

    def rotate(self, dt, direction):
        self.rotation += direction * constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt, direction):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += direction * forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        # gets the key pressed on the keyboard
        keys = pygame.key.get_pressed()

        # move horiontally
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # move left
            self.rotate(dt, -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # move right
            self.rotate(dt, 1)
        # move vertically
        if keys[pygame.K_w] or keys[pygame.K_UP]: # move up
            self.move(dt, 1)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # move down
            self.move(dt, -1)
