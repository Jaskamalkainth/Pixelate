''' j1k7_7 '''

from PIL import Image, ImageDraw, ImageFont
import random

INP_FILE_NAME = "InpImages/jk.jpg"
OUT_FILE_NAME = "OutImages/jkPixelate.jpg"
BLOCK_SIZE = 40
OVERLAY_IMAGES_MAX = 20

def genRand255():
    return int(random.randrange(0, 255))

def genRandPixel():
    return (genRand255(), genRand255(), genRand255())

def genImage(n):
    tempImage = Image.new('RGBA', (BLOCK_SIZE, BLOCK_SIZE), color=(0, 0, 0, 0))
    d = ImageDraw.Draw(tempImage)
    OVERLAY_IMAGE_FONT = 27
    font = ImageFont.truetype("Simply Glamorous.ttf", size=OVERLAY_IMAGE_FONT)
    TOP_LEFT_CORNER = (7, 7)
    d.text(TOP_LEFT_CORNER, n, fill=genRandPixel(), font=font)
    #tempImage.save(n + ".png")
    pixtempImage = tempImage.load()
    return pixtempImage

def genOverlayImages():
    oiList = []
    for i in range(OVERLAY_IMAGES_MAX):
        charset = ['#', '7', '1', '4', '&', '$',
                   '!', '~', '*', '2', '3', '6', '9', '*']
        chRand = charset[random.randrange(0, len(charset))]
        oiList.append(genImage(chRand))
    return oiList

def Pixelate():
    for r in range(0, imHeight, BLOCK_SIZE):
        for c in range(0, imWidth, BLOCK_SIZE):
            # Computing the average to Pixelate the Image
            avR, avG, avB = 0, 0, 0
            for i in range(BLOCK_SIZE):
                for j in range(BLOCK_SIZE):
                    if (r+i) >= imHeight or (c+j) >= imWidth:
                        continue
                    avR += pixII[r+i, c+j][0]
                    avG += pixII[r+i, c+j][1]
                    avB += pixII[r+i, c+j][2]
            avR /= BLOCK_SIZE*BLOCK_SIZE
            avG /= BLOCK_SIZE*BLOCK_SIZE
            avB /= BLOCK_SIZE*BLOCK_SIZE
            for i in range(BLOCK_SIZE):
                for j in range(BLOCK_SIZE):
                    if (r+i) >= imHeight or (c+j) >= imWidth:
                        continue
                    pixOI[r+i, c+j] = (int(avR), int(avG), int(avB))

def AddOverlayImages():
    for r in range(0, imHeight, BLOCK_SIZE):
        for c in range(0, imWidth, BLOCK_SIZE):
            overlayId = int(random.randrange(0, OVERLAY_IMAGES_MAX))
            # Overlaying the random image on top of the Pixelated Image
            for i in range(BLOCK_SIZE):
                for j in range(BLOCK_SIZE):
                    if (r+i) >= imHeight or (c+j) >= imWidth:
                        continue
                    if overlayList[overlayId][i, j] != (0, 0, 0, 0):
                        pixOI[r+i, c+j] = overlayList[overlayId][i, j]


''' Main Driver Program BEGINS '''

# Opening Input FILE
inpImage = Image.open(INP_FILE_NAME)
pixII = inpImage.load ()

imHeight, imWidth = inpImage.size

# Output FILE
outImage = Image.new('RGB', (imHeight, imWidth))
pixOI = outImage.load()

# Generate Overlay Images to add to the default Input Image
overlayList = genOverlayImages()

Pixelate()
AddOverlayImages()

# Saving the Final Output Image
outImage.save(OUT_FILE_NAME)
