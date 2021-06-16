import math
from sympy import *                                                                                              
x = symbols('x')
a = integrate(x**2, (x, 0, 1))
print(float(a))
# Out[2]: -1/2 + exp(2)/2