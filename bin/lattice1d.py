"""Compartment model for diffusion, where each lattice site is represented as a
stromboli species and the system is simulated using a Gillespie-type algorithm.
"""
import stromboli
from numpy import arange,exp

# Number of lattice sites
K = 101
# Diffusion constant
D = 100.
# Lattice spacing
h = 1.
# Initial number of particles in the middle compartment
N = 10000

# Setup the system
d = D/h**2
species = [stromboli.Species(0,"A"+str(i)) for i in range(K)]
species[50].number = N
reactions = [stromboli.Reaction([(1,species[i])],[(1,species[i+1])],d) for i in range(K-1)] + [stromboli.Reaction([(1,species[i])],[(1,species[i-1])],d) for i in range(1,K)]
algo = stromboli.Algorithm(reactions)

from pylab import subplot,draw,ion,ioff,show

ion()
ax = subplot(111)
cond = True
while cond:
    time = 0.
    for i in range(10000):
        try:
            time = algo.step()
        except RuntimeError:
            cond = False
            break

    ax.clear()
    ax.plot(N*exp(-(arange(K)-50)**2/(4.*D*time))/(4*3.14*D*time)**0.5, label="Exact distribution")
    ax.plot(arange(K)*h,[s.number for s in species], label="Solution of SSA")
    ax.legend(loc="upper left")
    ax.set_xlabel("Position x")
    ax.set_ylabel("Number of particles at t=%g" % time)
    draw()

ioff()
show()
