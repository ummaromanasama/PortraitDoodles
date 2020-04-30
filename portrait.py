from PIL import Image  

original_image = Image.open("jg.jpg") # open colour image
bw_image = original_image.convert('1') # convert image to black and white
#image_file.save('result.png')
# bw_image.show()
# original_image.show()
  
import numpy as np  
import matplotlib.pyplot as plt  
  
bw_image_array = np.array(bw_image, dtype=np.int)  
black_indices = np.argwhere(bw_image_array == 0)  
# Changing "size" to a larger value makes this algorithm take longer,  
# but provides more granularity to the portrait  
chosen_black_indices = black_indices[  
                           np.random.choice(black_indices.shape[0],  
                                            replace=False,  
                                            size=90000)]  
  
plt.figure(figsize=(6, 8), dpi=100)  
plt.scatter([x[1] for x in chosen_black_indices],  
            [x[0] for x in chosen_black_indices],  
            color='black', s=1)  
plt.gca().invert_yaxis()  
plt.xticks([])  
plt.yticks([]) 
plt.show()