import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('piedra.png')
imgplot = plt.imshow(img)
plt.show()