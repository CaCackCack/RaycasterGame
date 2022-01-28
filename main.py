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


# finds center of player shape
# finds slope and midpoint of each vertice-midpoint line on the longer sides, 
# then the intercept of them all
def player_center(player):
  left_mid = line_midpoint(player[0], player[1])
  right_mid = line_midpoint(player[0], player[2])
 

  left_mid_slope = line_slope(left_mid, player[2])
  right_mid_slope = line_slope(right_mid, player[1])
  
  

  left_mid_line = find_equation(player[2], left_mid_slope, True)
  right_mid_line = find_equation(player[1], right_mid_slope, True)
 

 

  standard_left_mid_line = slope_intercept_to_standard(left_mid_line[0], left_mid_line[1], left_mid_line[2])
  standard_right_mid_line = slope_intercept_to_standard(right_mid_line[0], right_mid_line[1], right_mid_line[2])


  lines = sym.Matrix([standard_left_mid_line, standard_right_mid_line])

 
  return (float(lines.rref()[0].row(0).col(2)[0]), float(lines.rref()[0].row(1).col(2)[0]))

  



# rotates the player using SOHCAHTOA
# divides x coordinate by radius to find angle, then adds or subtracts increment of 5 to it depending on direction
# calculates the position of point at incremented angle, then appends to new set of points
# fially, new set is returned


# direction; 1 is left, 0 is right
# TODO: Fix odd shrinking problem
def rotate_player(player, direction):
  increment = math.pi/36 # radian equivalent of 5 degrees
  full_circle = 2 * math.pi # radian equivalent of 360 degrees
  
  center = player_center(player)
  print(player)
  print(center)
  new_player = []

  for point in player:
    radius = line_distance(point, center)
    if (center[1] > point[1]):
      point_sin = (center[1] - point[1])/radius
    else:
      point_sin = (point[1] - center[1])/radius
    print(point_sin)
    while (point_sin > 1):
      point_sin -= 1
    print(point_sin)
    point_angle = math.asin(point_sin)

    if (direction == 1):
      if ((point_angle+increment) > math.pi * 2):
        new_angle = (point_angle+increment) - math.pi * 2
      else:
        new_angle = point_angle + increment
    else:
      if ((point_angle-increment) < 0):
        new_angle = 2 * math.pi + (point_angle-increment)
      else:
        new_angle = point_angle-increment
    print("The angle was {}".format(math.degrees(point_angle)))
    print("The angle is now {}".format(math.degrees(new_angle)))
    
    
    # finding a working algorithm for this part was hell — all credit goes to MBo on Stack Overflow
    new_x = center[0] + (center[0] - point[0]) * math.cos(new_angle) - (center[1] - point[1]) * math.sin(new_angle)
    new_y = center[1] + (center[0] - point[0]) * math.sin(new_angle) + (center[1] - point[1]) * math.cos(new_angle)
    new_point = (new_x, new_y)
    new_player.append(new_point)
  print("\n")
  

  return new_player





## Main code

# We start with a 2D base, the 3D comes with a little math

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      sys.exit()
      quit()
    elif (event.type == pygame.KEYDOWN):
      if (event.key == pygame.K_a):
        camera_points = rotate_player(camera_points, 1)
      elif (event.key == pygame.K_d):
        camera_points = rotate_player(camera_points, 0)
      
  
 
  screen.blit(background, (0, 0))
  pygame.draw.polygon(screen, (255, 255, 255), camera_points)
  pygame.display.flip()
  clock.tick(40)

