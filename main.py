# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	clock = pygame.time.Clock() # Create a clock object
	dt = 0
	running = True
	
	# Existing groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# Set containers for each class
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots,updatable, drawable)

	#Create instances
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while running:  # This is your infinite loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
    # Fill the screen with black
		screen.fill((0, 0, 0))  # RGB for black
		updatable.update(dt)
	# Check for collisions
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
			if asteroid.collision(player):
				sys.exit("Game over!")
	# Draws the different shapes
		for entity in drawable:
			entity.draw(screen)
	
    # Update the display
		pygame.display.flip()
		dt = clock.tick(60) / 1000	

if __name__ == "__main__":
    main()

