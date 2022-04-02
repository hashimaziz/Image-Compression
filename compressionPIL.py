import PIL, time
from PIL import Image
start_time = time.time()
fileName = str(input("What image would you like to compress? "))
img = Image.open(fileName)
original = Image.open(fileName)
fullValueList = []
pix = img.load()
print(pix)
width, height = img.size
print(img.mode)
#*******************************************************************
compressedFileName = "compressed_" + fileName + ".blap"
f = open(compressedFileName, "w")
f.write(str(width) + " " + str(height) + "\n")
#*******************************************************************
if(img.mode == "RGB"):
    f.write("1\n")
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            r = round(r, -1)
            g = round(g, -1)
            b = round(b, -1)
            if(r >= 250):
                r = 250
            if(g >= 250):
                g = 250
            if(b >= 250):
                b = 250
        
            pix[x, y] = (r, g, b)
            fullValueList.append(str(r) + " " + str(g) + " " + str(b))

valueCount = 1
previousVal = None
for value in fullValueList:
    if(value == previousVal):
        valueCount += 1
        pass
    else:
        f.write(str(valueCount) + ":" + str(value) + "\n")
        valueCount = 1
        pass
    previousVal = value

#*******************************************************************
if(img.mode == "RGBA"):
    f.write("2")
    for x in range(width):
        for y in range(height):
            r, g, b, a = pix[x, y]
            r = round(r, -1)
            g = round(g, -1)
            b = round(b, -1)
            if(r >= 250):
                r = 250
            if(g >= 250):
                g = 250
            if(b >= 250):
                b = 250

            pix[x, y] = (r, g, b, a)
 #*******************************************************************       
if(img.mode == "HSV"):
    f.write("3")
    for x in range(width):
        for y in range(height):
            h, s, v = pix[x, y]
            h = round(r, -1)
            s = round(g, -1)
            v = round(b, -1)
            if(h >= 250):
                h = 250
            if(s >= 250):
                s = 250
            if(v >= 250):
                v = 250

            pix[x, y] = (h, s, v)
#*******************************************************************
end_time = time.time()
print("That took " + str(end_time - start_time) + " seconds")
img.show()
original.show()
