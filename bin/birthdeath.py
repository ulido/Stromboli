"""
Simple birth-death process example using Stromboli.
"""
import stromboli

vol = 1.
sigma = 100.*vol
mu = 1./vol
print sigma/mu

ssA = sigma/mu

A = stromboli.Species(int(ssA))

birth = stromboli.Reaction([],[(1,A)],sigma)
death = stromboli.Reaction([(1,A)],[],mu)

algo = stromboli.Algorithm([birth,death])

from pylab import subplot,draw,ion,ioff,show

ion()
ax = subplot(111)
times = [0.]
An = [A.number]
cond = True
while cond:
    for i in range(1000):
        try:
            times.append(algo.step())
        except RuntimeError:
            cond = False
            break
        An.append(A.number)

    ax.clear()
    ax.plot(times,An)
    ax.axhline(ssA, color='r')
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of A")
    draw()

ioff()
show()
