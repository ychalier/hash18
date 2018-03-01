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
    print("Computing file " + filename)
    inp = read_file(filename)
    inp.rides.sort(key=lambda x: -x.latest_finish)
    vehicules = [Vehicule(i) for i in range(inp.F)]

    # Ajout des premiers rides
    for i in range(inp.F):
        vehicules[i].add_ride(inp.rides[i])

    # Ajout des suivants
    for i in range(inp.F, inp.N):
        ride = inp.rides[i]

        max_index = -1
        max_margin = None
        for j in range(inp.F):

            # Si le vehicule peut prendre la course
            if vehicules[i].can_take(ride):
                margin = vehicules[i].margin_if_added(ride)
                if margin < max_margin:
                    max_margin = margin
                    max_index = i

        if max_index >= 0:  # On peut poser la course directement
            vehicules[max_index].add_ride(ride)
        else:  # Il va falloir decaller
            tries = 0
            while tries < inp.F:
                max_index = -1
                max_margin = None
                for j in range(inp.F):
                    margin = vehicules[i].margin_if_added(ride)
                    if margin < max_margin:
                        max_margin = margin
                        max_index = i

                if vehicules[max_index].can_push(ride):
                    vehicules[max_index].push_ride(ride)

                tries += 1
    output(vehicules, filename[:-3] + ".out")


compute_file("a_example.in")
compute_file("b_should_be_easy.in")
compute_file("c_no_hurry.in")
compute_file("d_metropolis.in")
compute_file("e_high_bonus.in")


