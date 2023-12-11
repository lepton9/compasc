from PIL import Image
import sys
import numpy as np

def read(fileName):
    im = Image.open(fileName)
    pixelMap = im.load()
    pixels = []
    image = np.asarray(im)

    print(image.shape)
    _y, _x = image.shape
    str_array = [str(image[y][x]) for y in range(_y) for x in range(_x)]
    return str_array


if __name__ == "__main__":
    pixels = read(sys.argv[1])
    print(pixels)
