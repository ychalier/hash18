from read import *


def output(vehicules, filename):
    file = open(filename, 'w')
    for vehicule in vehicules:
        tmp = str(len(vehicule.rides))
        for ride in vehicule.rides:
            tmp += " " + str(ride.id)
        file.write(tmp + "\n")
    file.close()


def compute_file(filename):
    inp = read_file(filename)
    inp.rides.sort(key=lambda x: x.earlier_start)
    vehicules = [Vehicule(i) for i in range(inp.F)]
    for ride in inp.rides:
        min_index = 0
        minimum = vehicules[0].time_for_ride(ride)
        for i in range(1, inp.F):
            current_value = vehicules[i].time_for_ride(ride)
            if current_value < minimum:
                min_index = i
                minimum = current_value
        vehicules[min_index].add_ride(ride)
    output(vehicules, filename[:-3] + ".out")

compute_file("a_example.in")
compute_file("b_should_be_easy.in")
compute_file("c_no_hurry.in")
compute_file("d_metropolis.in")
compute_file("e_high_bonus.in")


