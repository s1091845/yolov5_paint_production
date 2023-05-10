import numpy as np
import cv2
# 讀取圖檔
#img = cv2.imread('image_02.jpg', cv2.IMREAD_COLOR+cv2.IMREAD_IGNORE_ORIENTATION)

# 寫入圖檔
#cv2.imwrite('image_09.jpg', img)

# 讀取圖檔
#img3 = cv2.imread('image_09.jpg')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import matplotlib.pyplot as plt
import image_to_numpy
# Load your image file
img = image_to_numpy.load_image_file("image_02.jpg")
# Show it on the screen (or whatever you want to do)
plt.imshow(img)
plt.show()

# 寫入圖檔
cv2.imwrite('image_10.jpg', img)
