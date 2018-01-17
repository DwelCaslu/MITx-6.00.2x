# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:08:56 2017

@author: .LUCAS
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.
    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
    The global variable CURRENTRABBITPOP is modified by this procedure.
    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    
    p_rabbit = 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)
    for rabbit in range(CURRENTRABBITPOP):
        if random.random()<p_rabbit:
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.
    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.
    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).
    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
    If it does not eat a rabbit, then with a 1/10 prob it dies.
    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    p_eat = CURRENTRABBITPOP/float(MAXRABBITPOP)
    
    for fox in range(CURRENTFOXPOP):
        if random.random()<p_eat:
            if CURRENTRABBITPOP > 10:
                p_fox = 1/3.0
                CURRENTRABBITPOP -= 1
                if random.random()<p_fox:
                    CURRENTFOXPOP += 1
        else:
            p_die = 9/10.0
            if random.random()<p_die:
                if CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.
    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.
    Both lists should be `numSteps` items long.
    """
    rabbit_pop = []
    fox_pop = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_pop.append(CURRENTRABBITPOP)
        fox_pop.append(CURRENTFOXPOP)
    return (rabbit_pop, fox_pop)
    
numsteps = 200
pops = runSimulation(numsteps)
#print(pops)
pylab.plot(range(numsteps), pops[0])
pylab.plot(range(numsteps), pops[1])
pylab.show()

coeffr = pylab.polyfit(range(numsteps), pops[0], 2)
coefff = pylab.polyfit(range(numsteps), pops[1], 2)
pylab.plot(pylab.polyval(coeffr, range(numsteps)))
pylab.plot(pylab.polyval(coefff, range(numsteps)))
pylab.show()