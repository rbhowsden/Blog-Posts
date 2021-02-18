uniform_dist = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
linear_dist = [0.0525, 0.0475, 0.0425, 0.0375, 0.0325, 0.0275, 0.0225, 0.0175, 0.0125, 0.0075]
plateau_dist = [.30, 0, 0, 0, 0, 0, 0, 0, 0, 0]

r_cadence = 52
r_size = 6
c_size = 1000
c_growth = 2
power_dist = [.20, .133, .0889, .059260, .03951, .02634, .017559, .011706, .007804, .005203, .003468, .002312, .001542, .001028, .000685, .000457, .000305, .000203, .000135, .000090]

import random

def rotate_simulation(dist, r_cadence, r_size, c_size, c_growth, spread, method):

    catalog = add_items([], 0, dist, c_size, spread)
    catalog = rank_items(catalog, method)
    index = c_size

    total_sold = 0
    for _ in range(r_cadence):
        for item in catalog[0:r_size]:
            if random.random() <= item[2]:
                catalog.remove(item)
                total_sold += 1
        catalog = add_items(catalog, index, dist, c_growth, spread)
        index += c_growth
        catalog = rank_items(catalog, method)
    
    return total_sold

def rank_items(catalog, method):
    if method == "random":
        random.shuffle(catalog)
    elif method == "popular":
        catalog.sort(key=lambda x: x[1], reverse=True)
    elif method == "personal":
        catalog.sort(key=lambda x: x[2], reverse=True)

    return catalog

def add_items(catalog, index, dist, number, spread):
    q, r = divmod(number, len(dist))
    new_items = q*dist + random.sample(dist, r)
    catalog.extend([(index + i, x, x + x*(2*random.random()-1)*spread)
                     for i, x in enumerate(new_items)])

    return catalog

