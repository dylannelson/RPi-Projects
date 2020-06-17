import board
from adafruit_ht16k33.matrix import Matrix8x8
import time

i2c = board.I2C()
matrix = Matrix8x8(i2c)

import numpy as np
from PIL import Image
x = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
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
while True:
    for i in slices:
        for h in range(8):
            for w in range(8):
                matrix[h,w] = i[w,h]
        time.sleep(.01)
    
print('done')