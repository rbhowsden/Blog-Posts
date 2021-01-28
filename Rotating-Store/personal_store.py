import numpy as np

num_items = 20
p = 0.33333
pmf = [0]*num_items
weights = [0]*num_items
purch_rate = .03
for item in range(20):
    pmf[item] = (1-(1-p)**(item+1))
    if item == 0:
        weights[item] = pmf[item]
    else:
        weights[item] = pmf[item] - pmf[item-1]

weights = np.array(weights)
weights /= weights.sum()
np.random.choice(20, 20, replace=False, p=weights)
