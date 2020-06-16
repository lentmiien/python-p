from pathlib import Path
# .\Scripts\pip install --user pillow
from PIL import Image, ImageDraw, ImageFont

# Load/Init
f = open(Path(Path.home(), 'Documents', 'tti', 'data.txt'), "r")
template = Image.open(Path(Path.home(), 'Documents', 'tti', 'template.jpg'))
width, height = template.size
template = template.resize((width * 2, height * 2))

datefont = ImageFont.FreeTypeFont(
    font=str(Path(Path.home(), 'Documents', 'tti', 'arial.ttf')), size=20)
trackfont = ImageFont.FreeTypeFont(
    font=str(Path(Path.home(), 'Documents', 'tti', 'arial.ttf')), size=18)
addressfont = ImageFont.FreeTypeFont(
    font=str(Path(Path.home(), 'Documents', 'tti', 'arial.ttf')), size=18)

japfont = ImageFont.FreeTypeFont(
    font=str(Path(Path.home(), 'Documents', 'tti', 'msgothic.ttc')), size=40)

filereader = f.readline()[:-1]
while len(filereader) == 10:
    template_copy = template.copy()
    draw = ImageDraw.Draw(template_copy)
    draw.rectangle((311, 204, 398, 239), outline='black', width=5)
    draw.text((155, 580), '米国返送・・・', fill='black', font=japfont)
    draw.text((307, 643), '123-4567', fill='black', font=addressfont)
    draw.text((169, 670), 'Oh-ami Inc.\nStreet address',
              fill='black', font=addressfont)
    draw.text((230, 723), '080-6931-3319',
              fill='black', font=addressfont)

    # Add text
    tracking = f.readline()[:-1]
    date = f.readline()[:-1]
    year = date[0:4]
    month = str(int(date[5:7]))
    day = str(int(date[8:]))
    address = f.readline() + f.readline() + f.readline() + f.readline()[:-1]
    # Shipping method
    if tracking[0:2] == 'EM':
        draw.text((220, 385), 'EMS', fill='black', font=japfont)
    else:
        draw.text((155, 385), '航空便(Air)', fill='black', font=japfont)
    # Date 150x310 240x310 310x310
    draw.text((150, 310), year, fill='black', font=datefont)
    draw.text((240, 310), month, fill='black', font=datefont)
    draw.text((310, 310), day, fill='black', font=datefont)
    # Tracking 490x393
    draw.text((480, 390), tracking, fill='black', font=trackfont)
    # Address 169x473
    draw.text((169, 473), address, fill='black', font=addressfont)

    # Save output
    template_copy.save(Path(Path.home(), 'Documents',
                            'tti', 'output', tracking + '_return.jpg'))

    filereader = f.readline()[:-1]
