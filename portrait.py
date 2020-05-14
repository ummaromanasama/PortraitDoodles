#Importing Libraries
from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  
import math
from itertools import permutations 

#Number of dots
dot_number = 12

#Load image and convert to black and white
original_image = Image.open("jg.jpg") 
bw_image = original_image.convert('1') 
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=dot_number)]  

#Generate dots with X and Y values
x = [x[1] for x in chosen_black_indices]
y = [x[0] for x in chosen_black_indices]

#Pair and store coordinates points
coordinates_values = zip(x,y)
image_coordinates = list(coordinates_values)
print(image_coordinates)

#Total distance between points are stored here
distance_points = []

#Permuation combos routes are stored here
all_routes = []

#Permutation of cooridnates are calulated
# to gernate different routes
perm = permutations(image_coordinates, dot_number)
for i in perm: 
    route = list(i)
    route.append(route[0])
    dis_list = [] 
    #I need to put all the routes in a list to acess the routes by index  
    all_routes.append(route)
    #Distances between points are calulates
    # and stored                       
    for (x1, y1), (x2, y2) in zip(route, route[1:]):
        distance_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        dis_list.append(distance_formula)     
    distance_points.append(dis_list)    

#Finding the total distances of each route and stored in list
route_distance = []
for d in distance_points:
    dis = sum(d)
    route_distance.append(dis)

#Find the shortest distance in the list
m = min(route_distance)

#Find the index of the shortest distance
s = route_distance.index(m)

#Find the route of the shortest distance
shortest_route = all_routes[s]

#Plotting points and conncting them in order of the list 
x = [point[0] for point in shortest_route]
y = [point[1] for point in shortest_route]

plt.plot(x, y)
plt.show()

# #Customize popup
# plt.figure(figsize=(5, 5), dpi=100)  
# plt.gca().invert_yaxis()  
# plt.xticks([])  
# plt.yticks([])

# #Plotting points and conencting them in order of the list 
# plt.plot(x, y, '-0') 
# plt.show()



