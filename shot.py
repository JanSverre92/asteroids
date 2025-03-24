import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x ,y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 0)
    
    def update(self, dt):
    # Update position based on velocity and time
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt