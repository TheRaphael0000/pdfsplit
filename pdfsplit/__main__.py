#!/usr/bin/env python

import argparse
from .spliter import split, create_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Slice into a grid every pages of a pdf and create a new pdf with every cells of the grid")
    parser.add_argument("input", help="Input file")
    parser.add_argument("output", help="Output file (doesn't work with the same as input file)")
    parser.add_argument("-r", "--rows", type=int, default=1, help="Number of rows")
    parser.add_argument("-c", "--cols", type=int, default=1, help="Number of colunms")
    parser.add_argument("-x", "--xflip", action="store_true", help="Horizontal flip of the reading grid direction (default: left to right)")
    parser.add_argument("-y", "--yflip", action="store_true", help="Vertical flip of the reading grid direction (default: up to bottom)")
    parser.add_argument("-t", "--transpose", action="store_true", help="Transpose the way of reading the grid (default: horizontal then vertical)")

    args = parser.parse_args()
    pages = split(args.input, args.rows, args.cols, args.xflip, args.yflip, args.transpose)
    pdf = create_pdf(pages)
    pdf.write(open(args.output, "wb"))


if __name__ == "__main__":
    main()
