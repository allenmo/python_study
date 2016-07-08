from SimpleCV import *

cam = Camera()
img = cam.getImage()
display = Display()
width = img.width
height = img.height
screensize = width * height
divisor = 5
threshold = 100

def stoplayer():
    newlayer = DrawingLayer(img.size())
    points = [(2 * width /divisor, height /divisor),
            (3 * width /divisor, height /divisor),
            (4 * width /divisor, 2 * height /divisor),
            (4 * width /divisor, 3 * height /divisor),
            (3 * width /divisor, 4 * height /divisor),
            (2 * width /divisor, 4 * height /divisor),
            (1 * width /divisor, 3 * height /divisor),
            (1 * width /divisor, 2 * height /divisor)]
    newlayer.polygon(points, filled=True, color=Color.RED)
    newlayer.setLayerAlpha(75)
    newlayer.text("STOP", (width / 2, height / 2), color = Color.WHITE)
    return newlayer

def golayer():
    newlayer = DrawingLayer(img.size())
    newlayer.circle((width / 2, height / 2), width / 4, filled = True, color = Color.GREEN)
    newlayer.setLayerAlpha(75)
    newlayer.text("GO", (width / 2, height / 2), color = Color.WHITE)
    return newlayer

while display.isNotDone():
    img = cam.getImage()
    min_blob_size = 0.30 * screensize
    max_blob_size = 0.60 * screensize
    blobs = img.findBlobs(minsize = min_blob_size, maxsize = max_blob_size)

    layer = golayer()

    if blobs:
        avgcolor = np.mean(blobs[-1].meanColor())
        if avgcolor >= threshold:
            layer = stoplayer()
        blobs.draw()

    img.addDrawingLayer(layer)
    img.show()

