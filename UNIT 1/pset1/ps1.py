###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:
 
    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows
 
    Does not mutate the given dictionary of cows.
 
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
 
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #create local copy of cows
    #greedy_cows = sorted(cows, key=lambda x:cows.get(x), reverse=True)
    master = []
    processed = len(cows.keys())
    greedy_cows = sorted(cows, key=lambda x:cows.get(x), reverse=True)
    cows_processed = {}
    for cow in greedy_cows:
        cows_processed[cow] = False
    while processed > 0:
        manifest = []
        total = 0
        for cow in greedy_cows:
            if not cows_processed[cow] and (cows[cow] + total <= limit):
                manifest.append(cow)
                total += cows[cow]
                cows_processed[cow] = True
                processed -= 1
        master.append(manifest)
    return master


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
 
    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
 
    Does not mutate the given dictionary of cows.
 
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
 
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def isFit(cows, partitions, limit):
        for p in partitions:
            total = 0
            for c in p:
                total += cows[c]
                if total > limit:
                    return False
        return True
 
    master = []
    for partition in get_partitions(cows.keys()):
        #print(partition)
        if isFit(cows, partition, limit):
            master.append(partition)
    if len(master) == 0:
        return []
 
    master.sort(key = lambda x:len(x))
    #print("Sorted: " + str(master))
    return master[0]
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
 
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.
 
    Returns:
    Does not return anything.
    """
    cows = {'Maggie':3,'Herman':7,'Betsy':9,'Oreo':6,'Moo Moo':3,'Milkshake':2,'Millie':5,'Lola':2,\
'Florence':2,'Henrietta':9}
	#cows = load_cows('ps1_cow_data.txt')
    gc_begin = time.time()
    gct = greedy_cow_transport(cows)
    gc_end = time.time()
    bft = brute_force_cow_transport(cows)
    bft_end = time.time()
    print('Greedy: Trips= ' + str(len(gct)) + ' Run Time= ' + str(gc_end-gc_begin))
    print('Brute : Trips= ' + str(len(bft)) + ' Run Time= ' + str(bft_end-gc_end))
 
 
"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
compare_cow_transport_algorithms()


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


