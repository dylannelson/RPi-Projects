import board
from PIL import Image
from adafruit_ht16k33 import matrix
# regular setup/imports
matrix = matrix.Matrix8x8(board.I2C())

image = Image.open("heart_example.png")
matrix.image(image)

### Summary ###
# using a black/white png, you can simply load in the 
# 8x8 map you want. 
# this makes it easier to create images, sites like
# pixilart.com/draw can allow you to create these 8x8's with ease
# note that a black pixel corresponds to an ON led, while white is 
# an OFF led
# Any other will just be on/off, without any way to tell which beforehand
###