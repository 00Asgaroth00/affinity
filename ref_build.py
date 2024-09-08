#!/usr/bin/env python

"""
Script used to create reference.md
"""

from os import walk

PATH = "svg/"


def main():

    """
    All the action
    """

    with open("reference.md", "w") as my_file:
        # Headers and settings alignments for file
        my_file.write("# Reference for Icons\n")
        my_file.write("\n")
        my_file.write("|Icon|Name|Icon|Name|Icon|Name|\n")
        my_file.write("|:---:|:---:|:---:|:---:|:---:|:---:|\n")
        for (root, dirs, files) in walk(PATH):
            count = 0
            # Iterating over all files with .png extension
            for f in files:
                if ".png" in f:
                    # Simple math checks on matches and reset
                    # counter on third entry
                    count += 1
                    if count == 1:
                        my_file.write(f"|![{f}]({root}/{f})|{f.replace('.png', '')}|")
                    if count == 2:
                        my_file.write(f"![{f}]({root}/{f})|{f.replace('.png', '')}|")
                    if count == 3:
                        my_file.write(f"![{f}]({root}/{f})|{f.replace('.png', '')}|\n")
                        count = 0
        my_file.write("\n")


if __name__ == "__main__":
    main()
