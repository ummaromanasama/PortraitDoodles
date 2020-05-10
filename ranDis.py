#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations 
from itertools import combinations
from math import hypot

#Individual values
num_dot = 3
x = np.random.randint(10, size = num_dot)
y = np.random.randint(10, size = num_dot)

#Store coordinates points
result = zip(x,y)
result_List = list(result)

#Permutation of each cooridnate in relation to the 
#rest of the the cooridnate
perm = permutations(result_List, num_dot)
for i in perm: 
    route = list(i)
    route.append(result_List[0])
    print(route)
    for (x1, y1), (x2, y2) in zip(route, route[1:]):
        distance_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(distance_formula)

#pop up
# plt.plot(x, y, '-0')
# plt.show()

