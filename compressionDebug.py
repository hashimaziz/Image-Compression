from PIL import Image
import numpy
fullRGBList = []
img = Image.open(str(input("What image would you like to compress? ")))
width, height = img.size
print("Width of the image is:", width)
print("Height of the image is:", height)
#*********************************************************************************
imgArray = numpy.asarray(img)
print(imgArray[0][0][0])
print(imgArray)

print("Number of Pixels in the img: " + str(len(imgArray) * len(imgArray[0])))
#*********************************************************************************
for row in imgArray:
    for col in row:
        for pixel in col:
            if(pixel >= 250):
                fullRGBList.append(250)
                continue
            rounded = round(pixel, -1)
            fullRGBList.append(rounded)
#*********************************************************************************
#print(fullRGBList)
print("Phase 1 complete")
print("Number of Pixels in RGBList: " + str(len(fullRGBList)/3))
#*********************************************************************************
#print(fullRGBList)
newImgArray = numpy.array(fullRGBList).reshape(height, width, 3)
print(newImgArray)
compressedImg = Image.fromarray(newImgArray, mode="RGB")
#*********************************************************************************
img.show()
compressedImg.show()
print()
#compressedImg.save("my.png")
