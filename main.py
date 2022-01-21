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
# finds slope and midpoint of each vertice-midpoint line on the longer sides, 
# then the intercept of them all
def player_center(player):
  left_mid = line_midpoint(player[0], player[1])
  right_mid = line_midpoint(player[0], player[2])
 

  left_mid_slope = line_slope(left_mid, player[2])
  right_mid_slope = line_slope(right_mid, player[1])
  
  
  print(player[0])

  left_mid_line = find_equation(player[2], left_mid_slope, True)
  right_mid_line = find_equation(player[1], right_mid_slope, True)
 

 

  standard_left_mid_line = slope_intercept_to_standard(left_mid_line[0], left_mid_line[1], left_mid_line[2])
  standard_right_mid_line = slope_intercept_to_standard(right_mid_line[0], right_mid_line[1], right_mid_line[2])


  lines = sym.Matrix([standard_left_mid_line, standard_right_mid_line])

  return (float(lines.rref()[0].row(0).col(2)[0]), float(lines.rref()[0].row(1).col(2)[0]))

  



# rotates the player using SOHCAHTOA
# divides x coordinate by radius to find angle, then adds or subtracts increment of 5 to it depending on direction
# calculates the position of point at incremented angle, then appends to new set of points
# finally, new set is returned


# direction; 1 is left, 0 is right
def rotate_player(player, direction):
  increment = math.pi/36 # radian equivalent of 5 degrees
  full_circle = 2 * math.pi # radian equivalent of 360 degrees

  center = player_center(player)
  
  new_player = []

  for point in player:
    cos_ratio = point[0]/line_distance(point, center)
    while (cos_ratio > 1):
      cos_ratio -= 1
    angle = math.acos(cos_ratio)
    if (direction == 1):
      if (angle + increment > full_circle):
        new_angle = (angle + increment) - full_circle
      else:
        new_angle = angle + increment
    elif (direction == 0):
      if (angle - increment < 0):
        new_angle = full_circle - (angle - increment)
      else:
        new_angle = angle - increment


    new_point = (center[0] + ( ((point[0] - center[0]) * math.cos(new_angle - angle)) - ((point[1] - center[1]) * math.sin(new_angle - angle)),
                center[1] + ( ((point[0] - center[0]) * math.sin(new_angle - angle)) + ((point[1] - center[1]) * math.sin(new_angle - angle)))))
    print(new_point)
    new_player.append(new_point)
    
    
  return new_player


rotate_player(camera_points, 1)


## Main code

# We start with a 2D base, the 3D comes with a little math

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      sys.exit()
      quit()
    elif (event.type == pygame.KEYDOWN):
      if (event.key == pygame.K_a):
        camera_points = rotate_player(camera_points, 1)
    
      
  
  # Test drawings, remove later
  pygame.draw.polygon(screen, (255, 255, 255), camera_points)
  pygame.display.flip()
  clock.tick(40)

