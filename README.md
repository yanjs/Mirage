# Mirage

To make an PNG image which looks like img1 when in white background, img2 when in black background.

## Usage:

### In Windows Explorer:

Select two images and drag them onto 'Emerge.bat'.

### Command line:

Usage:

	python emerge.py [img1 [img2 [outimg]]]

Arguments:

	img1[default='f.png'], img2[default='b.png']: filename (must exist)
	outimg: filename (may override existing file)


Output:

	An PNG image which looks like img1 when shown in white(#FFFFFF) background, img2 in black(#000000) background.

## Dependence:

Python3

PIL(Pillow)