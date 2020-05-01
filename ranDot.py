import numpy as np
import matplotlib.pyplot as plt

#Practice for generating random dots and connecting them

x = np.random.random_sample(size=100)
y = np.random.random_sample(size=100)

fig, ax = plt.subplots()
ax.scatter(x,y)
plt.plot(x, y, '-o')
plt.show()
