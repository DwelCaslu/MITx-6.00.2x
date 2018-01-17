# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:57:14 2017

@author: .LUCAS
"""

import random, pylab

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    three_in_a_row = 0
    for i in range(numTrials):
        balls = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
        drawn_balls = []
        for i in range(3):
            drawn_ball = random.choice(balls)
            balls.remove(drawn_ball)
            drawn_balls.append(drawn_ball)
        if drawn_balls[0] == drawn_balls[1] and drawn_balls[1] == drawn_balls[2]:
            three_in_a_row += 1
    return three_in_a_row/float(numTrials)

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_runs = []
    for i in range(numTrials):
        last_roll = None
        run = 1
        longest_run = 1
        for i in range(numRolls):
            roll = die.roll()
            if roll == last_roll:
                run += 1
            else:
                run = 1
            if run > longest_run:
                longest_run = run
            last_roll = roll
        longest_runs.append(longest_run)
    makeHistogram(longest_runs, 10, "Longest run", "Number of trials")
    return sum(longest_runs)/float(len(longest_runs))
        
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))