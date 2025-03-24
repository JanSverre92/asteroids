import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
    # Update position based on velocity and time
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt