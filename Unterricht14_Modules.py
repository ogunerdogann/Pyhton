# We can import libraries(modules) with 'import' command
#Consider a module to be the same as a code library.

#import math
#result = math.factorial(6)
#print(result)                   # prints 720

# We don't have to import the whole libraries
# If we need just a small part of a library, we can import just the part that we need.

#from math import factorial
#result = factorial(5)
#print(result)                    # prints 120

#from math import factorial,sqrt
#print(sqrt(36))                   # prints 6.0

# We can also import the all functions in a module.
# In this case, we do not import the whole module,
# but we import all the functions in it.

#from math import *
#result = sqrt(36)
#print(result)           # prints 6.0

# Lets import our module

#import My_Module1
#result = My_Module1.area_circle(2)
#print(result)            # prints 12.56

from My_Module1 import perimeter_circle
result = perimeter_circle(3)
print(result)             # prints 




