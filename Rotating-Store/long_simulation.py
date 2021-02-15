

uniform_dist = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
linear_dist = [0.0525, 0.0475, 0.0425, 0.0375, 0.0325, 0.0275, 0.0225, 0.0175, 0.0125, 0.0075]
power_dist = [.20, .133, .0889, .059260, .03951, .02634, .017559, .011706, .007804, .005203, .003468, .002312, .001542, .001028, .000685, .000457, .000305, .000203, .000135, .000090]
plateau_dist = [.30, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#EVERY PLAYER WILL HAVE DIFFERENT DISTRIBUTION

r_cadence = 52
r_size = 6
c_size = 1000
c_growth = 2
method="weighted"

import random

def random_selection(dist, r_num, r_size, c_size, c_growth, method):

    total_sold = 0
    dist_length = len(dist)
    if c_size % dist_length != 0:
        print('bad, choose better parameters')

    full_catalog = dist*int(c_size/dist_length)
    items = [(i, x) for i, x in enumerate(full_catalog)]
    
    for _ in range(r_num):
        for item in random.sample(items, r_size):
            if random.random() <= item[1]:
                items.remove(item)
                total_sold += 1
    
    return total_sold


def recomm_selection(dist, r_num, r_size, c_size, c_growth, method):

    total_sold = 0
    dist_length = len(dist)
    if c_size % dist_length != 0:
        print('bad, choose better parameters')

    full_catalog = dist*int(c_size/dist_length)
    items = [(i, x) for i, x in enumerate(full_catalog)]
    sort_items = sorted(items, key = lambda x: x[1], reverse = True)

    for _ in range(r_num):
        for item in sort_items[0:r_size]:
            if random.random() <= item[1]:
                sort_items.remove(item)
                total_sold += 1
    
    return total_sold

