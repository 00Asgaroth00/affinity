#!/usr/bin/env python

"""
Script used to convert a bunch of SVG files to PNG
"""

from os import walk, mkdir
import pyvips

# sudo apt-get install libvips
# pip install pyvips

PATH = "svg/"


def main():

    """
    All the action
    """

    for (root, dirs, files) in walk(PATH):
        for f in files:
            if ".svg" in f:
                try:
                    mkdir(path=f"{root}/png/")
                except OSError:
                    pass
                convert_file = pyvips.Image.thumbnail(f"{root}/{f}", 52, height=52)
                convert_file.write_to_file(f"{root}/png/{f.replace('svg', 'png')}")
                # alternative method using cairosvg, taken from comment:
                #    https://github.com/ecceman/affinity/issues/12#issuecomment-819598447
                # cairosvg.svg2png(url=f"{root}/{f}", write_to=f"{root}/png/{f.replace('svg', 'png')}")


if __name__ == "__main__":
    main()
