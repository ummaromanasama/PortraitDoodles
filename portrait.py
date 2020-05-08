#Importing Libraries
from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  

#Load image and conver to black and white
original_image = Image.open("jg.jpg") 
bw_image = original_image.convert('1') 
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=10)]  

#(x, y) values
x = [x[1] for x in chosen_black_indices]
y = [x[0] for x in chosen_black_indices]

#Store coordinates points
result = zip(x,y)
result_List = list(result)
print(result_List)

#Black and white image popup 
plt.figure(figsize=(5, 5), dpi=100)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([])
plt.plot(x, y, '-0') 
plt.show()



