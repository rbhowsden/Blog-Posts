import random

def expected_distance(num_houses=100, sims=100):
    total_dist = 0
    sims_count = 0
    for x in range(sims):
        you = random.randint(1, num_houses)
        friend = random.randint(1, num_houses)

        # account for constraint violations
        if you != friend: 
            total_dist += abs(you-friend)
            sims_count += 1

    return(total_dist/sims_count)