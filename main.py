# Project #2
# See requirements in gClassroom
# Clear and readable code is the best code
# Student Name: Jayden Diaz
# Main Issues: Math and TypeErrors galore!


### DEPENDENCIES ###
import pygame
import sys
from quick_geometry_formulas import *
import sympy as sym

pygame.init()

### CONSTANTS ###
WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)
# Since undefined slopes are incalculable, we just use a very high number
UNDEFINED = 500**10

# order of points are tip, left edge, right edge
camera_points = [(400, 300), (385, 340), (415, 340)]
### Important Functions

# rotates the camera using trigonometric calculations
# function takes the slope between the two edges
# draws a perpendicular line through the edge it wants to turn toward
# then a parallel line through the tipaad
# the intersection of these can be treated as a point
# From that point on, it's just SOHCAHTOA

# finds center of player shape
# finds slope and midpoint of each vertice-midpoint line, then the intercept of them all
def player_center(player):
  left_mid = line_midpoint(player[0], player[1])
  right_mid = line_midpoint(player[0], player[2])
  back_mid = line_midpoint(player[1], player[2])


  left_mid_slope = line_slope(left_mid, player[2])
  right_mid_slope = line_slope(right_mid, player[1])
  back_mid_slope = line_slope(back_mid, player[0])
  
 

  left_mid_line = find_equation(player[2], left_mid_slope, True)
  right_mid_line = find_equation(player[1], right_mid_slope, True)
  back_mid_line = find_equation(player[0], back_mid_slope, True)

 

  standard_left_mid_line = slope_intercept_to_standard(left_mid_line[0], left_mid_line[1], left_mid_line[2])
  standard__right_mid_line = slope_intercept_to_standard(right_mid_line[0], right_mid_line[1], right_mid_line[2])
  standard_back_mid_line = slope_intercept_to_standard(back_mid_line[0], back_mid_line[1], back_mid_line[2])

  lines = sym.Matrix([standard_left_mid_line, standard_right_mid_line, standard_back_mid_line])

  

player_center(camera_points)







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
  pygame.draw.polygon(screen, (255, 255, 255), camera_points)
  pygame.display.flip()
  clock.tick(40)

