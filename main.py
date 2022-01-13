# Project #2
# See requirements in gClassroom
# Clear and readable code is the best code
# Student Name: Jayden Diaz

### DEPENDENCIES ###
import pygame
import sys, math
from quick_geometry_formulas import *

pygame.init()

### CONSTANTS ###

WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)

# order of points are tip, left edge, right edge
camera_points = [(400, 300), (385, 340), (415, 340)]
### Important Functions



## Main code

# We start with a 2D base, the 3D comes with a little math

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      sys.exit()
      quit()
  
  # Test drawings, remove later
  pygame.draw.polygon(screen, (255, 255, 255), polygon_points)
  pygame.display.flip()
  clock.tick(40)
