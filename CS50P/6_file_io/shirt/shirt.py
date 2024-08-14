import sys, os.path
from PIL import Image, ImageOps

def main():
    input_img, output_img = validate_args(sys.argv[1], sys.argv[2])
    img2 = overlay_shirt(input_img)
    img2.save(output_img)

def validate_args(arg1, arg2):
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py before_image after_image")

    arg1 = os.path.splitext(arg1)
    arg2 = os.path.splitext(arg2)
    valid_ext = [".jpg", ".png", ".jpeg"]

    if arg1[1].casefold() not in valid_ext:
        sys.exit("Invalid extensions")
    if arg1[1] != arg2[1]:
        sys.exit("Input and output have different extensions")

    return sys.argv[1], sys.argv[2]

def overlay_shirt(input_img):
    try:
        img1 = Image.open(input_img) # img1.size is (1200, 1600)
    except FileNotFoundError:
        sys.exit("Input file not found")
    shirt_img = Image.open("shirt.png")
    img1 = ImageOps.fit(img1, shirt_img.size) # resize/fit input image to the size of the shirt (600,600)
    img1.paste(shirt_img, shirt_img) # paste shirt onto img1

    return img1

if __name__ == "__main__":
    main()
