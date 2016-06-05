import Image

im = Image.open('mv.jpg')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('mv_thumbnail.jpg')

