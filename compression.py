from PIL import Image
import numpy
fullRGBList = []
compressedImgArray = []
img = Image.open(str(input("What image would you like to compress? ")))
width, height = img.size
pixelValues = []

print("Width of the image is:", width)
print("Height of the image is:", height)
imgArray = numpy.asarray(img)
'''
print(imgArray[1][1])
print(len(imgArray))
print(len(imgArray[0]))
print(len(imgArray[0][0]))
print(str(imgArray[0][0][0]))
'''
print("Number of Pixels in the img: " + str(len(imgArray) * len(imgArray[0])))

for row in imgArray:
    for col in row:
        for pixel in col:
            rounded = round(pixel, -1)
            if(rounded > 254):
                rounded = 250
            elif(rounded < 0):
                rounded = 0
            fullRGBList.append(rounded)
#print(fullRGBList)
print("Phase 1 complete")
print("Number of Pixels in RGBList: " + str(len(fullRGBList)/3))
imgArray = []

i = 0
for element in fullRGBList:
    if(i+2 > len(fullRGBList) - 1):
        break
    pixelValues.append([fullRGBList[i], fullRGBList[i+1], fullRGBList[i+2]])
    i += 3

print("Phase 2 complete")
print("Number of pixels in PixelList: " + str(len(pixelValues)))
fullRGBList = []

for h in range(height):
    intermediateArray = []
    for w in range(width):
        intermediateArray.append(pixelValues[0])
        pixelValues.pop(0)
    compressedImgArray.append(intermediateArray)

print("Phase 3 complete")
print("Number of pixels in compressed Image: " + str(len(compressedImgArray) * len(compressedImgArray[0])))
pixelValues = []
#print(compressedImgArray)
compressedImgArray = numpy.array(compressedImgArray)

'''
print(imgArray)
print(compressedImgArray)
'''

compressedImg = Image.fromarray(compressedImgArray, mode="RGB")

img.show()
compressedImg.show()
#compressedImg.save("my.png")

#print(compressedImgArray)
