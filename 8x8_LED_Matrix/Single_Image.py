import board
from PIL import Image
from adafruit_ht16k33 import matrix

matrix = matrix.Matrix8x8(board.I2C())
 
image = Image.open("test2.png")
matrix.image(image)