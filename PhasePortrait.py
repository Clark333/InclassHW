__author__ = 'DanielClarkJR'
import pylab as plt
import numpy as np

LAMBDA = 1
A = 1

def potentialFunction(u = np.asarray([1,2]), Lambda=0, a=1):
    potential = (0.5)* (u[0, :]**2) + Lambda*np.log(np.abs(a - u[0, :] ) )
    return potential

def mechanicalFunction(u = np.asarray([1,2]), potential= np.asarray([1,2])):
    kinetic = (1/2)*(u[1, :]**2)
    return kinetic + potential

numx = 100
numv = 100
u1all = np.linspace(-5, 5, numx)
u2all = np.linspace(-5, 5, numv)
u1, u2 = np.meshgrid(u1all, u2all)
u1.shape = (numx*numv,1)
u2.shape = (numx*numv,1)
u = np.asarray([u1,u2])

mechanicalEnergy = mechanicalFunction(u=u, potential = potentialFunction(u=u , Lambda=LAMBDA, a=A) )

u1 = u1.reshape(numx, numx)
u2 = u2.reshape(numx, numx)

mechanicalEnergy = mechanicalEnergy.reshape(numx, numx)
plt.figure()
plt.contour(u1, u2, mechanicalEnergy,30)
plt.xlabel('u(t)', fontsize=20)
plt.ylabel('$\dot{u}$(t)', fontsize=20)
plt.show()
