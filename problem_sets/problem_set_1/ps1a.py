###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    # TODO: Your code here
    with open(filename, "r", newline="") as file:
        content = file.readlines()
        cows = {}
        for line in content:
            line = line.strip()
            name, weight = line.split(",")
            cows[name] = int(weight)
        return cows

        



# Problem 2
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
    # TODO: Your code here
    sorted_cows = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    limit_copy = limit
    trips = []
    taken = set()
    while len(sorted_cows.keys()) > len(taken):
        trip = []
        for name, weight in sorted_cows.items():
            if limit - weight >= 0:
                if name not in taken:
                    trip.append(name)
                    taken.add(name)
                    limit -= weight
                else:
                    continue
            else:
                limit = limit_copy
                break
        trips.append(trip)
    return trips



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    # TODO: Your code here
    best = None
    for partition in get_partitions(cows.keys()):
        valid = True
        for trip in partition:
            if sum((cows[name] for name in trip)) > limit:
                valid = False
                break
        if valid:
            if best is None or len(best) > len(partition):
                best = partition
    return best




    
        
# Problem 4
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
    # TODO: Your code here
    filename = "problem_sets/problem_set_1/ps1_cow_data.txt"
    cows = load_cows(filename=filename)
    greedy_start = time.time()
    greedy_cow_transport(cows=cows)
    greedy_end = time.time()
    brute_start = time.time()
    brute_force_cow_transport(cows=cows)
    brute_end = time.time()

    greedy_delta = greedy_end - greedy_start
    brute_delta = brute_end - brute_start

    print(f"Greedy: {greedy_delta}\nBrute: {brute_delta}")

    percent_slower = ((brute_delta - greedy_delta) / greedy_delta) * 100
    print(f"{round(percent_slower)}" + "%")


if __name__ == "__main__":
    compare_cow_transport_algorithms()
