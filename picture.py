import array

width = 256;
height = 256;
maxval = 255;
header = "P3 " + str(width) + " "+ str(height) + " " + str(maxval) + "\n"

pixels = array.array('i', [0, 255, 255] * width * height)
fd = open("image.ppm", 'w')
for column in range(0, width):
    for row in range(0, height):
        index = (height * row + column) * 3
        pixels[index + 1] = 0
        pixels[index + 2] = column
fd.write(header)
for pixel in pixels:
    fd.write(str(pixel) + " ")

# .tofile(fd)
