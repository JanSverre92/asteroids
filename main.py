# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	# Inside your main() function, after creating the screen
	running = True
	while running:  # This is your infinite loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
    # Fill the screen with black
		screen.fill((0, 0, 0))  # RGB for black
    
    # Update the display
		pygame.display.flip()

if __name__ == "__main__":
    main()

