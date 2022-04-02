from PIL import Image
import numpy
import time
start_time = time.time()
img = Image.open(str(input("What image would you like to compress? ")))
imgArray = numpy.asarray(img)
width, height = img.size
print("Width of the image is:", width)
print("Height of the image is:", height)
print("Number of Pixels in the img: " + str(len(imgArray) * len(imgArray[0])))

'''
newImg = numpy.empty((height, width, 3))
for row in imgArray:
    for rgb in row:
        for value in rgb: 
            if(value >= 250):
                numpy.append(newImg, 250)
                pass
            rounded = round(value, -1)
            numpy.append(newImg, rounded, axis=2)
'''
'''
for row in imgArray:
    for col in row:
        i = 0
        for pixel in col:
            if(pixel >= 250):
                numpy.delete(imgArray[row][col], i)
                numpy.insert(col, i, 250)
                i += 1
                continue
            rounded = round(pixel, -1)
            #print(str(pixel), ", " + str(rounded))
            numpy.delete(col, i)
            numpy.insert(col, i, rounded)
            i += 1
'''
newImg = numpy.empty((height, width, 3))
for col in imgArray:
    newCol = numpy.empty(width)
    for pixel in col:
        newPixel = numpy.empty(3)
        for value in pixel:
            if(value >= 250):
                numpy.append(newPixel, 250)
                continue
            else:
                rounded = round(value, -1)
                numpy.append(newPixel, rounded)
        numpy.append(newCol, newPixel)
    numpy.append(newImg, newCol)

compressedImg = Image.fromarray(newImg, mode="RGB")
end_time = time.time()
print("It took ", (end_time - start_time), " seconds")
img.show()
#time.sleep(2)
compressedImg.show()
print()