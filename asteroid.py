import random
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create new velocity vectors by rotating the current one
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create new asteroids with the correct parameters
        new_asteroid1 = Asteroid(
            x=self.position.x,  # Extract x coordinate from position vector
            y=self.position.y,  # Extract y coordinate from position vector
            radius=new_radius
        )
        # Assign the velocity after creation
        new_asteroid1.velocity = new_velocity1 * 1.2
        
        new_asteroid2 = Asteroid(
            x=self.position.x,
            y=self.position.y,
            radius=new_radius
        )
        new_asteroid2.velocity = new_velocity2 * 1.2