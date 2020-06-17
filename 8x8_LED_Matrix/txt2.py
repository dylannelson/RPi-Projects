import board
from adafruit_ht16k33.matrix import Matrix8x8
import time
import numpy as np
from PIL import Image
i2c = board.I2C()
matrix = Matrix8x8(i2c)
# info for this function identicalt to info availible in txt.py, up until the last loop
# *note* that here we use a different numpy array initialization.
# this is due to PIL handling numpy arrays poorly, and making it this specific datatype helps
# more info in the stackoverflow link a the end
x = np.asarray(dtype=np.dtype('uint8'),\
           a=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
              [1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0],\
              [0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0]])

slices = []
for i in range(x.shape[1]):
    indices = range(i,i+8)
    neighbourhood = x.take(indices, mode='wrap')
    x_slice = x.take(indices, mode='wrap',axis=1)
    slices.append(x_slice)

# here we actually just turn each  slice into an image    
for i in range(10):
    for cut in slices:
        # due to poor design of how Pillows creates iamges from arrays, we have to
        # create it as an 8 bit/pixel image, and then convert to 1 bit
        i = Image.fromarray(cut*255, mode='L').convert('1')
        # and then just display it
        matrix.image(i)

# here is further info on how/why PIL opperates so strangely with numpy arrays
# https://stackoverflow.com/questions/32159076/python-pil-bitmap-png-from-array-with-mode-1

        
