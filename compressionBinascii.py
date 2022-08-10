import time, binascii, struct, sys
from PIL import Image

def encrypt(rep, R, G, B):
    newNum = 0
    newNum = newNum | rep
    newNum = newNum << 8
    newNum = newNum | R
    newNum = newNum << 8
    newNum = newNum | G
    newNum = newNum << 8
    newNum = newNum | B
    return newNum

fileName = str(input("What image would you like to compress? "))
start_time = time.time()
img = Image.open(fileName)

if(img.mode != "RGB"):img = img.convert('RGB')

original = Image.open(fileName)
fullValueList = []
pix = img.load()
print(pix)
width, height = img.size
print(img.mode)
valueCount = 1
previousVal = None
#*******************************************************************
compressedFileName = "compressed_" + fileName + ".blap"
f = open(compressedFileName, "wb")
'''
f.write(bytes(width))
f.write(bytes(height))
'''
#*******************************************************************
if(img.mode == "RGB"):
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
            if(pix[x,y] == previousVal):
                valueCount += 1
            else:
                if(previousVal == None):
                    pass
                else:
                    num = binascii.a2b_uu(str(encrypt(valueCount, r, g, b)))
                    f.write(num)

                    valueCount = 1
            
            previousVal = pix[x,y]
    num = binascii.a2b_uu(str(encrypt(valueCount, r, g, b)))
    f.write(num)
            #fullValueList.append([r, g, b])
f.close()
#*******************************************************************
end_time = time.time()
print("That took " + str(end_time - start_time) + " seconds")
img.show()
original.show()
