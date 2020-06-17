import board
from adafruit_ht16k33.matrix import Matrix8x8
import time

i2c = board.I2C()
matrix = Matrix8x8(i2c)

import numpy as np
from PIL import Image
x = np.asarray(dtype=np.dtype('uint8'), a=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
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
for i in range(10):
    for cut in slices:
        i = Image.fromarray(cut*255, mode='L').convert('1')
        matrix.image(i)
# https://stackoverflow.com/questions/32159076/python-pil-bitmap-png-from-array-with-mode-1

        
