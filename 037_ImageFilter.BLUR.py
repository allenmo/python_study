import Image, ImageFilter

im = Image.open('61.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('61_ImageFilterBLUR.jpg')

