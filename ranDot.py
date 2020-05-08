#Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math


x = np.random.randint(10, size=5)
y = np.random.randint(10, size=5)

#Store coordinates points
result = zip(x,y)
result_List = list(result)
print(result_List)

#pop up
plt.plot(x, y, '-0')
plt.show()

