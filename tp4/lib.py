from data import distances, cities

def getDistance(city, otherCity):
    '''Returns distances between city and otherCity 
    Require data package'''

    return distances[city][otherCity]

def getTotalDistance(chr):
    '''Return the total distance from a road (list of int)
    Require data package'''

    s = 0

    for x in range(len(chr)):
        if x == len(chr) - 1:
            s += getDistance(chr[x], chr[0])
        else:
            s += getDistance(chr[x], chr[x + 1])

    return 0 - s

def roadMaker(pattern):
    pattern = list(str(pattern).replace('[', '').replace(']', ''))
    while len(pattern) < len(distances):
        pattern.insert(0, '0')

    return pattern
