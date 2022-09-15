# solving nonlinear equations
# import the library to solve problems
from scipy.optimize import fsolve
import math
# write down the equations
def equations(p):
    x,y,t = p
    return (9.55-x*math.exp(-x*t),9.73-y*math.exp(-y*t), 17.21-(x+y)*math.exp(-(x+y)*t))        

x, y,t =  fsolve(equations, (.001, .001,0.001))
print (x, y,t)
