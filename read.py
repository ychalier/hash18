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


class Ride:
    def __init__(self, line):
        split = line.split(" ")
        self.start = int(split[0]), int(split[1])
        self.finish = int(split[2]), int(split[3])
        self.earlier_start = int(split[4])
        self.latest_finish = int(split[5])


def read_file(filename):
    file_object = open(filename, 'r')
    inp = Input(file_object.readline())
    for line in file_object.readlines():
        ride = Ride(line)
        inp.rides.append(ride)
    file_object.close()
    return inp


print(read_file("a_example.in"))
