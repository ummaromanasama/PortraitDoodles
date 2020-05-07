#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math

#dont ask
#How should the coordnates be formatted for the the distance forumla
#option one it x and y values in an array togehter or
#the x and y value seperated?

#ask
#if my calulation for the distance is correct and i properly stored the info.
#how do I "manually connect tthe dots based off the information"
#the new connecting the dots would go from shortest to longest route and no intersection...
#I dont know if i need to prevent intersections becuase of the algorith or i do?
#do i need to merge the coordinates and distance data then pict out the points based off the data and then eventually replot the points? manually?
#whould it not be classified as a scatter plot if re plotted on purpuse in an scififc order?? trickey.


#Individual values
x = np.random.randint(10, size=3)
y = np.random.randint(10, size=3)

#Store coordinates points
result = zip()
result_list = list(result)
result = zip(x, y)
result_set = list(result)
print(result_set)

#Accesing 2D array and calculating distance fomula and storing the info
distance = []
for i in range(len(result_set)):
    for j in range(len(result_set[i])):
        distance_formula = math.sqrt(((x[i]-y[i])**2)+((x[j]-y[j])**2))
    print(distance_formula)
    distance.append(distance_formula)  
print(distance) 

#pop up
plt.plot(x, y, '-0')
plt.show()