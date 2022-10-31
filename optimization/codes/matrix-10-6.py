import numpy as np
import matplotlib.pyplot as plt
#import cvxpy  as cp

import sys, os
sys.path.insert(0,'/sdcard/ramesh/maths/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)
def f(x,a,b,c):
  return x**4 + a * x**3 + b*x**2 + c*x +d
a =1
b =1
c = 0
d=2
label_str = "$x^4 + x^3+x^2+2$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0
min_x = -1
max_x = 1

#Defining derivative of f(x)
df = lambda x: 4*x**3+3*a*x**2+2*b*x+c            

#Gradient ascent calculation
while ((previous_step_size > precision) and (iters < max_iters) and (cur_x >= min_x) and( cur_x <= max_x) ) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x) 
    iters+=1
    min_val = f(cur_x,a,b,c)
print("Maximum value of f(x) is ", min_val, "at","x =",cur_x)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

#Gradient descent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1     
max_val = f(cur_x,a,b,c)
print("Miniimum value of f(x) is ", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,a,b,c)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'Q({cur_x:.4f},{max_val:.4f})')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('/sdcard/ramesh/maths/CoordGeo/figs6.pdf')
#subprocess.run(shlex.split("termux-open  /sdcard/ramesh/maths/CoordGeo/figs6.pdf"))
