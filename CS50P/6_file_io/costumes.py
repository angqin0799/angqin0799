import sys

from PIL import Image

images = []

# iterage through sys.argv and add to images list
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)


# save first image and to append following images
try:
    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )
except IndexError:
    print("add CL arguments")

