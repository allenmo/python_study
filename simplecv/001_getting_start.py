from SimpleCV import Camera

# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
    # make mage black and white
    img = img.binarize()
    # Draw the text "Hello World" on image
    img.drawText("Hello World")
    # Show the image
    img.show()


