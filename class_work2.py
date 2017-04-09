# def print_delim():
#       print  ("**************")
#
#
# def pretty_print(value):
#       print_delim()
#       print ("Value =", value)
#       print_delim()
#
#
# def square_rect(width,height):
#       result = width*height
#       return result
# def square_square(width):
#       result = square_rect(width,width)
#       return result
# print_delim()
#
#
# square = square_rect(12,10)
# pretty_print(square)
# print_delim()
#
# square2 = square_square(4)
# pretty_print(square2)
# print_delim()
#
# print_delim()
#
# def add_and_multiply(a,b):
#       sum  = a + b
#       mult = a * b
#       return sum, mult
# result1, result2 = add_and_multiply(2,3)
# pretty_print(result1)
# pretty_print(result2)

# def celsium_to_fareng (degrees):
#       result = (degrees * 1.8)+32
#       return result
#
# v = celsium_to_fareng(36.6)
# print(v)



def square_of_cyrcle (r):
      import math
      result = (math.pi * r ** 2)
      return result

radius = square_of_cyrcle(3)
print(radius)

