# question 2.8.3 from nld book.
# one should write runge kutta method separately and then import in every code to use it.
# this way only writing one time is enough

# in this question intial condition is x(0) = 1, therefor
# for t = 0, we have x = 1

#question changed to different equation, which was looking sexy
'''
verbose = Truewill output results of each iteration with values of x
and t at that iteration
'''

import matplotlib.pyplot as plt
from math import exp


def func(x, t):
    return 10*(x+t)**2


def rKutta_for(x, t, delta):
    k1 = delta*func(x, t)
    k2 = delta*func(x+(k1)/2, t + delta/2)
    k3 = delta*func(x+(1/2)*k2, t + delta/2)
    k4 = delta*func(x+k3, t + delta)

    return x + (k1 + 2*k2 + 2*k3 + k4)/6



#new info is that use directly negative delta
'''
def rKutta_rev(x,t, delta):
    k1 = delta*func(x,t)
    k2 = delta*func(x + (k1)/2, t - delta/2)
    k3 = delta*func(x + (1/2)*k2, t - delta/2)
    k4 = delta*func(x + k3, t - delta)
    
    return x + (k1 + 2*k2 + 2*k3 + k4)/6
'''
# will find the values till t = 5


def solve(initial_x, initial_t, final_t, delta, verbose = False):
    x = [initial_x]
    t = [initial_t]

    while initial_t < final_t:
        new = rKutta_for(x[-1], initial_t, delta)
        x.append(new)
        t.append(initial_t+delta)

        if float(f'{initial_t:.2f}') % 1 == 0 and verbose==True:
            print(f'Solving for t = {initial_t:.2f} and found value of x = {new:.3f}')
        initial_t += delta
    '''
    Sorry to say i am unable to make reverse part of this
    if rev == True:
        x_rev = [initial_x]
        t_rev = [initial_rev_t]
        while initial_rev_t > -final_t:
            new_rev = rKutta_rev(x[-1], initial_rev_t, delta)
            x_rev.append(new_rev)
            t_rev.append(initial_rev_t-delta)

            if float(f'{initial_rev_t:.2f}') % 1 == 0 and verbose == True:
                print(f'Solving for t = {initial_rev_t:.2f} and found value of x = {new_rev:.3f}')
            initial_rev_t = initial_rev_t - delta
        
        x.reverse()
        x.extend(x_rev)
        x.reverse()
        t.reverse()
        t.extend(t_rev)
        t.reverse()
    '''
    return x , t


def main():
    x,t = solve(-1,0,1.1,0.01,verbose=True)
    plt.scatter(t,x)
    plt.show()

if __name__ == '__main__':
    main()
