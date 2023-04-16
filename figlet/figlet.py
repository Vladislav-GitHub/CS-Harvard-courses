import sys
from random import choices
from pyfiglet import Figlet

figlet = Figlet()

# list of available fonts
fonts = figlet.getFonts()

try:
    if len(sys.argv) == 1:
        f = choices(fonts)
    elif len(sys.argv) == 3:
        f = sys.argv[2]
    else:
        sys.exit('Invalid usage')
except OSError:
    print('Error')

if (sys.argv[1] != '-f' and sys.argv[1] != '--font') or sys.argv[2] not in fonts:
    sys.exit('Invalid usage')

# prompt user for the text
s = input('Input: ')

# set the font, wherein f is the font’s name as a str
figlet.setFont(font=f)

# output text in that font, wherein s is that text as a str
print(f'Output:\n{figlet.renderText(s)}')