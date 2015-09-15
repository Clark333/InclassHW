__author__ = 'DanielClarkJR'
import pylab as plt
import numpy as np
import scipy.integrate as sp
# dfasdf jlfdsasdf
LAMBDA = 1
A = 1

def RHS(u = np.asarray([1,2]), Lambda=0, a=1):
    Udot1 = u[1, :]
    Udot2 = -u[0, :] + (Lambda/(a-u[0, :]))
    return Udot1, Udot2

# plotting information
numx = 10
numv = 10
u1all = np.linspace(-10, 10, numx)
u2all = np.linspace(-10, 10, numv)
u1, u2 = np.meshgrid(u1all, u2all)
u1.shape = (numx*numv,1)
u2.shape = (numx*numv,1)
u = np.asarray([u1,u2])

# Evaluating the function
Udot1, Udot2 = RHS(u = u, Lambda=LAMBDA, a=A)

# plotting the quiver
plt.figure()
plt.quiver(u1, u2, Udot1, Udot2)
plt.xlabel('u(t)', fontsize=20)
plt.ylabel('$\dot{u}$(t)', fontsize=20)
plt.grid()

# Plotting some solutions
def solve_hw2(max_time=1.0, Lambda = .1, a = 1, x0 = np.array([[-1, -.9 , -0.9, -1, -1]]).T, v0 = np.array([[1, 1, .9, 0.9, 1]]).T, plotnow = 1):
    def hw2_deriv(x1_x2, t, a=a, Lambda = Lambda):
        """Compute the time-derivative of a SDOF system."""
        x1, x2 = x1_x2
        #print(x2)
        #print(-x1+(Lambda/(a-x1)))
        return [x2, -x1+(Lambda/(a-x1))]
    x0 = np.concatenate((x0, v0), axis = 1)
    N = x0.shape[0]
    # Solve for the trajectories
    t = np.linspace(0, max_time, int(250*max_time))
    x_t = np.asarray([sp.odeint(hw2_deriv, x0i, t)
                      for x0i in x0])
    if plotnow == 1:
        #fig = plt.figure()
        #plt.axis((-1.4,1.4,-1.2,1.2))
        for i in range(N):
            x, v = x_t[i,:,:].T
            plt.plot(x, v,'-')
            #Let's plot '*' at the end of each trajectory.
            plt.plot(x[-1],v[-1],'*')
        plt.grid('on')
    # Just in case we want to pull and plot.
    return t, x_t
numx = 20
numv = 20
x = np.linspace(-10, 10, numx)
v = np.linspace(-10, 10, numv)
x0, v0 = np.meshgrid(x, v)
x0.shape = (numx*numv,1) # Python array trick to reorganize numbers in an array
v0.shape = (numx*numv,1) # The matrices are now "vectors" (1 column)
_,_ = solve_hw2(max_time=.05, Lambda = LAMBDA, a = A, x0 = x0, v0 = v0)

# Showing the plot
plt.show()
