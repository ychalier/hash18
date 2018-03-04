from read import *

def getScore(vehicles, B):
    score = 0
    for v in vehicles:
        start = (0,0)
        time = 0
        for i in range(len(vehicles.rides)):
            ride = vehicles.rides[i]
            if time[i] - time < distance(ride.start, start):
                return False
            if time[i] < ride.earlier_start:
                return False
            else if time[i] + ride.distance <= ride.latest_finish:
                score += ride.distance
                if time[i] == ride.earlier_start:
                    score += B
            time += time[i] + ride.distance
            start = ride.finish
    return score
