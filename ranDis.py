#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations 
from itertools import combinations
from math import hypot

#Individual values
num_dot = 5
x = np.random.randint(10, size = num_dot)
y = np.random.randint(10, size = num_dot)

#Store coordinates points
result = zip(x,y)
result_List = list(result)

#Total distance values are stored here
total_dis = []

#Permutation of cooridnates 
perm = permutations(result_List, num_dot)
for i in perm: 
    route = list(i)
    route.append(route[0])
    dis_list = []                             # <----  Add this line 
    for (x1, y1), (x2, y2) in zip(route, route[1:]):
        distance_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        dis_list.append(distance_formula)     # <----  Add this line 
    total_dis.append(dis_list)                # <----  Add this line (outside the "distance" loop)
print('Distance between each points', total_dis)

#Add the distances of each combo and store in list
add = []
for a in total_dis:
    dis = sum(a)
    add.append(dis)
print('sum of each index of each combo', add)

#Find the shortest distance
u = min(add)
print('shortes route',u)

#Find the index of the shortest distance
s = add.index(u)
print('index:',s)

#pop up
# plt.plot(x, y, '-0')
# plt.show()

