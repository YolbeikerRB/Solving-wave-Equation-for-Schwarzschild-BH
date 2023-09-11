## v1.2:  Solving wave-like equation to compute wave function that gives the quasinormal modes
## Author: Yolbeiker Rodriguez Baez

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

##-----     DEFINING FUNCTIONS     -----
def rt_coor(r):
    # Give the tortoise coordinates (rt) from the radial coordinates (r)
    return r + np.log(r-1)

def r_coor(rt):
    # Give the radial coordinates (r) from the tortoise coordinates (rt)
    nexp  = np.exp(rt - 1)
    return np.real(1 + lambertw(nexp))

def RWPotential_r_cood(r, l):
    # Give the RW potential in radial coordinates (r)
    lam = l*(l+1)
    return (1-1.0/r)*(lam/r**2 - (6.0)/r**3)

def RWPotential_rt_cood(rt, l):
    # Give the RW potential in tortoise coordinates (rt)
    nexp  = np.exp(rt - 1)
    rcoor = np.real(1 + lambertw(nexp))
    return RWPotential_r_cood(rcoor, l)

def RWPotential_uv_cood(u, v, l):
    # Give the RW potential in light-cone coordinates (u, v)
    r_t = (v-u)/2.
    t_t = (v+u)/2.
    return RWPotential_rt_cood(r_t, l)

def Gaussian_func(grid):
    # Initial data (perturbation) on the spacetime
    return np.exp(-(grid-10.)**2/18.)

##-----     DEFINING DATA and GRID     -----
l      = 2.0
npoint = 2000
dx     = 0.1
x_coor = np.array(range(npoint))*dx

##----- Initializing the grid in (u,v) coordinates -----
grid   = np.zeros((npoint, npoint))

#--	Inidial data (perturbation) on the spacetime
grid[0]   = Gaussian_func(x_coor)
grid.T[0] = np.ones(npoint)*grid[0][0]

##-----    SOLVING WAVE EQUATION     -----
for i in range(1, npoint):
	for j in range(1, npoint):
		grid[i][j] = grid[i][j-1] + grid[i-1][j] - grid[i-1][j-1] - dx**2/8.*RWPotential_uv_cood(dx*(i-1), dx*(j-1), l)*(grid[i][j-1] + grid[i-1][j])

##-----     PLOT WAVE FUNCTION     -----
time_list = []
wave_list = []
for i, u in enumerate(np.arange(0, npoint)*dx):
    for j, v in enumerate(np.arange(0, npoint)*dx):
        t  = (v+u)/2.
        rc = (v-u)/2.
        if rc == 10.0:
            time_list.append(t)
            wave_list.append(np.log(abs(grid[i][j])))

plt.plot(time_list, wave_list, '.', color='C0', ms=2.5)
plt.xlabel('$time$', fontsize=18)
plt.ylabel('$\ln |\Psi |$', fontsize=20)
plt.tight_layout()
plt.show()
plt.close()