import random
import sys
from pyfiglet import Figlet, FontNotFound

figlet = Figlet()

if (sys.argv[1] == "--font" or sys.argv[1] == "-f") and len(sys.argv) > 2:
    try:
        figlet.setFont(font=sys.argv[2])
    except FontNotFound:
        sys.exit("Invalid usage")
    s = input("Input: ")
    print(figlet.renderText(s))

elif len(sys.argv) == 1:
    s = input("Input: ")
    random_font = random.choice(figlet.getFonts())
    figlet = Figlet(font=random_font)
    print(figlet.renderText(s))
    
else:
    sys.exit("Invalid usage")



