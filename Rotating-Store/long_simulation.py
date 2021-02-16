

uniform_dist = [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]
linear_dist = [0.0525, 0.0475, 0.0425, 0.0375, 0.0325, 0.0275, 0.0225, 0.0175, 0.0125, 0.0075]
plateau_dist = [.30, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#EVERY PLAYER WILL HAVE DIFFERENT DISTRIBUTION

r_cadence = 52
r_size = 6
c_size = 1000
c_growth = 2
power_dist = [.20, .133, .0889, .059260, .03951, .02634, .017559, .011706, .007804, .005203, .003468, .002312, .001542, .001028, .000685, .000457, .000305, .000203, .000135, .000090]

import random

def random_selection(dist, r_num, r_size, c_size, c_growth):

    dist_length = len(dist)
    if c_size % dist_length != 0:
        print('bad, choose better parameters')

    full_catalog = dist*int(c_size/dist_length)
    items = [(i, x, x*random.random()*2) for i, x in enumerate(full_catalog)]
    current_i = len(items)
    random.shuffle(items)
    
    total_sold = 0
    for _ in range(r_num):
        for item in items[0:r_size]:
            if random.random() <= item[2]:
                items.remove(item)
                total_sold += 1
        new_items = random.sample(dist, c_growth)
        new_items = [(current_i + i, x, x*random.random()*2) for i, x in enumerate(new_items)]
        items += new_items
        random.shuffle(items)
        current_i += c_growth
    
    return total_sold


def rotate_simulation(dist, r_num, r_size, c_size, c_growth, method):

    dist_length = len(dist)
    if c_size % dist_length != 0:
        print('bad, choose better parameters')

    full_catalog = dist*int(c_size/dist_length)
    items = [(i, x, x*random.random()*2) for i, x in enumerate(full_catalog)]
    current_i = len(items)
    rank_items(items, method)

    total_sold = 0
    for _ in range(r_num):
        for item in items[0:r_size]:
            if random.random() <= item[2]:
                items.remove(item)
                total_sold += 1
        new_items = random.sample(dist, c_growth)
        new_items = [(current_i + i, x, x*random.random()*2) for i, x in enumerate(new_items)]
        items += new_items
        rank_items(items, method)
        current_i += c_growth
    
    return total_sold

def rank_items(items, method):
    if method == "random":
        random.shuffle(items)
    elif method == "popular":
        items.sort(key=lambda x: x[1], reverse=True)
    elif method == "personal":
        items.sort(key=lambda x: x[2], reverse=True)

    return items

def personal_selection(dist, r_num, r_size, c_size, c_growth):

    total_sold = 0
    dist_length = len(dist)
    if c_size % dist_length != 0:
        print('bad, choose better parameters')

    full_catalog = dist*int(c_size/dist_length)
    items = [(i, x*random.random()*2) for i, x in enumerate(full_catalog)]
    current_i = len(items)
    items.sort(key=lambda x: x[1], reverse=True)

    total_sold = 0
    for _ in range(r_num):
        for item in items[0:r_size]:
            if random.random() <= item[1]:
                items.remove(item)
                total_sold += 1
        new_items = random.sample(dist, c_growth)
        new_items = [(current_i + i, x*random.random()*2) for i, x in enumerate(new_items)]
        items += new_items
        items.sort(key=lambda x: x[1], reverse=True)
        current_i += c_growth
    
    return total_sold
