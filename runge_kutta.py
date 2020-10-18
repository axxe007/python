## question 2.8.3 from nld book.
## one should write runge kutta method separately and then import in every code to use it.
## this way only writing one time is enough

## in this question intial condition is x(0) = 1, therefor
## for t = 0, we have x = 1

import matplotlib.pyplot as plt
from math import exp

def func(x,t):
    return (5*t**2-x)/(exp(x+t))

def rKutta_for(x,t, delta):
    k1 = delta*func(x,t)
    k2 = delta*func(x+(k1)/2, t + delta/2)
    k3 = delta*func(x+(1/2)*k2, t + delta/2)
    k4 = delta*func(x+k3, t + delta)

    return x + (k1 + 2*k2 + 2*k3 + k4)/6

def r_kutta_rev(x,t, delta):
    k1 = delta*func(x,t)
    k2 = delta*func(x-(k1)/2, t - delta/2)
    k3 = delta*func(x-(1/2)*k2, t - delta/2)
    k4 = delta*func(x-k3, t - delta)
    
    return x + (k1 + 2*k2 + 2*k3 + k4)/6

# will find the values till t = 5

t_start = 0
t_end = 5

delta = 0.01

x = [1]
t = [0]

while t_start < 5:
    new = rKutta_for(x[-1],t_start,delta)
    x.append(new)
    t.append(t_start+delta)
    if float(f'{t_start:.2f}')%1 == 0:
        print(f'Solving for t = {t_start:.2f} and found value of x = {new:.3f}')
    t_start+=delta

plt.plot(t,x)
plt.show()