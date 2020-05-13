#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import permutations 

#Generate dots with X and Y values
num_dot = 10
x = np.random.randint(10, size = num_dot)
y = np.random.randint(10, size = num_dot)

#Pair and store coordinates points
result = zip(x,y)
result_List = list(result)

#Total distance between points are stored here
total_dis = []

#Permuation combos routes are stored here
all_route = []

#Permutation of cooridnates are calulated
# to gernate different routes
perm = permutations(result_List, num_dot)
for i in perm: 
    route = list(i)
    route.append(route[0])
    dis_list = [] 
    #I need to put all the routes in a list to acess the routes by index  
    all_route.append(route)
    #Distances between points are calulates
    # and stored                       
    for (x1, y1), (x2, y2) in zip(route, route[1:]):
        distance_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        dis_list.append(distance_formula)     
    total_dis.append(dis_list)               

#Finding the total distances of each route and stored in list
route_distance = []
for d in total_dis:
    dis = sum(d)
    route_distance.append(dis)

#Find the shortest distance in the list
m = min(route_distance)

#Find the index of the shortest distance
s = route_distance.index(m)

#Find the route of the shortest distance
shortest_route = all_route[s]

#Plotting points and conencting them in order of the list 
x = [point[0] for point in shortest_route]
y = [point[1] for point in shortest_route]

plt.plot(x, y)
plt.show()
