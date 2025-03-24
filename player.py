import pygame
from constants import *
from circleshape import CircleShape
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # Ensure the player adds itself to the groups
        self.add(*self.containers)
    
    # Create the image (a surface) for the player
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Transparent placeholder
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.timer = 0  # Create a timer


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt): # Rotates player
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
    # Handle movement and rotation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Rotate counterclockwise
            self.rotate(dt * -1)
        if keys[pygame.K_d]:  # Rotate clockwise
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.move(dt * -1)
        shoot_pressed = keys[pygame.K_SPACE]
    
    # Rest of your code remains the same

    # Handle cooldown timer
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:  # Prevent negative values
                self.timer = 0

    # Handle shooting
        if shoot_pressed and self.timer <= 0:  # Check if shooting cooldown allows a shot
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN  # Reset the cooldown timer

        # Ensure rect matches position after all movement
        self.rect.center = self.position
    
    def shoot(self):
        # Create a new shot at the player's position
        new_shot = Shot(self.position.x, self.position.y)

        # Set the shot's velocity based on player direction
        # Start with a vector pointing up
        shot_direction = pygame.Vector2(0, 1)  # Note: In Pygame, negative y is up

        # Rotate it to match the player's direction
        shot_direction = shot_direction.rotate(self.rotation)

        # Scale it by the shot speed
        new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
