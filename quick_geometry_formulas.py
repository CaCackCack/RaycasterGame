import math
import sympy as sym

# shape is in form of list of tuples e.g [(1,1), (2,1), (1,0), (2,0)]
# angle is in degrees
# def rotate_shape(shape, angle): 


def line_distance(first_point, second_point):
  return math.sqrt( (second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2) 

# undefined is represented by None in this program
def line_slope(first_point, second_point):
  if (second_point[0] - first_point[0] == 0):
    return None
  elif (second_point[1] - first_point[1] == 0):
    return 0
  else:
    return (second_point[1] - first_point[1])/(second_point[0] - first_point[0])


def line_midpoint(first_point, second_point):
  return ( (first_point[0] + second_point[0])/2, (first_point[1] + second_point[1])/2 )


def find_equation(coord_pair, slope, array_form):


  if (slope == 0):
    intercept = coord_pair[1]
    print("y = {0}".format(intercept))
    return
  elif (slope == None):
    intercept = coord_pair[0]
    print("x = {0}".format(intercept))
    return
  else:
    intercept = coord_pair[1] - (coord_pair[0] * slope)


  # Array form useful for conversion into standard form
  if (array_form == True):
    if (slope == 0):
      return [0, 1, intercept]
    elif (slope == None):
      return [1, 0, intercept]
    else:
      return [slope, 1, intercept]
  else:
    if (intercept >= 0):
      print("y = {0}x + {1}".format(slope, intercept))
      return
    else:
      print("y = {0}x - {1}".format(slope, intercept))


def find_perpendicular(slope):
  if (slope == 0):
    return None
  elif (slope == None):
    return 0 
  else:
    return -(1/slope)

def find_perp_bisector(first_point, second_point):
  # This function finds the perpendicular bisector between two points, using funcs made previously
  midpoint = line_midpoint(first_point, second_point)
  slope = line_slope(first_point, second_point)
  return find_equation(midpoint, -(1/slope)) 

def find_perp_equation(x, y, m, array_form):
  # returns the perpendicular equation of a given line
  if (array_form == True):
    return [find_perpendicular(x), y, m] 

  else:
    if (m >= 0):
      print("{0}y = {1}x + {2}".format(y, find_perpendicular(x), m))
    else:
      print("{0}y = {1}x - {2}".format(y, find_perpendicular(x), m))


def find_hyp(a, b):
 return math.sqrt((a**2) + (b**2)) 

def find_tri_area(a, b, c): 
  # finds area of triangle using Heron's formula
  semi = (a+b+c)/2 
  return math.sqrt(semi * (semi - a) * (semi - b) * (semi - c) )


def r_tri_check(a, b, c):
  if (a**2) + (b**2) != (c**2):
    print("This thing fake, bro.")


def find_point_section(first_point, second_point, ratio):
  # I coded this half a year ago and can't remember what for, but kept it here anyway.
  # separtions aren't necessary, but good for code readability
  first_numerator = (ratio[0] * second_point[0]) + (ratio[1] * first_point[0])  
  second_numerator = (ratio[0] * second_point[1]) + (ratio[1] * first_point[1]) 
  return ( first_numerator/(ratio[0]+ratio[1]), second_numerator/(ratio[0] + ratio[1]))


def slope_intercept_to_standard(x, y, b):
  # x and y are the coeffients of the said variables, for example 5y = 3x + 8 would be inputted as (3, 5, 8) 
  if (x == 0):
    return [0, 1, b]
  elif (y == 0):
    return [x, 0, b]
  else:
    return [x, -y, -b]



