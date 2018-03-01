class Input:
    def __init__(self, line):
        split = line.split(" ")
        self.R = int(split[0])
        self.C = int(split[1])
        self.F = int(split[2])
        self.N = int(split[3])
        self.B = int(split[4])
        self.T = int(split[5])
        self.rides = []

    def __str__(self):
        s = str(self.R) + " rows\n" + str(self.C) + " columns\n" + str(self.F)\
            + " vehicules\n" + str(self.N) + " rides\n" + str(self.B)\
            + " bonus\n" + str(self.T) + " steps\n"
        for ride in self.rides:
            s += str(ride) + "\n"
        return s


class Ride:
    def __init__(self, line, id_):
        split = line.split(" ")
        self.id = id_
        self.start = int(split[0]), int(split[1])
        self.finish = int(split[2]), int(split[3])
        self.earlier_start = int(split[4])
        self.latest_finish = int(split[5])
        self.distance = distance(self.start, self.finish)

    def __str__(self):
        return "ride from " + str(self.start) + " to " + str(self.finish)\
               + ", earliest start " + str(self.earlier_start)\
               + ", latest finish " + str(self.latest_finish)

    def __repr__(self):
        return str(self.id)


class Vehicule:
    def __init__(self, id_):
        self.id = id_
        self.pos = 0, 0
        self.rides = []
        self.time = 0

    def add_ride(self, ride):
        self.time += ride.distance
        self.pos = ride.finish
        self.rides.append(ride)

    def time_for_ride(self, ride):
        return self.time + distance(self.pos, ride.start)

    def __str__(self):
        return str(self.rides)

    def __repr__(self):
        return self.__str__()


def distance(start, finish):
    return abs(start[0] - finish[0]) + abs(start[1] - finish[1])


def read_file(filename):
    file_object = open(filename, 'r')
    inp = Input(file_object.readline())
    index = 0
    for line in file_object.readlines():
        ride = Ride(line, index)
        index += 1
        inp.rides.append(ride)
    file_object.close()
    return inp

