from read import *


def output(vehicules, filename):
    file = open('out/' + filename, 'w')
    for vehicule in vehicules:
        tmp = str(len(vehicule.rides))
        for ride in vehicule.rides:
            tmp += " " + str(ride.id)
        file.write(tmp + "\n")
    file.close()


def compute_file_basic(filename):
    inp = read_file('in/' + filename)
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
        vehicules[min_index].add_ride_basic(ride)
    output(vehicules, filename[:-3] + ".out")


def compute_file_advanced(filename):
    print("Computing file " + filename)
    inp = read_file('in/' + filename)
    inp.rides.sort(key=lambda x: -x.latest_finish)
    vehicules = [Vehicule(i) for i in range(inp.F)]

    # Ajout des premiers rides
    for i in range(inp.F):
        vehicules[i].add_ride_advanced(inp.rides[i])

    # Ajout des suivants
    for i in range(inp.F, inp.N):
        ride = inp.rides[i]
        print(i)
        max_index = -1
        max_margin = None
        for j in range(inp.F):

            # Si le vehicule peut prendre la course
            if vehicules[j].can_add(ride):
                margin = vehicules[j].get_margin(ride)
                if max_margin is None or margin < max_margin:
                    max_margin = margin
                    max_index = j

        if max_index >= 0:  # On peut poser la course directement
            vehicules[max_index].add_ride_advanced(ride)
        else:  # Il va falloir decaller
            tries = 0
            while tries < inp.F:
                max_index = -1
                max_margin = None
                for j in range(inp.F):
                    margin = vehicules[j].get_margin(ride)
                    if max_margin is None or margin < max_margin:
                        max_margin = margin
                        max_index = j

                if vehicules[max_index].can_push(ride):
                    vehicules[max_index].push_ride(ride)

                tries += 1
    output(vehicules, filename[:-3] + ".out")


for f in ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in",\
          "d_metropolis.in", "e_high_bonus.in"]:
    compute_file_advanced(f)
