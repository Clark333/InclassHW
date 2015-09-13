__author__ = 'DanielClarkJR'
# i know you said you wanted to use matlab but this was easy. The code was basically there in the notes.
# we can work on making it better this saturday. just in case you don't have my number its 513-673-8799


#%pylab inline # included if you want to open in the journal thing
import pylab as pl
import numpy as np
import scipy.integrate as sp
from matplotlib.legend_handler import HandlerLine2D


def solve_sdof(max_time=10.0,Lambda=1,a=2,x0=5,v0=0):

    def problem_one(x1_x2,Lambda=Lambda,a=a):
        """Compute the time-derivative of a SDOF system."""
        u1, u2 = x1_x2
        return [u2, -u1+(Lambda/(a-u1))]

    x0i=(x0, v0)
    # Solve for the trajectories
    t = np.linspace(0, max_time, int(250*max_time))
    x_t = sp.odeint(problem_one, x0i, t)
    x, v = x_t.T

    return t, x, v
def F_of_U( x=[1,2,3], a = 1, Lambda=1):
    f = (1/2) * x**2 + Lambda*np.log(np.absolute(a-x))
    return f


# Start of figure and function calls


# Case 1 a^2 - 4lambda > 0
t, x, v = solve_sdof(max_time=5, Lambda=0, a=1, x0=5, v0=0)
pl.figure()
pl.plot(x,F_of_U(x=x,a=1,Lambda=0))
pl.show()

pl.figure()
line1, = pl.plot(x, v, label='$\lambda = 0, a = 1$')

# Case 2 a^2 - 4lambda = 0
t, x, v = solve_sdof(max_time=5, Lambda= 1, a=2, x0= 5, v0=0)
line2, = pl.plot(x, v, label='$\lambda = 1, a = 2$')

# Case 3 a^2 - 4lambda < 0
t, x, v = solve_sdof(max_time = 5, Lambda = 1, a = 1, x0 = 5, v0 = 0)
line3, = pl.plot(x, v, label='$\lambda = 1, a = 1$')

# Plotting information
pl.xlabel('$u(t)$', fontsize=30)
pl.ylabel('$\dot u(t)$', fontsize=30)
pl.title('$u(t)$ vs $\dot u(t)$, $u_0$ = 5, $\dot u_0$ = 0', fontsize=30)
pl.grid()
pl.legend(handler_map={line1: HandlerLine2D(numpoints=4)},loc=4)
pl.show()



#lambdaList = [0, 1.5, 1, 4, 1, 1.5]
#aList = [1.0, 3, 2.0, 4, 1.0, 2]
#print(len(aList) )

## dummy case
#t, x, v = solve_sdof(max_time=5, Lambda=0, a=1, x0=5, v0=0)
#tlist = np.zeros((len(t), len(aList)))
#xlist = np.zeros((len(t), len(aList)))
#vlist = np.zeros((len(t), len(aList)))

#print(len(tlist))

#print( xlist[:][1] )


#for i in range( len(aList)  ) :
#    tlist[i][:], xlist[:][i], vlist[:][i] = solve_sdof(max_time=5, Lambda=lambdaList[i], a=aList[i], x0=5, v0=0)
#
#print(tlist)
