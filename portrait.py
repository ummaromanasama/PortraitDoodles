#Importing Libraries
from PIL import Image  
import numpy as np  
import matplotlib.pyplot as plt  

#Load image and conver to black and white
original_image = Image.open("jg.jpg") 
bw_image = original_image.convert('1') 
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
chosen_black_indices = black_indices[np.random.choice(black_indices.shape[0], replace=False, size=1000)]  

#Black and white image popup 
plt.figure(figsize=(5, 5), dpi=100)  
plt.scatter([x[1] for x in chosen_black_indices], [x[0] for x in chosen_black_indices], color='black', s=1)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([])
plt.plot([x[1] for x in chosen_black_indices], [x[0] for x in chosen_black_indices], marker='o', color='black') 
plt.show()



