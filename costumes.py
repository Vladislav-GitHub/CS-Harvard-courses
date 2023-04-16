import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save('cotumes.gif', save_all=True, append_images=[images[1]], duration=200, loop=0)

# code costumes.py
# python costumes.py costume1.gif costume2.gif
# code costumes.gif
