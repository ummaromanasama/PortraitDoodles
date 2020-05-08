#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations 


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

    
#Accesing 2D array and calculating distance fomula and storing the info
# distance = []
# for i in range(len(result_List)):
#     for j in range(len(result_List[i])):
#         distance_formula = math.sqrt(((x[j]-x[i])**2)+((y[j]-y[i])**2))
#     distance.append(distance_formula)  
# print(distance) 


#pop up
# plt.plot(x, y, '-0')
# plt.show()

