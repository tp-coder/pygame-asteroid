import pygame
import sys
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.score = 0
        self.lives = 4

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
        pygame.draw.polygon(screen, (250, 149, 0), self.triangle(), width = 2)

    def rotate(self, dt, direction):
        self.rotation += direction * PLAYER_TURN_SPEED * dt
    
    def increase_score(self, points):
        self.score += points

    def move(self, dt, direction):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot_dir = pygame.Vector2(0,1).rotate(self.rotation)
        shots = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shots.velocity = shot_dir * PLAYER_SHOT_SPEED
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN

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
        # shoot
        if self.shot_cooldown <= 0:
            if keys[pygame.K_SPACE]:
                self.shoot(dt)
        self.shot_cooldown -= dt

    # lose life and respawn method
    def lose_life(self):
        self.lives -= 1
        if self.lives > 0:
            self.respawn()
        else:
            print("Game Over")
            pygame.quit()
            sys.exit()

    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        self.shot_cooldown = 0