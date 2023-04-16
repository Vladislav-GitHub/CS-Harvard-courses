import sys
from os.path import splitext
from PIL import Image, ImageOps


images = []

def main():
    check_command_line_args()
    # Open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    # Open shirt.png
    shirtfile = Image.open('shirt.png')
    # Get the size of the shirt.png
    size = shirtfile.size
    # Resize muppet image to fit shirt.png
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt.png in muppet
    muppet.paste(shirtfile, shirtfile)
    # Create output image
    muppet.save(sys.argv[2])


def check_command_line_args():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')
    if check_extension(file1[1]) == False or check_extension(file2[1]) == False:
        sys.exit('Invalid output')


def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()