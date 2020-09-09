#pygame template
import pygame
import random
from settings import *

#initilize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

#Game loop
running = True
while running:
	# Keep loop running at right speed
	clock.tick(FPS)
	#process input
	for event in pygame.event.get():
		#3check for closin window
		if event.type == pyame.QUIT:
			running = False

	# Updtade
	all_sprites.update()

	#draw render
	