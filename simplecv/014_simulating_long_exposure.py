from SimpleCV import *

image_directory = "../static/images/exposure/"
frames = ImageSet()
frames.load(image_directory)
img = Image(frames[0].size())
num_of_frames = len(frames)

for frame in frames:
    img = img + ( frame / num_of_frames)

img.show()
time.sleep(1000)
