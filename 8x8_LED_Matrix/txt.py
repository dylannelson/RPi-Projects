import board
from adafruit_ht16k33.matrix import Matrix8x8
import time
import numpy as np
from PIL import Image

# basic setup for connecting to LED matrix through GPIO
i2c = board.I2C()
matrix = Matrix8x8(i2c)
# Array that looks like the text for UCSD
# 1's are a lit LED
# 0's are an unlit LED
x = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
              [1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0],\
              [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0],\
              [0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0]])
slices = []

# this loop makes a set of each different 8x8 slice from the above
# array, in order from left to right this is done so each 8x8 can 
# be displayed, and give it the text sliding effect
for i in range(x.shape[1]):
    indices = range(i,i+8)
    # this is a useful numpy funcctions that allow you to take
    # slices of a certain length, and if you reach the end of 
    # the array, it will wrap around to the beginning
    neighbourhood = x.take(indices, mode='wrap')
    x_slice = x.take(indices, mode='wrap',axis=1)
    slices.append(x_slice)

# this, while looking very innefficient, is about as fast as the 
# adafruit 'matrix.image' function, which I show in txt2.py

# it basically powers each pixel on/off 1 by 1 from he slices we made
while True:
    for i in slices:
        for h in range(8):
            for w in range(8):
                matrix[h,w] = i[w,h]
        time.sleep(.01)
    
print('done')